const input = ``;

const _test = `>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>`;

type Block = {
	x: number;
	y: number;
};

// 0 is the bottom left corner outside of the grid

// 3 |
// 2 |
// 1 |
//   + - - - - - - -
// 0   1 2 3 4 5 6 7

type Shape = Block[];

// you spawn with left 2 away from the left wall
// and bottom 3 above the highest block, but we'll do 4 because of the way set things up
const makeShape = (shape: number, highest: number): Shape => {
	switch (shape) {
		case 0:
			{
				// horizontal line
				const y = highest + 4;
				return [
					{ x: 3, y },
					{ x: 4, y },
					{ x: 5, y },
					{ x: 6, y }
				];
			}
			break;
		case 1:
			{
				// plus
				const bottom = highest + 4;
				return [
					{ x: 3, y: bottom + 1 },
					{ x: 4, y: bottom + 1 },
					{ x: 5, y: bottom + 1 },
					{ x: 4, y: bottom },
					{ x: 4, y: bottom + 2 }
				];
			}
			break;
		case 2:
			{
				// backwards l
				//     #
				//     #
				// # # #
				const bottom = highest + 4;
				return [
					{ x: 3, y: bottom },
					{ x: 4, y: bottom },
					{ x: 5, y: bottom },
					{ x: 5, y: bottom + 1 },
					{ x: 5, y: bottom + 2 }
				];
			}
			break;
		case 3:
			{
				// vertical line
				const bottom = highest + 4;
				return [
					{ x: 3, y: bottom },
					{ x: 3, y: bottom + 1 },
					{ x: 3, y: bottom + 2 },
					{ x: 3, y: bottom + 3 }
				];
			}
			break;
		case 4:
			{
				// square
				const bottom = highest + 4;
				return [
					{ x: 3, y: bottom },
					{ x: 3, y: bottom + 1 },
					{ x: 4, y: bottom },
					{ x: 4, y: bottom + 1 }
				];
			}
			break;
	}
	return [];
};

const move = (state: Set<Block>, dir: string, shape: Shape) => {
	const moveDown = (s: Shape) => s.map(b => b.y--);
	const moveLeft = (s: Shape) => s.map(b => b.x--);
	const moveRight = (s: Shape) => s.map(b => b.x++);

	switch (block) {
		case 0:
			{
				// horizontal line
				if (dir === ">") {
				}
			}
			break;
		case 1: {
		}
	}
};

const simulate = (input: string, iterations: number) => {
	let moves = input.split("");
	let mvlen = moves.length;
	let currentMove = 0;

	// 0 = horizontal line
	// 1 = plus
	// 2 = backwards l
	// 3 = vertical line
	// 4 = square
	let nextShape = 0;

	// highest column
	let highest = 0;

	const state = new Set<Block>();

	let currShape = makeShape(nextShape, highest);
	nextShape = (nextShape + 1) % 5;

	while (iterations > 0) {}
};
