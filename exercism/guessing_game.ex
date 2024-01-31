# When the guess matches the secret number 	                    "Correct"
# When the guess is one more or one less than the secret number "So close"
# When the guess is greater than the secret number 	            "Too high"
# When the guess is less than the secret number 	              "Too low"
# When a guess isn't made 	                                    "Make a guess"

defmodule GuessingGame do
  def compare(secret_number, guess \\ :no_guess)

  def compare(secret_number, guess) do
    cond do
      guess == :no_guess -> "Make a guess"
      secret_number == guess -> "Correct"
      secret_number == guess + 1 || secret_number == guess - 1 -> "So close"
      guess > secret_number -> "Too high"
      guess < secret_number -> "Too low"
      true -> "Unknown"
    end
  end
end
