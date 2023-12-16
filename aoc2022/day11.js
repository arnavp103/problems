"use strict";

const input = `Monkey 0:
Starting items: 83, 88, 96, 79, 86, 88, 70
Operation: new = old * 5
Test: divisible by 11
  If true: throw to monkey 2
  If false: throw to monkey 3

Monkey 1:
Starting items: 59, 63, 98, 85, 68, 72
Operation: new = old * 11
Test: divisible by 5
  If true: throw to monkey 4
  If false: throw to monkey 0

Monkey 2:
Starting items: 90, 79, 97, 52, 90, 94, 71, 70
Operation: new = old + 2
Test: divisible by 19
  If true: throw to monkey 5
  If false: throw to monkey 6

Monkey 3:
Starting items: 97, 55, 62
Operation: new = old + 5
Test: divisible by 13
  If true: throw to monkey 2
  If false: throw to monkey 6

Monkey 4:
Starting items: 74, 54, 94, 76
Operation: new = old * old
Test: divisible by 7
  If true: throw to monkey 0
  If false: throw to monkey 3

Monkey 5:
Starting items: 58
Operation: new = old + 4
Test: divisible by 17
  If true: throw to monkey 7
  If false: throw to monkey 1

Monkey 6:
Starting items: 66, 63
Operation: new = old + 6
Test: divisible by 2
  If true: throw to monkey 7
  If false: throw to monkey 5

Monkey 7:
Starting items: 56, 56, 90, 96, 68
Operation: new = old + 7
Test: divisible by 3
  If true: throw to monkey 4
  If false: throw to monkey 1`;

const _test = `Monkey 0:
Starting items: 79, 98
Operation: new = old * 19
Test: divisible by 23
  If true: throw to monkey 2
  If false: throw to monkey 3

Monkey 1:
Starting items: 54, 65, 75, 74
Operation: new = old + 6
Test: divisible by 19
  If true: throw to monkey 2
  If false: throw to monkey 0

Monkey 2:
Starting items: 79, 60, 97
Operation: new = old * old
Test: divisible by 13
  If true: throw to monkey 1
  If false: throw to monkey 3

Monkey 3:
Starting items: 74
Operation: new = old + 3
Test: divisible by 17
  If true: throw to monkey 0
  If false: throw to monkey 1`;

class Monkey {
	// id is a number, items is a list of worry levels, operation is a function, test is a function that also passes
	constructor(id, items, operation, test) {
		this.id = id;
		this.items = items;
		this.operation = operation;
		this.test = test;
		this.inspectionCounter = 0;
	}

	pass(monkeyID) {
		const target = jungle.find(m => m.id === monkeyID);
		target.items.push(this.items.shift());
	}

	toString() {
		return `Monkey ${this.id}: ${this.items} - Inspections: ${this.inspectionCounter}`;
		// return `Monkey ${this.id}: - Inspections: ${this.inspectionCounter}`;
	}

	play() {
		// for each and for of don't work since we mutate the array while reading it
		// this works because a monkey can never keep an item after a test
		// console.log(this.toString());
		while (this.items.length > 0) {
			let item = this.items[0];
			// idk why letting item be a var and mutating it directly doesn't work
			item = this.operation(item, lcm);
			this.items[0] = item; // since item is copied by value
			this.test(item, lcm);
			this.inspectionCounter++;
		}
	}
}

const parse = input => {
	const lines = input.split("\n\n").map(monkey => monkey.split("\n"));
	const monkeys = {};
	lines.forEach(monkey => {
		const id = parseInt(
			monkey[0].slice(monkey[0].length - 2, monkey[0].length - 1)
		);
		const items = monkey[1]
			.slice(monkey[1].indexOf(": ") + 2)
			.split(", ")
			.map(worryLevel => parseInt(worryLevel));
		// indirect eval with optional chaining is safer and faster since its evaluated like it's its own script
		// but we have to do direct eval to be able to use the variable old
		const op = Function(
			"old, lcm",
			`return Math.floor((${monkey[2].slice(
				monkey[2].indexOf("= ") + 2
			)})/ 3)`
		);
		const divisor = parseInt(monkey[3].split(" ")[3]);
		lcm *= divisor;
		const test = Function(
			"worryLevel, lcm",
			`"use strict";
			if (worryLevel % ${parseInt(monkey[3].split(" ")[3])}=== 0) {
			this.pass(${monkey[4].slice(monkey[4].indexOf("to monkey ") + 10)});
			} else {
				this.pass(${monkey[5].slice(monkey[5].indexOf("to monkey ") + 10)});
			}`
		);
		// console.log(id, items, op, test);
		const m = new Monkey(id, items, op, test);
		// console.log(m.operation.toString());
		// console.log(m.test.toString());
		monkeys["m.id"] = m;
		jungle.push(m);
	});
};

const jungle = [];
let lcm = 1;

function monkeyBusiness(input, parse, rounds = 20) {
	parse(input);
	console.log(jungle);

	for (let i = 0; i < rounds; i++) {
		for (const monkey of jungle) {
			monkey.play();
		}
		if ((i + 1) % 100 === 0) {
			console.log(
				`After round ${
					i + 1
				} the monkeys hold these items with worry levels and inspected `
			);
			for (const monkey of jungle) {
				console.log(monkey.toString());
			}
		}
	}
	const topPerformers = jungle
		.sort((m1, m2) => m2.inspectionCounter - m1.inspectionCounter)
		.slice(0, 2);
	console.log(
		topPerformers[0].inspectionCounter * topPerformers[1].inspectionCounter
	);
}

monkeyBusiness(input, parse);

// part 2
// the strategy is just change the eval function and hope that js automatically uses bigints to handle the huge numbers
// 15 mins later - ok that didn't work
// we can convert ints to bigints by appending an n to them. bigints and ints are not automatically converted
const parse2 = input => {
	const lines = input.split("\n\n").map(monkey => monkey.split("\n"));
	const monkeys = {};
	lines.forEach(monkey => {
		const id = parseInt(
			monkey[0].slice(monkey[0].length - 2, monkey[0].length - 1)
		);
		// only changes are appending an n to the numbers and one BigInt constructor
		const items = monkey[1]
			.slice(monkey[1].indexOf(": ") + 2)
			.split(", ")
			.map(worryLevel => parseInt(worryLevel));

		const op = Function(
			"old, lcm",
			`return (${monkey[2].slice(monkey[2].indexOf("= ") + 2)}) % lcm;`
		);
		const divisor = parseInt(monkey[3].split(" ")[3]);
		lcm *= divisor;
		const test = Function(
			"worryLevel, lcm",
			`"use strict";
			if (worryLevel !== 0 && worryLevel % ${parseInt(
				monkey[3].split(" ")[3]
			)} === 0) {
			this.pass(${monkey[4].slice(monkey[4].indexOf("to monkey ") + 10)});
			} else {
				this.pass(${monkey[5].slice(monkey[5].indexOf("to monkey ") + 10)});
			}`
		);
		const m = new Monkey(id, items, op, test);
		monkeys["m.id"] = m;
		jungle.push(m);
	});
};

monkeyBusiness(input, parse2, 10000);

/*
 * up till round 1000 the program runs fine with matching inspections
 * we can't not do the op by looking ahead at the test since that value is passed to another monkey
 * so not dividing won't work since we have to also pass the values and we can't trust their divsions to hold
 * we exceeded the maximum size of a bigint which is annoying
 * rewriting the op and test function won't help if the bigints are whats broken
 * the trick: all the divisor are coprime (prime actually) so chinese remainder theorem
 * If we store all of our worry levels under a modulo N (choosing N is the tricky part without CRT)
 * x === a (mod N) <=> x = a + kN for some integer x, a, k
 * Ok so adding (and subtracting) a number under a modulo is closed
 * 12 === 2 (mod 5)
 * 12 + 2 === 2 + 2 (mod 5)
 * x + b = a + b + kN
 * So is multiplying
 * 12 === 2 (mod 5)
 * 12 * 2 === 2 * 2 (mod 5)
 * x*b = b(a + kN)
 * but we also have to divide in our test function and division is not always allowed under modulo
 * 4 === 4 (mod 6)
 * 4 / 5 === 4 / 5 (mod 6) looks weird; <=> 5*y === 4 (mod 6) - division def (a/b = c <=> a = b*c) so y = 2 is fine, but
 * 4 / 2 === 4 / 2 (mod 6) doesn't work since 2*y === 4 (mod 6) has y = 2 or y = 5
 * since there's more than one solution to we can't do division
 * 20 === 4 (mod 8)
 * 20 / 4 === 4 / 4 (mod 8) doesn't work since 20 and 8 are not coprime, 5 === 1 (mod 8) is not true
 * You can only do modular division when the multiplicative inverse exists
 * the inverse of x mod N is int x^-1 s.t. x * x^-1 === 1 (mod N) <=> x * x^-1 = 1 + kN (x * x^-1 = 1 is the standard inverse non mod)
 * An inverse exists iff x and N are coprime and the inverse is unique
 * if the inverse exists then division is closed under modulo
 * xy === b (mod N) <=> y === b * x^-1 (mod N) for integers x, y, b, N
 * so how does this help our problem? the worry levels(w1 ... wk) get too big so instead we'd like to store them under a modulo N
 * then we can find a st w1 / b (mod N) and we can just use a in place of w1 / b
 * then the additions and multiplications will still give the same result in test
 * however when we pass it to another monkey it may not be coprime to the divisor of that monkey (from the additions)
 * since we can subtract out multiples of the divisor we can take the lcm of the divisors and use that as N from CRT
 * This works since they're coprime so no repeated multiples of the divisor
 * i find it helpful to think of one w at a time going through all its ops in all the rounds rather than each w doing one op than another
 */
