require 'prime'

def largest_prime_factor(n)
  raise ArgumentError unless n.is_a? Integer and n > 1
  # get the largest prime that evenly divides n
  Prime.each((n**0.5) + 1).select{ |x| n % x == 0 }.max
end

puts largest_prime_factor(600851475143)
