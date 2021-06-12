# `none` vs `nearest` in Matplotlib's imshow()

To get a visual display of the entries of a matrix, I often use
[Matplotlib's](https://matplotlib.org/)
[`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)
function. However, by default that function does bilinear interpolation in
order to smooth the values between the centers of the pixels. That makes it
virtually useless for analysing the elements of a matrix.

Therefore, I have been passing to `imshow()` the parameter
`interpolation='none'`. This led to a mysterious bug, where I would save the
image in PDF format, then include in a LaTeX document and compile directly to
PDF using `latexmk -pdf myfile.tex`. The bug would manifest itself when
displaying the PDF at *some* lower resolutions it would blur the image and do
some kind of interpolation or antialiasing between the pixel centers again. But
not at all lower resolutions, which is why it had escaped me before.

Clearly, this can be done better? Yes!

Pass `interpolation='nearest'` instead. That solves the bug, at least as well
as I can expect. Why does this work? No idea. I guess it somehow turns off that
antialiasing. In any case, remember to use `'nearest'`
instead of `'none'`.
