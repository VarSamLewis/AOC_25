dial = 50
modulo = 99
count = 0
filename = "input.txt"

array = File.read(filename).split

array.each do |line|

  direction = line[0]
  distance = line[1..-1].to_i

  case direction
  when 'R'
    dial = (dial + distance) % 100
  when 'L'
   dial = (dial - distance) % 100
  end

  count += 1 if dial == 0
end

puts count
