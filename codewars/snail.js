snail = function (array) {
	if (array.length === 1 && array[0].length === 0) return [];
	let row = 0;
	let col = 0;
	const result = [];

	let bound = array.length - 1;
	let dir = "r";

	while (result.length < array.length * array.length) {
		result.push(array[row][col]);

		switch (dir) {
			case "r":
				if (col === bound) {
					dir = "d";
					row++;
				} else {
					col++;
				}
				break;
			case "d":
				if (row === bound) {
					dir = "l";
					col--;
				} else {
					row++;
				}
				break;
			case "l":
				if (col === array.length - bound - 1) {
					dir = "u";
					row--;
				} else {
					col--;
				}
				break;
			case "u":
				// here we dont need - 1 since we're going to hit a new low ceiling
				if (row === array.length - bound) {
					dir = "r";
					col++;
					// decrease bound after completing a full loop
					bound--;
				} else {
					row--;
				}
				break;
		}
	}

	return result;
};

// const array = [
// 	[1, 2, 3],
// 	[8, 9, 4],
// 	[7, 6, 5]
// ];
const array = [[]];
console.log(snail(array));

// traverse the matrix in a clockwise spiral
// array = [[1,2,3],
//          [8,9,4],
//          [7,6,5]]
// snail(array) #=> [1,2,3,4,5,6,7,8,9]
