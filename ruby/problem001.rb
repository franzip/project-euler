def mulsum_3_5(limit)
  (2...limit).select{ |n| n % 5 == 0 || n % 3 == 0 }.reduce(:+)
end

puts mulsum_3_5(1000)