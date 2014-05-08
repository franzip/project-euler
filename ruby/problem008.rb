require 'net/http'

def largest_prod()
  uri = URI.parse("http://projecteuler.net/problem=8")
  html = Net::HTTP.get(uri)
  res = 0
  # match the digits
  data = /(^[\d]+<br \/>\n)+/.match(html)[0]
  # strip html from the string
  data = data.gsub(/<br \/>|\n/, '').chars.map { |x| x.to_i }
  # check all products
  (0..data.length - 5).each do |x|
    prod = (x..x+4).map { |y| data[y] }.reduce(:*)
    res = prod if prod > res
  end
  res 
end

puts largest_prod()