def is_palindrome?(s)
	s == s.reverse
end

def largest_palindrome(digits)
	raise ArgumentError unless digits.is_a? Fixnum and digits > 0
	# set up and low bounds
	up = (10**digits) - 1
	low = up - (up / 10) + 1
  # loop from top to bottom and return on the first palindrome
  up.downto(low) do |x|
    up.downto(low) do |y|
      return (x * y) if is_palindrome? (x * y).to_s
    end
  end
end

puts largest_palindrome(3)

