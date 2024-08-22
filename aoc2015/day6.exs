# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

#     turn on 0,0 through 999,999 would turn on (or leave on) every light.
#     toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#     turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

defmodule Solution do
  defp parse_coordinates(coordinates) do
    [y, x] = String.split(coordinates, ",")

    {String.to_integer(y), String.to_integer(x)}
  end

  defp parse_instruction(instruction) do
    case String.split(instruction, " ") do
      ["turn", "on", from, "through", to] ->
        {:turn_on, parse_coordinates(from), parse_coordinates(to)}

      ["turn", "off", from, "through", to] ->
        {:turn_off, parse_coordinates(from), parse_coordinates(to)}

      ["toggle", from, "through", to] ->
        {:toggle, parse_coordinates(from), parse_coordinates(to)}
    end
  end

  defp turn_on(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          1
        else
          light
        end
      end)
    end)
  end

  defp turn_off(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          0
        else
          light
        end
      end)
    end)
  end

  defp toggle(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          if light == 0 do
            1
          else
            0
          end
        else
          light
        end
      end)
    end)
  end

  def part1(input, size) do
    grid =
      for _ <- 1..size do
        Enum.map(1..size, fn _ -> 0 end)
      end

    input
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_instruction/1)
    |> Enum.reduce(
      grid,
      fn {case, from, to}, grid ->
        case case do
          :turn_on -> turn_on(grid, from, to)
          :turn_off -> turn_off(grid, from, to)
          :toggle -> toggle(grid, from, to)
        end
      end
    )
    |> Enum.filter(fn row -> Enum.filter(row, &(&1 == 1)) end)
    |> Enum.map(fn row -> Enum.sum(row) end)
    # |> dbg()
    |> Enum.sum()
  end

  defp turn_on_2(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          light + 1
        else
          light
        end
      end)
    end)
  end

  defp turn_off_2(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          if light > 0 do
            light - 1
          else
            0
          end
        else
          light
        end
      end)
    end)
  end

  defp toggle_2(grid, from, to) do
    {from_y, from_x} = from
    {to_y, to_x} = to

    grid
    |> Enum.with_index()
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index()
      |> Enum.map(fn {light, x} ->
        if x >= from_x && x <= to_x && y >= from_y && y <= to_y do
          light + 2
        else
          light
        end
      end)
    end)
  end

  def part2(input, size) do
    grid =
      for _ <- 1..size do
        Enum.map(1..size, fn _ -> 0 end)
      end

    input
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_instruction/1)
    |> Enum.reduce(
      grid,
      fn {case, from, to}, grid ->
        case case do
          :turn_on -> turn_on_2(grid, from, to)
          :turn_off -> turn_off_2(grid, from, to)
          :toggle -> toggle_2(grid, from, to)
        end
      end
    )
    |> Enum.map(fn row -> Enum.sum(row) end)
    |> Enum.sum()
  end

  def main do
    input = File.read!("day6_input.txt") |> String.trim_trailing()
    size = 1000
    IO.puts("Part 1: #{part1(input, size)}")
    IO.puts("Part 2: #{part2(input, size)}")
  end
end

Solution.main()
