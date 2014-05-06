def mulsum_3_5(limit)
  raise ArgumentError unless limit.is_a? Fixnum and limit > 3
  (2...limit).select{ |n| n % 5 == 0 || n % 3 == 0 }.reduce(:+)
end

puts mulsum_3_5(1000)