function pigIt(str) {
	return str
		.split(" ")
		.map(w => (isPunctuation(w) ? w : pigWord(w)))
		.join(" ");
}

// for example
// this : 'O tempora o mores !'
// becomes: 'Oay emporatay oay oresmay !'

function isPunctuation(word) {
	return word.match(/[.,:!?]/g);
}

function pigWord(word) {
	return word.slice(1) + word[0] + "ay";
}

console.log(pigIt("O tempora o mores !"));
