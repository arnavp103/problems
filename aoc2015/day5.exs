# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
#
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?

# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

defmodule Solution do
  def contains_forbidden_substrings?(string) do
    String.contains?(string, "ab") ||
      String.contains?(string, "cd") ||
      String.contains?(string, "pq") ||
      String.contains?(string, "xy")
  end

  def contains_three_vowels?(string) do
    String.split(string, "", trim: true)
    |> Enum.reduce(
      0,
      fn x, acc ->
        if x in ["a", "e", "i", "o", "u"] do
          acc + 1
        else
          acc
        end
      end
    ) >= 3
  end

  def contains_double_letter?(string) do
    String.split(string, "", trim: true)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.any?(fn [x, y] -> x == y end)
  end

  def part1(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn x ->
      !contains_forbidden_substrings?(x) &&
        contains_three_vowels?(x) &&
        contains_double_letter?(x)
    end)
    |> Enum.count()
  end

  # Part 2

  def contains_pair_of_two_letters?(string) do
    # need to count how many times we've seen each pair
    String.split(string, "", trim: true)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.reduce(
      {%{}, 0},
      fn [x, y], {map, index} ->
        new_map =
          Map.update(
            map,
            {x, y},
            {1, index},
            fn {count, pos} ->
              if index - pos > 1, do: {count + 1, index}, else: {count, pos}
            end
          )

        {new_map, index + 1}
      end
    )
    |> elem(0)
    |> Enum.any?(fn {_, {count, _}} -> count > 1 end)
  end

  def contains_repeating_letter_with_one_between?(string) do
    String.split(string, "", trim: true)
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.any?(fn [x, _, y] -> x == y end)
  end

  def part2(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn x ->
      contains_pair_of_two_letters?(x) &&
        contains_repeating_letter_with_one_between?(x)
    end)
    |> Enum.count()
  end

  def main do
    input = File.read!("day5_input.txt") |> String.trim_trailing()

    IO.puts("Part 1: #{part1(input)}")
    IO.puts("Part 2: #{part2(input)}")
  end
end

Solution.main()
