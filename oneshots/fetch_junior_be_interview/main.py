"""
API for fetch rewards backend to handle transactions and points
"""

import bisect
from dataclasses import dataclass
from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()


@dataclass
class Transaction:
    """
    A transaction model from a payer to the payee, which is whichever user owns the transaction
    """

    payer: str
    points: int
    timestamp: datetime

    # the sort order is based on the timestamp
    def __lt__(self, other):
        return self.timestamp < other.timestamp


@dataclass
class SpendPoints:
    """
    A spend points model from a user spending their own points
    """

    points: int


@dataclass
class User:
    """
    User dataclass containing the user's name, total points,
    a dictionary of payers and their points and the sorted transactions according to datetime

    Note: The payers can be recomputed from the transactions
    but we denormalize the data for faster reads
    """

    name: str
    payers: dict[str, int]
    transactions: list[Transaction]


# the global state of the users
# this would typically be stored in a durable data store
# but for the exercise, we will use an in-memory dictionary
USERS = {}


@app.get("/api/v1/health")
def status():
    """
    Health check for the API
    """
    return {"status": "ok", "timestamp": datetime.now().isoformat(timespec="seconds")}


@app.get("/api/v1/users/{username}/balance")
def get_user_balance(username: str):
    """
    Get the balance of a user's payers
    """

    user = USERS.get(username)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {username} not found")

    return user.payers


@app.post("/api/v1/users/{username}/transactions", response_model=dict[str, int])
def add_transaction(username: str, transaction: Transaction):
    """
    Add a transaction to the user's account.
    This method is also responsible for creating the user
    if they don't exist.

    If the transaction amount is negative,
    and the payer's balance can handle it
    the balance will be progressively deducted from the
    oldest transactions until the transaction amount
    has been used up.
    """
    user = USERS.get(username)
    if not user:
        user = User(name=username, payers={}, transactions=[])
        USERS[username] = user

    # if the transaction points are negative
    if transaction.points < 0:
        payer_balance = user.payers.get(transaction.payer, 0)

        # check if that payer's balance is enough to deduct the points
        if payer_balance + transaction.points < 0:
            raise HTTPException(
                status_code=400,
                detail=f"Payer {transaction.payer} will have a negative balance",
            )

        # if they can pay for it, instead of adding it to transactions
        # distribute the loss amongst the first k transactions of that payer
        # so that all user.transactions have positive points
        # the payer also need enough points uptil that timestamp
        total = -transaction.points
        new_transactions = []
        final = 0

        for i, tx in enumerate(user.transactions):
            if total <= 0:
                final = i
                break
            if tx.timestamp > transaction.timestamp:
                raise HTTPException(
                    status_code=400,
                    detail=f"{transaction.payer} would be negative at {transaction.timestamp}",
                )
            if tx.payer == transaction.payer:
                if tx.points <= total:
                    total -= tx.points
                    continue
                tx.points -= total
                total = 0
            new_transactions.append(tx)

        new_transactions.extend(user.transactions[final:])
        user.transactions = new_transactions
        user.payers[transaction.payer] += transaction.points
        return user.payers

    # bisect to insert the transaction in a sorted order
    bisect.insort(user.transactions, transaction)

    # update the payers
    new_payer_balance = user.payers.get(transaction.payer, 0) + transaction.points
    user.payers[transaction.payer] = new_payer_balance

    return user.payers


@app.post("/api/v1/users/{username}/spend", response_model=list[dict])
def spend_points(username: str, spend: SpendPoints):
    """
    Spend points from the user's payers
    """

    user = USERS.get(username)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {username} not found")

    total = spend.points
    new_start = 0
    total_points = sum(user.payers.values())

    if total_points < total:
        raise HTTPException(
            status_code=400, detail=f"Insufficient points to spend {total}"
        )

    payer_spent = {}

    for i, tx in enumerate(user.transactions):
        if total <= 0:
            break

        if tx.points <= total:
            total -= tx.points
            user.payers[tx.payer] -= tx.points
            payer_spent[tx.payer] = payer_spent.get(tx.payer, 0) - tx.points
            new_start = i
            continue

        # if the transaction has more points than the total
        # remove part of the points from the transaction
        user.payers[tx.payer] -= total
        user.transactions[i].points -= total
        payer_spent[tx.payer] = payer_spent.get(tx.payer, 0) - total
        total = 0

    # set the transactions list to the new start
    user.transactions = user.transactions[new_start + 1 :]

    payer_list = []
    for payer, points in payer_spent.items():
        payer_list.append({"payer": payer, "points": points})

    return payer_list
