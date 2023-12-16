"use strict";

const input = `addx 1
addx 4
addx -2
addx 3
addx 3
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 4
noop
addx -1
noop
addx 3
addx -10
addx -17
noop
addx -3
addx 2
addx 25
addx -24
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 14
addx -9
noop
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -5
noop
noop
addx -19
addx -11
addx 5
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 4
noop
noop
addx 5
noop
noop
noop
addx 5
addx -3
addx 8
noop
addx -15
noop
addx -12
addx -9
noop
addx 6
addx 7
addx -6
addx 4
noop
noop
noop
addx 4
addx 1
addx 5
addx -11
addx 29
addx -15
noop
addx -12
addx 17
addx 7
noop
noop
addx -32
addx 3
addx -8
addx 7
noop
addx -2
addx 5
addx 2
addx 6
addx -8
addx 5
addx 2
addx 5
addx 17
addx -12
addx -2
noop
noop
addx 7
addx 9
addx -8
addx 2
addx -33
addx -1
addx 2
noop
addx 26
addx -22
addx 19
addx -16
addx 8
addx -1
addx 3
addx -2
addx 2
addx -17
addx 24
addx 1
noop
addx 5
addx -1
noop
addx 5
noop
noop
addx 1
noop
noop`;

const test = `addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop`;

// can only do one instruction at a time so if we see multiple addxs we can just add 2*n to the cycle counter

function parse(input, vm) {
	const lines = input.split("\n");
	lines.forEach((instruction) => {
		const op = instruction.slice(0, 4);
		switch (op) {
			case "noop":
				vm.noop();
				break;
			case "addx":
				const [_, arg] = instruction.split(" ");
				vm.addx(Number(arg));
				break;
			default:
				break;
		}
	});
}

const vm = {
	cycleCounter: 1,
	X: 1,

	tick() {
		if (this.test(this.cycleCounter)) {
			this.hook();
		}
		this.cycleCounter++;
	},

	noop() {
		this.tick();
	},

	addx(arg) {
		this.tick();
		this.tick();
		this.X += arg;
	},

	test() {
		// default test always returns false
		return false;
	},

	hook() {
		// default hook does nothing
	}
};

const part1 = Object.create(vm);

part1.signalStrength = 0;

part1.test = function(cycle) {
	const test = (cycle + 20) % 40 === 0;
	return test;
};

// you need to call function like this instead of arrow syntax to use 'this'
part1.hook = function() {
	this.signalStrength += this.cycleCounter * this.X;
};

parse(input, part1);

console.log(part1.signalStrength);


// part 2

const part2 = Object.create(vm);

// 40 wide 6 high screen
part2.screen = Array(6 * 40).fill(".");

part2.render = function() {
	for (let i = 0; i < 6; i++) {
		console.log(this.screen.slice(i * 40, (i + 1) * 40).join(""));
	}
};

part2.test = function(cycle){
	// the crt always draws 1 px per cycle and its always 1 less than the cycle counter
	// there's no concpet of vertical position so we have to mod the cycle counter and treat the pos as the first row
	const pos = (cycle-1) % 40;
	const test = pos === this.X - 1 || pos === this.X  || pos === this.X + 1;
	return test;
}

part2.hook = function() {
	this.screen[this.cycleCounter-1] = "#";
}

parse(input, part2);

part2.render();
