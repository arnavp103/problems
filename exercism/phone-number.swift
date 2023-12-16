class PhoneNumber {
	var number: String

	init(_ number: String) {
		self.number = number
	}

	func clean() throws -> String {
		var cleanNumber = self.number.filter { $0.isNumber }
		if cleanNumber.count == 11 && cleanNumber.first == "1" {
			cleanNumber.removeFirst()
		}
		if cleanNumber.count != 10 ||
		(cleanNumber[cleanNumber.startIndex].wholeNumberValue ?? 0) < 2  ||
		(cleanNumber[cleanNumber.index(cleanNumber.startIndex, offsetBy: 3)].wholeNumberValue ?? 0) < 2 {
			throw PhoneNumberError.invalidPhoneNumber
		}
		return cleanNumber
	}
}

enum PhoneNumberError: Error {
	case invalidPhoneNumber
}

// For example, the inputs
//     +1 (613)-995-0253
//     613-995-0253
//     1 613 995 0253
//     613.995.0253
// should all produce the output
// 6139950253