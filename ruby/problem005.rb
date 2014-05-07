def smallest_multiple(to_n)
  raise ArgumentError unless to_n.is_a? Fixnum and to_n > 0
  result = 1
  # smallest multiple in range(1..to_n) is just lcm(1..to_n)
  (1..to_n).each { |x| result = x.lcm(result) } 
  result
end

puts smallest_multiple(20)
