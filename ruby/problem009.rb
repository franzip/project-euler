def pythagorean_triplet(triplet_sum)
  raise ArgumentError unless triplet_sum.is_a? Fixnum and triplet_sum > 0
  # (a + b + c) / 2 is always larger than max(a, b, c)
  pool = (1..triplet_sum / 2).to_a
  # check every (a, b) combination
  pool.combination(2).to_a.each do |x|
    # get c from (a, b)
    c = (x[0]**2 - x[1]**2).abs**0.5
    if x[0] + x[1] + c == triplet_sum
      return "#{x[0]} + #{c.to_i} + #{x[1]} = #{triplet_sum}"
    end
  end
  "There is no triplet (a + b + c) = #{triplet_sum}"
end

puts pythagorean_triplet(1000)