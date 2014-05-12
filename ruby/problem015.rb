def lattice_paths(n)
  raise ArgumentError unless n.is_a? Fixnum and n > 0
  def fact(n)
    (1..n).inject(:*)
  end
  fact(2 * n) / fact(n)**2
end

p lattice_paths(20)
