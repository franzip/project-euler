def triangular_n
	# triangular number generator
	Enumerator.new do |triang|
		x, iter_next = 0, 1
		loop do
			x += iter_next
			iter_next += 1
			triang.yield x 
		end
	end
end

def count_divisors(n)
	factors, bound = [1, n], (n**0.5).ceil + 1
	(2..bound).each do |x|
		if n % x == 0
			factors << n
			factors << n / x
		end
	end
	factors.uniq.count
end

def first_triangular(n_divisors)
	raise ArgumentError unless n_divisors.is_a? Fixnum and n_divisors > 0
	triangular_n.detect {|x| count_divisors(x) == n_divisors}
end

p first_triangular(500)