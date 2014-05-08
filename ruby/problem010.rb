require 'prime'

def sum_prime_until(limit)
  raise ArgumentError unless limit.is_a? Fixnum and limit > 1
  result, start = 0, 2
  while start <= limit
    result += start if Prime.prime? start 
    start += 1
  end
  result
end

puts sum_prime_until(2_000_000)