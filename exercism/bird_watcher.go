package exercism

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	total := 0
	for _, bird := range birdsPerDay {
		total += bird
	}
	return total
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	total := 0
	start := (week - 1) * 7
	end := week * 7
	for i := start; i < end; i++ {
		total += birdsPerDay[i]
	}
	return total
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i += 2 {
		birdsPerDay[i] += 1
	}
	return birdsPerDay
}


//

package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, time int) int {
	if time == 0 {
		time = 2
	}
	return len(layers) * time
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	noodles := 0
	sauce := 0.0
	for _, layer := range layers {
		switch layer {
		case "noodles":
			noodles += 50
		case "sauce":
			sauce += 0.2
		}
	}
	return noodles, sauce
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList []string, myList []string) []string {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
	return myList
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, factor int) []float64 {
	multiple := float64(factor) / 2.0
	newQuantities := make([]float64, len(quantities))
	for i := range quantities {
		newQuantities[i] = quantities[i] * multiple
	}
	return newQuantities
}

//

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	value := 0
	switch card {
		case "ace":
			value = 11
		case "king", "queen", "jack":
			value = 10
		case "ten":
			value = 10
		case "nine":
			value = 9
		case "eight":
			value = 8
		case "seven":
			value = 7
		case "six":
			value = 6
		case "five":
			value = 5
		case "four":
			value = 4
		case "three":
			value = 3
		case "two":
			value = 2
		case "one":
			value = 1
	}
	return value
}


// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	move := "S"
	if card1 == card2 && card1 == "ace" {
		return "P"
	}

	value := ParseCard(card1) + ParseCard(card2)

	if value == 21 && dealerCard != "ace" && dealerCard != "king" && dealerCard != "queen" && dealerCard != "jack" && dealerCard != "10" {
		return "W"
	}
	if value >= 17 && value <= 20 {
		move = "S"
	}
	if value >= 12 && value <= 16 && ParseCard(dealerCard) >= 7 {
		move = "H"
	}
	if value <= 11 {
		move = "H"
	}
	return move
}
