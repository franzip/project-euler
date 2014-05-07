def sum_square_diff(to_n)
  raise ArgumentError unless to_n.is_a? Fixnum and to_n > 0
  # (1 + 2 + ... + to_n)**2 - (1**2 + 2**2 + ... + to_n**2)
  (1..to_n).reduce(:+)**2 - (1..to_n).map { |x| x**2 }.reduce(:+)
end

puts sum_square_diff(100)
