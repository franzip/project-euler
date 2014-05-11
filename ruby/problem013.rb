require 'net/http'

def large_sum(n_digits)
	uri = URI.parse("http://projecteuler.net/problem=13")
  html = Net::HTTP.get(uri)
  data = /(^[\d]+<br \/>\n)+/.match(html)[0]
  data = data.lines.each do |x|
  	x.gsub(/<br \/>|\n/, '')
  end
  # convert to int, sum and convert back to string
  data.collect!{ |x| x.to_i }.reduce(:+).to_s[0...n_digits]

end

puts large_sum(10)