def fib_gen(limit)
	# lazy fibonacci generator
  Enumerator.new do |fib|
  	x, y = 0, 1
  	while x < limit
 			x, y = y, x + y	
 			fib.yield x
  	end
  end
end

def even_fib(upper_bound)
	raise ArgumentError unless upper_bound.is_a? Fixnum and upper_bound > 1
	# only catch even fibs in range
	fib_gen(upper_bound).select { |x| x % 2 == 0 }.reduce(:+)
end

puts even_fib(4_000_000) 