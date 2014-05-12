def get_length(n, memo)
  # use caching
  return memo[n] unless memo[n].nil?
  return 1 + get_length(3 * n + 1, memo) if n % 2 == 1
  return 1 + get_length(n / 2, memo) 
end

def collatz_dict(up_to, memo)
  # return a dictionary with collatz sequence length
  (1..up_to).each do |x|
    val = get_length(x, memo)
    memo[x] = val
  end
  memo
end

def longest_collatz(up_to)
  # get the max length and return its key
  result = collatz_dict(up_to, {1 => 1})
  result.key(result.values.max)
end

puts longest_collatz(1_000_000)
