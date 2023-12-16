function digital_root(n) {
	let temp = String(n)
		.split("")
		.map(Number)
		.reduce((a, b) => a + b);
	return String(temp).length === 1 ? temp : digital_root(temp);
}
