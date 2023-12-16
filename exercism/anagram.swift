class Anagram {
	var word: String

	init(word: String) {
		self.word = word
	}

	func match(_ candidates: [String]) -> [String] {
		let word = self.word.lowercased()
		// a word is not an anagram of itself
		let result = candidates.filter { $0.lowercased() != word  && $0.lowercased().sorted() == word.sorted() }

		return result
	}
}