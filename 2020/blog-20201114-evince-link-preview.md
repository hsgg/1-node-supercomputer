# Evince 3.38 has Link Previews!

Evince is a document viewer. I primarily use it to view PDF documents as most
of the papers I read and write are disseminated as PDFs.

Starting with version 3.38 Evince shows a preview of a link when you hover over
it with the mouse.

The kinds of papers I read tend to have lots of equations and figures in them.
It is very typical to give equations a number and then reference the equation
later in the text, and this reference is often a hyperlink to the original
equation in the PDF.

So, if this reference is, say, to Eq. (42), maybe you remember what Eq. (42)
was? I, however, don't. To see it, I would have to click the link to jump to
the page with the equation. Then, find the place where you where right before
jumping to the equation (where was that again?), perhaps do some scroll-mania
until you find it. Finally, you can continue reading the paper. What was Eq.
(42), again?

Clearly, this situation was suboptimal.

Enter link previews. With a link preview, you hover over the link, and a popup
shows the contents of the PDF at the link location. Boom, no more scolling all
over the place and getting lost in the document while your eyes get dizzy
spinning.

So Evince added those previews. I should show pictures or even a video to
demonstrate. Instead, I'm going to point you to the commits:
[first](https://gitlab.gnome.org/GNOME/evince/-/commit/6fa47bc006b5847122e29163f38ee43d315863cd),
[second](https://gitlab.gnome.org/GNOME/evince/-/commit/f95c24b96de0024f5888e1b11f787ad1432e2263),
[third](https://gitlab.gnome.org/GNOME/evince/-/commit/c73b2f5ae01908d813bc04f15bfe51c3f7708004),
[fourth](https://gitlab.gnome.org/GNOME/evince/-/commit/cf569bd229a74073d1d69a87ba2f06100d83954c),
and
[fifth](https://gitlab.gnome.org/GNOME/evince/-/commit/727657a4e13fd00bbb5bd35c1c19e80723a8bbb0).

Here, I want to justify the choice of layout, which was my contribution.

First, horizontally, we display the full width of the destination page in the
popup. This is needed to make the preview useful for two-column papers.
Unfortunately, the links in a PDF don't contain enough information to select
the correct column, so we have to show both, if possible.

Vertically, we limit the height of the popup to maximally one third of the main
view. That way the popup will not dominate the view, and the reader can see
context both in the popup and the main page.

Next, what to show in the popup? We have to deal with a limitation of links in
PDF files. The link only contains a (x,y) position, nothing else. And different
types of links have the main content either above, below, left, or right of
that (x,y) position.

Specifically, section headers, bibliographic references, footnotes, and tables
tend to have the link point to the top left of their main content. Equations,
on the other hand, tend to have the link point to the center right or bottom
right of the equation, and figures usually have a link to the top left of the
caption that is below the actual figure.

Therefore, we choose the link destination to be centered horizontally, and
slightly above the center vertically. That way, whether the link points left or
right of the content, we don't discriminate. Vertically, this allows seeing
most equations in full and for figures seeing just the bottom of the actual
figure is often enough to remind the reader of the full figure.

One more thing to note is that we do not zoom out. That would make the
equations in the preview too small to read, therefore defeating the purpose of
having a link preview. Just keep it at the regular zoom level.

All in all, I am super happy about the outcome. Special thanks to Mads Chr.
Olesen for the original patch and the Evince maintainer Germán Poo-Caamaño for
giving feedback and helping us out!
