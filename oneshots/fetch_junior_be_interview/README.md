# Fetch Junior Backend Developer Take Home Interview

This creates a simple RESTful API that allows adding and spending user's points.
Some liberties were taken when the problem description was unclear.
The API is built using FastAPI and the data is stored in memory.

## Installation

This guide is designed for someone with no python/fastapi experience to get
the service up and running.

Assuming an Ubuntu environment, first clone the repository and navigate to the directory

Then install python3 and pip3

```bash

sudo apt update
sudo apt install python3 python3-pip

```

Then install the required packages

```bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

This will install the required packages in a virtual environment.
From there you can run the service.

## Usage

First run the service

```bash

fastapi run

```

Then you can follow the link on the API docs to see the available endpoints.

To add a user, use the add transaction endpoint and put in a username to create a user.

From there you can try out the endpoints on the UI.

