dial = 50
modulo = 99
count = 0
filename = "input.txt"

array = File.read(filename).split

array.each do |line|
  direction = line[0]
  distance = line[1..-1].to_i
  complete_loops = distance / 100
  count += complete_loops
  partial_distance = distance % 100
  
  case direction
  when 'R'
    count += 1 if (dial + partial_distance) >= 100
    dial = (dial + distance) % 100
  when 'L'
    count += 1 if partial_distance >= dial && dial  != 0
    dial = (dial - distance) % 100
  end
end
puts count
