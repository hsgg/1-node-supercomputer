# reduce(op,arr)

I was trying to explain the concept of the function
[`reduce(op,arr)`](https://docs.julialang.org/en/v1/base/collections/#Base.reduce-Tuple{Any,%20Any})
that takes an array `arr` and reduces it pairwise using the binary operator
`op` until just one number is left.

For example, the `sum()` function can then be written

	sum(arr) = reduce(+, arr)

To explain what `reduce()` does, I thought it would be nice to have a great
graph, but I couldn't find one online.

Thus, I attempted to make one myself using
[Ti*k*Z](https://github.com/pgf-tikz/pgf). I failed:

[![reduce](mapreduce/mapreduce.svg "reduce(op,arr)")](mapreduce/mapreduce.tex)
