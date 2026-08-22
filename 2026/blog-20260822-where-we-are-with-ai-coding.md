# Where we are with LLM coding agents

In this post I do not want to ask the question of what the future of coding
looks like. I want to ask what at present we still need to do when coding, even
if some of that will go away as LLMs continue to get better.

It is clear that the technology is here to stay. However, it is not clear what
level will continue to be available and what dependency on a big LLM provider
will remain tolerable in the future. The level of tolerance is one everyone
will have to answer themselves. Local is often better, as for example
distributed version control systems allow you to get more work done when your
internet connect sucks. So being dependant on an LLM provider over the internet
has its disadvantanges. No need to go to political or environmental doom
scenarios. On the other hand, maybe that is what you are concerned about. I
certainly am. Up to you.

Much of this was written in mind with writing and maintaining Julia packages. I
don't think we are at a stage where we can abandon dividing our code bases into
packages, yet. The modularity and abstractions make it possible to check that
the LLM is doing the right thing. And LLMs, too, benefit from good
abstractions. Whether this will remain true is the subject of another debate.

The kind of code I am talking about is also code where we need to ensure it
does the right thing, e.g., scientific codes. There certainly are scenarios
where we don't care that much about the correctness of code.

That means not everything of the LLM output needs to be checked in detail.

I believe we currently need to operate at the following level when using coding
agens:

1. We need to check and understand the tests.
2. We need to check and understand the interfaces and APIs.
3. We do not need to understand every implementation detail.

Number 1 is kind of obvious: we need some way to check that the output is
actually what we want, and tests can play a major role not just in enforcing
that the code continues to do what we want, but also to decide what the right
thing is. However, some details of tests may some day be uninteresting, e.g.,
testing edge cases like whether sin(NaN) = NaN or some such thing.

Number 2 may change in the future. However, at present, in summer 2026, I don't
think we can get away without checking a lot of the interfaces. Sure, LLMs are
very good at dealing with crappy interfaces. However, letting the interface
drift means no going back, and LLMs are just not good enough, yet, to design
phantastic interfaces.

Number 3 is the big change: LLMs are great at optimizing code. We want to make
use of that ability. However, it is not reasonable to clean the code up or
spend that much time understanding how exactly it all works in detail. LLMs are
now good enough that we don't need to do that anymore. Of course, that puts
more emphasis on tests, and it requires better tests.

This what I am currently operating under. LLMs have been great to clean up some
loose ends in Julia packages I've had. But the next stage needs to unlock more
of their potential without overloading the humans.

My view is that as we develop and adapt to this new capability, we need to be
very careful how we change the way we work. We cannot, yet, code like we will
in the future, but we still want to be able to use this phantastic technology.
