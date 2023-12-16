function moveZeros(arr) {
	return arr.filter(x => x !== 0).concat(arr.filter(x => x === 0));
}
