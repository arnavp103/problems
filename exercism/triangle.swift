class Triangle<T: Numeric & Comparable> {
    public let isEquilateral: Bool
    public let isIsosceles: Bool
    public let isScalene: Bool

	init(_ abc: [T]) {
		let (a, b, c) = (abc[0], abc[1], abc[2])

		// if invalid size or fails triangle inequality
		if (a <= 0 && b <= 0 && c <= 0) ||
			(a + b <= c) ||
			(a + c <= b) ||
			(b + c <= a) {
			isEquilateral = false
			isIsosceles = false
			isScalene = false
			return
		}

		if a == b && b == c {
			isEquilateral = true
			isIsosceles = true
		} else if a == b || b == c || a == c {
			isIsosceles = true
		} else {
			isScalene = true
		}
	}

}
