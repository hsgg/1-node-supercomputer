# Dark Mode CSS

I like to switch my terminal colors between a dark theme and a light theme.
During the day I prefer the light theme, during the evening I prefer a dark
theme.

The same applies to websites. Wouldn't it be nice if the entire web
automatically switched between light and dark modes?

We are not there, yet. But, at least I just made my website work that way by
using the `prefer-color-scheme` `@media` CSS tag. I barely know anything about
HTML, but here is the code that made it work for me. I am posting it, because
by the time you read this, my stratgey may have changed, and just looking at
the source of the website may no longer work. So here we go:


    @media (prefers-color-scheme: light) {
        :root {
            background: white;
            color: #333;
            --readmorecolor: blue;
        }
        a:link {
            color: blue;
        }
        a:visited {
            color: purple;
        }
    }

    @media (prefers-color-scheme: dark) {
        :root {
            background: #333;
            color: white;
            --readmorecolor: #74a0ff; /* light blue */
        }
        a:link {
            color: #add8ff;  /* darker blue than lightblue */
        }
        a:visited {
            color: #b695c0;  /* a light purple */
        }
    }

Basically, we define the different colors for the same things in light and dark
modes. The `:root` element makes the background and text colors apply to
everything that doesn't otherwise have it set. Of course, there are things that
do have other colors set. For example,
[links](https://www.w3schools.com/html/html_links_colors.asp) need their colors
to be specified explicitly, and I needed to explicitly set the color of the
[Read More](blog-20200809-read-more-see-all.html) buttons.
