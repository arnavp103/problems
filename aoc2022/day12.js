"use strict";

const input = `abcccaaaaaaccccccccaaaaaccccccaaaaaaccccccaaaaaaaacccaaaaaaaccaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa
abcccaaaaaacccccccaaaaaaccccaaaaaaaacccccccaaaaaaaaaaaaaaaaccaaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa
abccccaaaaacaaaccaaaaaaaacccaaaaaaaaacccccccaaaaaaaaaaaaaaaacaaaaaacccccccccaaacccccccccccaaaaaaaaccccccccccaaccccccccccccccccaaaaaa
abccccaaaaccaaaaaaaaaaaaacccaaaaaaaaaacccccaaaaaaaaaaaaaaaaaaacaaaacccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccccccccccccccccccaaa
abcccccccccaaaaaacccaacccccccccaaacaaaccccccaacccccccaaaaaaaaacaacccccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccacaaccccccccccccaaa
abcccccccccaaaaaacccaacccccccccaaacccccccccccccccccccaaaacaaaacccccccaacaaccaaaccccccccccaccaaaaacacccccccccaaaacaaaaccccccccccccaac
abccccccccccaaaaacccccccccccccccacccaaaacccccccccccccaaaacccccccccccccaaaacccccccccccaacccccaaaaccccccccjjjjaaaaaaaaaccccccccccccccc
abccccccccccaaaacccccccccccccccccccaaaaacccccccccccccaaaccccccccccccccaaaaacccccccccaaaaaacccaaccccccccjjjjjjkkaaaacccccccccaacccccc
abcccccaaccccccccccccccccccccccccccaaaaaacccccccccccccaacccccccccccccaaaaaaccccccccccaaaaaccccccccccccjjjjjjjkkkkaacccccaacaaacccccc
abccaaaacccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccaaaacaccccccccaaaaaaaccccaacccccjjjjoooookkkkkkkklllaaaaaaacccc
abccaaaaaacccccccccccccccccccccccccaaaaacccccccccccccccccccccccccccccccaaccccccccccaaaaaaaaccaaaaccccjjjoooooookkkkkkkllllaaaaaacccc
abcccaaaaacccccccccccccccccccccccccccaaaccccccccaaaacccccccccccccccccccccccccccccccaaaaaaaaccaaaaccccjjooooooooppkkppplllllaccaacccc
abccaaaaaccccccccccccaccccccccccccccccccccccccccaaaacccccccccccccccccccccccccccccccccaaacacccaaaacccijjooouuuuoppppppppplllccccccccc
abcccccaacccccccccccaaaaaaaaccccccccccccccccccccaaaaccccaaccccccccaaacccccccccccccaacaaccccccccccccciijoouuuuuuppppppppplllcccaccccc
abcccccccccccccccccccaaaaaaccccccccccccccccccccccaaccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiiiootuuuuuupuuuvvpppllccccccccc
abcccccccccccccccccccaaaaaaccaaaaacccccccccccccccccccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiinnotuuxxxuuuuvvvpppllccccccccc
abccccccccccccccacccaaaaaaaacaaaaaaacccccccccccccccccccaaaacccccccaaacccccaaaaccaaaaaccccaaccccccciiiinnnttxxxxuuyyyvvqqqllccccccccc
abcccccccccccaaaaccaaaaaaaaaaaaaaaaaaccaacccccccccccccccccccccccccccccccccaaaacccaaaaaccaaacccccciiinnnnnttxxxxxyyyyvvqqqllccccccccc
abaaaacccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaacccaaaaaacaaaccccciiinnnnttttxxxxxyyyyvvqqmmmccccccccc
abaaaaccccccccaaaaacccaaaaacaaaaaacaaaaaaccccccccccccccccaaccccccccccccccccaacccccccaaaaaaaaaaciiinnnnttttxxxxxyyyyvvqqqmmmccccccccc
SbaaaacccccccaaaaaccccaaaaaccaaaaaaaaaaaccccccccccccccccaaacaacccccccccccccccccccccccaaaaaaaaachhhnnntttxxxEzzzzyyvvvqqqmmmccccccccc
abaaaacccccccaacaacccccaaaaaaaacaaaaaaaaaccccccccccccccccaaaaaccccccccccccccccccccccccaaaaaaacchhhnnntttxxxxxyyyyyyvvvqqmmmdddcccccc
abaaaacccccccccccccccccccaaaaaacaaaaaaaaaacccccccccccccaaaaaaccccccccaaaccccccccccccccaaaaaaccchhhnnntttxxxxywyyyyyyvvvqqmmmdddccccc
abaacccccccccccccccccccaaaaaaacccccaaaaaaacccccccccccccaaaaaaaacccccaaaacccccccccccccaaaaaaacaahhhmmmttttxxwwyyyyyyyvvvqqmmmdddccccc
abcccccccccccccccccccccaaaaaaacaaccaaacccccccccccccccccaacaaaaacccccaaaacccccccccccccaaacaaaaaahhhmmmmtsssswwyywwwwvvvvqqqmmdddccccc
abcccccccccccccccaaaccccaaaaaaaaaacaaccaaccccccccccccccccaaacaccccccaaaacccccccccccccccccaaaaacahhhmmmmmsssswwywwwwwvvrrqqmmdddccccc
abcccccccccccccaaaaaaccccaaaaaaaaaccaaaacccccccccccccccccaacccccccccccccccccccccccaaaccccaaaaaaahhhhhmmmmssswwwwwrrrrrrrrmmmmddccccc
abcccccccccccccaaaaaaccccaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaacccccaaaaachhhhhmmmmsswwwwrrrrrrrrrkkmdddccccc
abccccccccccccccaaaaaccccccaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaaccccaaaaacccchhggmmmssswwrrrrrkkkkkkkkdddacccc
abccaaaacccccccaaaaacccccccccaaaaaacaaaaacccccccccccccccccccccccccccccccccccccccaaaaaaccccaacaaaccccggggmmsssssrrlkkkkkkkkkdddaccccc
abccaaaacccccccaaaaacccccccccaaaaaaccccaacccccccccccccccccccccccccccccccccccccccaaaaaccccccccaaccccccgggmllssssrllkkkkkkkeeeddaccccc
abccaaaacccccccaaacccccccccccaaaaaacccccccccccccccccccaacccccccccccccccccccccccaaaaaacccccccccccccccccggllllssslllkkeeeeeeeeeaaacccc
abcccaaccccccccaaacaaaccccccaaaaaaaaaaacccccccccccccaaaaaacccccccccccccccccccccaaacaaacccccaacccccccccggglllllllllfeeeeeeeeaaaaacccc
abccccccccccaaaaaaaaaaccccccccccccaccaaaccacccccccccaaaaaaccccaaccaacccaaccccccaaaaaaacccccaaccccccccccggglllllllfffeeecccaaaaaacccc
abccccccccccaaaaaaaaacccccccccccccccaaaaaaaccccccccccaaaaaccccaaaaaacccaaaaaaccaaaaaacccaaaaaaaacccccccggggllllfffffccccccaacccccccc
abcccccccccccaaaaaaacccccccccccccccccaaaaaaccaacccccaaaaaccccccaaaaacccaaaaaacaaaaaaacccaaaaaaaaccccccccgggffffffffccccccccccccccccc
abccccccccccccaaaaaaacccccccccccccaaaaaaaaacaaaaccccaaaaacaaaaaaaaaacaaaaaaacaaaaaaaaaccccaaaacccccccccccggffffffacccccccccccccccaaa
abccccccccccccaaaaaaacaaccccccccccaaaaaaaaacaaaacccccaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaacccaaaaacccccccccccaffffaaaaccccccccccccccaaa
abccccccccccccaaacaaaaaacccccccccccaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaacccaaacaaaccaaaaaacccccccccccccccccaaaccccccccccccccaaa
abccccccccccccaaccaaaaaccccccccccccccaaaaaaaccccaaaaaaaaaaaaccccaacccccaaaaaacccaaaccccccaaccaacccccccccccccccccaaacccccccccccaaaaaa
abcccccccccccccccaaaaaaaaccccccccccccaacccacccccccaaaaaaaaaaccccaacccccaaccccccccaccccccccccccccccccccccccccccccccccccccccccccaaaaaa`;

const _test = `Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi`;

function parse(input, graph) {
	let start;
	let end;
	// x to the right and y down
	const letters = input.split("\n").map(line => line.split(""));
	function close(origin, target) {
		let first = letters[origin[1]][origin[0]];
		first = first === "S" ? "a" : first === "E" ? "z" : first;
		let second = letters[target[1]][target[0]];
		second = second === "S" ? "a" : second === "E" ? "z" : second;
		// console.log(first, second, origin, target);
		// the change that i shouldve caught 3 hours ago
		return second.charCodeAt(0) - first.charCodeAt(0) <= 1;
	}

	letters.map((line, y) => {
		line.map((char, x) => {
			// console.log(letters[y][x], x, y)
			if (char === "S") {
				start = [x, y];
				char = "a";
			} else if (char === "E") {
				end = [x, y];
				char = "z";
			}
			graph[[x, y]] = [];
			// left right up down
			// remember that object keys are strings
			if (x > 0 && close([x, y], [x - 1, y])) {
				graph[[x, y]].push([x - 1, y]);
			}
			if (x < line.length - 1 && close([x, y], [x + 1, y])) {
				graph[[x, y]].push([x + 1, y]);
			}
			if (y > 0 && close([x, y], [x, y - 1])) {
				graph[[x, y]].push([x, y - 1]);
			}
			if (y < letters.length - 1 && close([x, y], [x, y + 1])) {
				graph[[x, y]].push([x, y + 1]);
			}
		});
	});
	return [[start], end, graph];
}

const heuristic = (a, b) => {
	// manhattan distance
	return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
};

function stringKey([x, y]) {
	return `${x},${y}`;
}

function shortest(input, parse) {
	let graph = {};
	// makes a graph of neighbors of [x, y] coordinates
	let start;
	let end;
	[start, end, graph] = parse(input, graph);

	// astar to find the shortest path with manhattan distance heuristic
	function astar(graph, start, end) {
		// console.log(graph, start, end);
		const paths = {};
		const fscores = {};
		for (const key in graph) {
			paths[key] = [Infinity, null]; // current distance in gscore, previous
			fscores[key] = Infinity;
		}
		paths[start] = [0, null];
		fscores[start] = heuristic(start, end);

		const considering = new Set();
		considering.add(start);

		while (considering.size > 0) {
			// determing the node with the lowest fscore
			let current = null;
			for (const key of considering.values()) {
				// choose the node with the lowest fscore
				// i was doing something else lol its fixed now
				if (current === null || fscores[key] < fscores[current]) {
					current = key;
				}
			}
			// to compare arrays we can't compare pointers
			if (stringKey(current) === stringKey(end)) {
				// || [...Array(101).keys()].map(x => x*10+1000).includes(i)) {
				const path = [];
				let node = current;
				while (node !== null) {
					path.push(node);
					node = paths[node][1];
				}
				console.log(path.reverse()); //.reduce((acc, cur) => acc+"->"+cur , ''));
				return path.length - 1;
			}

			considering.delete(current);
			// console.log("Current", current);
			for (const neighbor of graph[current]) {
				// get the g score of the current node and add 1 to represent the neighbors gscore
				const tentative = paths[current][0] + 1;
				// if your gscore is lower than your neighbors then update the neighbor
				if (tentative < paths[neighbor][0]) {
					paths[neighbor][1] = current;
					paths[neighbor][0] = tentative;
					fscores[neighbor] = tentative + heuristic(neighbor, end);
					considering.add(neighbor);
				}
			}
		}
		console.log("error no path found"); //, paths);
	}

	const shortest = start
		.map(x => astar(graph, x, end))
		.sort((a, b) => a - b)[0];
	return shortest;
}

console.log(shortest(input, parse));

// this is taking too long too run
// indeed djikstra's is not the right algorithm
// lets use astar

// after hours of debugging i realized the problem was impossible
// then i realized that didn't make sense and turns out i read the spec wrong
// you can't go up more than 1 but you can go down more than 1 annoyingly

// part 2

// all we have to do is rewrite the parse function to make a graph of all the "a"s as starts
// if two a's are connected then we can always ignore the one with the lower heuristic
function parse2(input, graph) {
	const start = [];
	let end;

	const letters = input.split("\n").map(line => line.split(""));
	let flag1 = false;
	let flag2 = false;

	loop1: for (const [y, line] of letters.entries()) {
		for (const [x, letter] of line.entries()) {
			if (letter === "S") {
				start.push([line.indexOf(letter), letters.indexOf(line)]);
				letters[y][x] = "a";
				flag1 = true;
			}
			if (letter === "E") {
				end = [line.indexOf(letter), letters.indexOf(line)];
				letters[y][x] = "z";
				flag2 = true;
			}
			if (flag1 && flag2) {
				break loop1; // what! how have i never seen this before
			}
		}
	}
	// x to the right and y down
	function close(origin, target) {
		const first = letters[origin[1]][origin[0]];
		const second = letters[target[1]][target[0]];
		// console.log(first, second, origin, target);
		// the change that i shouldve caught 3 hours ago
		return second.charCodeAt(0) - first.charCodeAt(0) <= 1;
	}
	letters.map((line, y) => {
		line.map((char, x) => {
			// console.log(letters[y][x], x, y)
			if (char === "a") {
				start.push([x, y]);
			}
			graph[[x, y]] = [];
			// left right up down
			// remember that object keys are strings
			if (x > 0 && close([x, y], [x - 1, y])) {
				graph[[x, y]].push([x - 1, y]);
			}
			if (x < line.length - 1 && close([x, y], [x + 1, y])) {
				graph[[x, y]].push([x + 1, y]);
			}
			if (y > 0 && close([x, y], [x, y - 1])) {
				graph[[x, y]].push([x, y - 1]);
			}
			if (y < letters.length - 1 && close([x, y], [x, y + 1])) {
				graph[[x, y]].push([x, y + 1]);
			}

			// if (char === "a") {
			// 	for (const neighbor of graph[[x, y]]) {
			// 		const l = letters[neighbor[1]][neighbor[0]];
			// 		if (
			// 			l == "a" &&
			// 			heuristic(neighbor, end) < heuristic([x, y], end) &&
			// 			graph[neighbor].filter(([x, y] => letter[y][x] == "a").length > 0
			// 		) {
			// 			console.log(l, heuristic(neighbor,end), heuristic([x, y],end), [x, y]);
			// 			dontAdd.add(stringKey([x, y]));
			// 			start = start.filter(
			// 				(x) => stringKey(x) != stringKey([x, y])
			// 			);
			// 		}
			// 	}
			// }
		});
	});
	console.log("Start", start);
	return [start, end, graph];
}

console.log(shortest(input, parse2));
// can't believe a* was the only optimization i needed
// this ran pretty fast

/*
// we can just use djikstra's to get a lookup table
	const djikstra = (graph, start, end) => {
		let visited = new Set();
		let lookup = new Map();
		// const minDist = Math.abs(start[0] - end[0]) + Math.abs(start[1] - end[1]);

		for (const key in graph) {
			// distance, previous
			// this is already a string
			lookup.set(key, [Infinity, null]);
		}
		lookup.set(stringKey(start), [0, null]);
		let current = stringKey(start);

		while (!visited.has(stringKey(end))) {
			visited.add(current);
			let [shortest, shortestKey] = [Infinity, null];
			// console.log(visited, lookup, neighbors, "current", current);
			for (const neighbor of neighbors) {
				if (visited.has(stringKey(neighbor))) {
					continue;
				}

				let [distance, previous] = lookup.get(stringKey(neighbor));
				let newDistance = lookup.get(current)[0] + 1;
				// console.log("distance:", distance, "new distance:", newDistance, "current:", current);
				if (newDistance < distance) {
					// console.log("new distance + neigb:", newDistance, neighbor);
					lookup.set(stringKey(neighbor), [newDistance, current]);
					if(newDistance < shortest) {
						shortest = newDistance;
						shortestKey = stringKey(neighbor);
					}
				}
			}
			// if you select a shortest which doesn't create any new shorter paths
			if(shortestKey === null) {
				// console.log("shortestkey is null", current, neighbors, visited);
				let min = lookup.get(stringKey(end))[0];
				for (let [key, value] of lookup) {
					// if we haven't visited it and it's the shortest path that's at least shorter than the currently known fastest path
					if (!visited.has(key) && value[0] <= min) {
						min = value[0];
						current = key;
					}
				}
			} else {
				current = shortestKey;
			}
		}
		return lookup.get(stringKey(end))[0];
	};
*/
