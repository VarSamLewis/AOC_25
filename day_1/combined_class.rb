class DialCounter
  Command = Struct.new(:direction, :distance)

  def initialize(filename, starting_dial = 50)
    @commands = File.read(filename).split.map { |line|
      Command.new(line[0], line[1..-1].to_i)
    }
    @starting_dial = starting_dial
  end

  def part1
    dial = @starting_dial
    count = 0

    @commands.each do |cmd|
      dial = case cmd.direction
             when 'R' then (dial + cmd.distance) % 100
             when 'L' then (dial - cmd.distance) % 100
             else dial
             end

      count += 1 if dial.zero?
    end

    count
  end

  def part2
    dial = @starting_dial
    count = 0

    @commands.each do |cmd|
      # Count complete loops
      complete_loops = cmd.distance / 100
      count += complete_loops
      partial_distance = cmd.distance % 100

      case cmd.direction
      when 'R'
        count += 1 if (dial + partial_distance) >= 100
        dial = (dial + cmd.distance) % 100
      when 'L'
        count += 1 if partial_distance >= dial && !dial.zero?
        dial = (dial - cmd.distance) % 100
      end
    end

    count
  end
end

# Usage:
counter = DialCounter.new("input.txt")
puts "Part 1: #{counter.part1}"
puts "Part 2: #{counter.part2}"
