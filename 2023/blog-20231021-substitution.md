# No such thing as substitution in mathematics

Today I claim that in algebra the word _substitution_ is really a misnomer, coming from concentrating on the representation on paper rather than the meaning of a mathematical expression. A more accurate description would be to use the word "relabeling" instead of "substituting."

I got onto this train of thought as I was listening to the podcast [*Sold a Story*](https://features.apmreports.org/sold-a-story/) by Emily Hanford. In the podcast the narrator says that reading has been taught all wrong in school. Without going into the details of the podcast and whether it is right or not, I was thinking if something similar may be happening in Mathematics education. Is math hard because it is taught wrong? Maybe. The words "solve by subtitution" have always bothered me, as soon as I heard them uttered in the halls of the UC Davis campus $\sim20$ years ago, and I think I now know why.

## An Example

Take the set of equations

$$
\begin{align*}
x &= 10 + y \,,\\
y &= 6\,.
\end{align*}
$$

Usually, one would say that in order to calculate $x$, you should *substitute* the value for $y$ into the first equation. That is, you erase the $y$ and write $6$ in its place. Such is the operation performed. Thus, you get $x=10+6=16$.

In this description little is said of why this works or why this is the correct procedure to follow. Indeed, all it does is give you a rule, with no understanding needed. It is a procedure operating purely on the syntax level of the expressions as written on paper.

Indeed, this operational description makes it seem like $y$ and $6$ may actually be different things.

## Substitution only works because of Equality

However, within the context of this example problem, the second equation tells us that $y$ and $6$ are equal. They refer to the same mathematical object, the number six. Thus, the substitution is not substituting what is in the equation. Rather, it merely changes the label for the underlying mathematical object.

That is, on the *semantic* level there is no substitution happening, and a more accurate term would be "relabeling" or "renaming". Indeed, the substitution procedure works precisely *because* there is no substitution happening on the semantic level, only on the syntactic level.

Thus, when applying the "solve-by-substitution" technique, you are not actually substituting anything other than some labels.

## Substitution is Approximation

OK, maybe there is substitution. Namely, when doing approximations. Consider the case when $y=6.001$. However, we may not care that $y$ isn't exactly $6$; it may be close enough for our purposes. Then, we may say

$$
y \approx 6\,.
$$

That is, we explicitly express that, within the current context, *substituting* the number $6$ for $y$ is sufficient.

Perhaps a philosophical difficulty could arise if $y$ is some small $\epsilon$ away from $6$, or $y=6+\epsilon$. As we take the limit $\epsilon\to0$, can we ever say we don't substitute?
