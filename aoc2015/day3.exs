# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

#     > delivers presents to 2 houses: one at the starting location, and one to the east.
#     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

defmodule Solution do
  def part1(input) do
    input
    |> String.graphemes()
    |> Enum.reduce(
      [{0, 0}],
      fn direction, acc ->
        {x, y} = List.first(acc)

        case direction do
          "^" -> [{x, y + 1} | acc]
          "v" -> [{x, y - 1} | acc]
          ">" -> [{x + 1, y} | acc]
          "<" -> [{x - 1, y} | acc]
        end
      end
    )
    |> Enum.uniq()
    |> Enum.count()
  end

  def part2(input) do
    {santa, robot, _} =
      input
      |> String.graphemes()
      # reached-santa, reached-robot, is-santa's-turn
      |> Enum.reduce(
        {[{0, 0}], [{0, 0}], true},
        fn direction, {santa, robot, is_santa_turn} ->
          {x, y} = if is_santa_turn, do: List.first(santa), else: List.first(robot)

          new_coords =
            case direction do
              "^" -> {x, y + 1}
              "v" -> {x, y - 1}
              ">" -> {x + 1, y}
              "<" -> {x - 1, y}
            end

          if is_santa_turn do
            {[new_coords | santa], robot, not is_santa_turn}
          else
            {santa, [new_coords | robot], not is_santa_turn}
          end
        end
      )

    (santa ++ robot)
    |> Enum.uniq()
    |> Enum.count()
  end

  def main do
    input = File.read!("day3_input.txt")
    IO.puts("Part 1: #{part1(input)}")
    IO.puts("Part 2: #{part2(input)}")
  end
end

Solution.main()
