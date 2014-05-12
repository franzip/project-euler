def digit_sum(n)
	raise ArgumentError unless n.is_a? Integer and n > 0
	n.to_s.split("").map{ |x| x.to_i }.reduce(:+)
end

p digit_sum(2**1000)

