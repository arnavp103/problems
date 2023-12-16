const input = `Sensor at x=407069, y=1770807: closest beacon is at x=105942, y=2000000
Sensor at x=2968955, y=2961853: closest beacon is at x=2700669, y=3091664
Sensor at x=3069788, y=2289672: closest beacon is at x=3072064, y=2287523
Sensor at x=2206, y=1896380: closest beacon is at x=105942, y=2000000
Sensor at x=3010408, y=2580417: closest beacon is at x=2966207, y=2275132
Sensor at x=2511130, y=2230361: closest beacon is at x=2966207, y=2275132
Sensor at x=65435, y=2285654: closest beacon is at x=105942, y=2000000
Sensor at x=2811709, y=3379959: closest beacon is at x=2801189, y=3200444
Sensor at x=168413, y=3989039: closest beacon is at x=-631655, y=3592291
Sensor at x=165506, y=2154294: closest beacon is at x=105942, y=2000000
Sensor at x=2720578, y=3116882: closest beacon is at x=2700669, y=3091664
Sensor at x=786521, y=1485720: closest beacon is at x=105942, y=2000000
Sensor at x=82364, y=2011850: closest beacon is at x=105942, y=2000000
Sensor at x=2764729, y=3156203: closest beacon is at x=2801189, y=3200444
Sensor at x=1795379, y=1766882: closest beacon is at x=1616322, y=907350
Sensor at x=2708986, y=3105910: closest beacon is at x=2700669, y=3091664
Sensor at x=579597, y=439: closest beacon is at x=1616322, y=907350
Sensor at x=2671201, y=2736834: closest beacon is at x=2700669, y=3091664
Sensor at x=3901, y=2089464: closest beacon is at x=105942, y=2000000
Sensor at x=144449, y=813212: closest beacon is at x=105942, y=2000000
Sensor at x=3619265, y=3169784: closest beacon is at x=2801189, y=3200444
Sensor at x=2239333, y=3878605: closest beacon is at x=2801189, y=3200444
Sensor at x=2220630, y=2493371: closest beacon is at x=2966207, y=2275132
Sensor at x=1148022, y=403837: closest beacon is at x=1616322, y=907350
Sensor at x=996105, y=3077490: closest beacon is at x=2700669, y=3091664
Sensor at x=3763069, y=3875159: closest beacon is at x=2801189, y=3200444
Sensor at x=3994575, y=2268273: closest beacon is at x=3072064, y=2287523
Sensor at x=3025257, y=2244500: closest beacon is at x=2966207, y=2275132
Sensor at x=2721366, y=1657084: closest beacon is at x=2966207, y=2275132
Sensor at x=3783491, y=1332930: closest beacon is at x=3072064, y=2287523
Sensor at x=52706, y=2020407: closest beacon is at x=105942, y=2000000
Sensor at x=2543090, y=47584: closest beacon is at x=3450858, y=-772833
Sensor at x=3499766, y=2477193: closest beacon is at x=3072064, y=2287523`;

const _test = `Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3`;

function parse(input: string) {
	const lines = input.split("\n");
	const sensors = lines.map(line => {
		const matches = line.match(/x=(-?\d+), y=(-?\d+)/);
		if (!matches) {
			throw new Error(`Invalid input: ${line}`);
		}
		const [x, y] = matches.slice(1).map(Number);
		return { x, y };
	});
	const beacons = lines.map(line => {
		const matches = line.match(/closest beacon is at x=(-?\d+), y=(-?\d+)/);
		if (!matches) {
			throw new Error(`Invalid input: ${line}`);
		}
		const [x, y] = matches.slice(1).map(Number);
		return { x, y };
	});
	return sensors.map((sensor, i) => ({ sensor, beacon: beacons[i] }));
}

/**
 * How to check if a sensor provides coverage for a particular square?
 * Consider a square as an (x, y) coordinate.
 * We get the manhattan distance from the sensor to it's beacon and store that as the radius.
 * For any square we check if it's manhattan distance to the sensor is less than or equal to the radius.
 * Then it provides coverage.
 */

function row_coverage(input: string, y: number): number {
	const results = parse(input);

	const sensorsWithDistance = results.map(({ sensor, beacon }) => {
		const distance =
			Math.abs(sensor.y - beacon.y) + Math.abs(sensor.x - beacon.x);
		return { sensor, distance };
	});

	// the indices of the x axis that are covered
	const covered = new Set<number>();

	function spread(x: number, extra: number) {
		const reached = [x];
		while (extra > 0) {
			reached.push(x + extra);
			reached.push(x - extra);
			extra--;
		}
		return reached;
	}

	for (const source of sensorsWithDistance) {
		// const dir = sensorwithD.sensor.y > y ? -1 : 1;
		// if (sensorwithD.sensor.y + dir * sensorwithD.distance >= y) {
		// if we're above it
		if (source.sensor.y >= y) {
			// and going down with our distance puts us below it
			if (source.sensor.y - source.distance <= y) {
				// then for each extra tile we didn't need to go up once
				// we can explore in both directions in the x-axis
				const extra = y - (source.sensor.y - source.distance);
				const reached = spread(source.sensor.x, extra);
				reached.forEach(x => covered.add(x));
			}
		} else {
			if (source.sensor.y + source.distance >= y) {
				const extra = source.sensor.y + source.distance - y;
				const reached = spread(source.sensor.x, extra);
				reached.forEach(x => covered.add(x));
			}
		}
	}

	for (const result of results) {
		const beacon = result.beacon;
		if (beacon.y === y) {
			if (covered.has(beacon.x)) {
				covered.delete(beacon.x);
			}
		}
	}

	// console.log(Array.from(covered).sort((a, b) => a - b));

	return covered.size;
}

const numCovered = row_coverage(_test, 11);
console.log(numCovered);

// part 2

function findUncoveredSquare(input: string, lb = 0, ub = 4000000) {
	const results = parse(input);

	const sensorsWithDistance = results
		.map(({ sensor, beacon }) => {
			// L1 norm
			const distance =
				Math.abs(sensor.y - beacon.y) + Math.abs(sensor.x - beacon.x);
			return { sensor, distance };
		})
		.sort((s1, s2) => s1.sensor.y - s2.sensor.y);

	function leftover(y: number, sensors: typeof sensorsWithDistance) {
		const row = new Set<number>();
		for (let x = lb; x <= ub; x++) {
			row.add(x);
		}

		sensors.forEach(source => {
			const extra =
				source.sensor.y > y
					? y - (source.sensor.y - source.distance)
					: source.sensor.y + source.distance - y;

			for (
				let x = Math.max(source.sensor.x - extra, lb);
				x <= Math.min(source.sensor.x + extra, ub);
				x++
			) {
				row.delete(x);
			}
		});
		return row;
	}

	let sol: number[] = [];

	for (let y = lb; y <= ub; y++) {
		const sensed: typeof sensorsWithDistance = [];
		for (const source of sensorsWithDistance) {
			const extra =
				source.sensor.y > y
					? y - (source.sensor.y - source.distance)
					: source.sensor.y + source.distance - y;
			// if == 0 then reached will be [x]
			if (extra < 0) {
				continue;
			} else {
				sensed.push(source);
			}
		}

		const row = leftover(y, sensed);
		// major optimization
		/*
		 * Consider a subset of sensors that cover a row y.
		 * If they are all below that row, then it must be the case that
		 * they cover the next row since going towards the source of the sensor can only cover more tiles.
		 * In fact they will at least cover every row until they reach the row where
		 * at least one sensor in the subset can no longer reach.
		 */

		if (row.size < 1) {
			console.log(`row ${y} is covered`);
			const farthest = sensed.sort(
				(s1, s2) =>
					s1.sensor.y + s1.distance - (s2.sensor.y + s2.distance)
			)[0];

			y = Math.max(y, farthest.sensor.y + farthest.distance);
		} else {
			const x = Array.from(row)[0];
			sol = [x, y];
			console.log(sol);
			const tuning_freq = sol[0] * 4000000 + sol[1];
			return tuning_freq;
		}
	}
	// should not reach here
	return 0;
}

// const sol = findUncoveredSquare(_test, 0, 20);
const sol = findUncoveredSquare(input);
console.log(sol);
