require 'prime'

def nth_prime(n)
	raise ArgumentError unless n.is_a? Fixnum and n > 0
	Prime.first(n)[-1] 
end

puts nth_prime(10_001)