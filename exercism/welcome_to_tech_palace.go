package exercism

// needed to stop the compiler from complaining about having c in the same directory
import (
	"C"
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	return "Welcome to the Tech Palace, " + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	return strings.Repeat("*", numStarsPerLine) + "\n" + welcomeMsg + "\n" + strings.Repeat("*", numStarsPerLine)
}

// message := `
// **************************
// *    BUY NOW, SAVE 10%   *
// **************************
// `

// CleanUpMessage(message)
// // => BUY NOW, SAVE 10%

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	middle := strings.Split(oldMsg, "\n")[1]
	return strings.Trim(middle, " *")
}
