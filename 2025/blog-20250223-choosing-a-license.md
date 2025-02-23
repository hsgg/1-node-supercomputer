# Choosing a license for open source

There are several common licenses to choose out there. Here I will list what I
am looking for in a license for an open source project, and which ones are out
there.

Basically, I want the following for the projects I am currently thinking about:

 1. License popularity: If you choose a different license from everyone
    else, you will make a lot of people
    [grouchy](https://discourse.julialang.org/t/package-license/7109/4) and
    annoyed. This is because different licenses will make it just that
    little bit harder to share and change. For one, contributors will need
    to become familiar with the new license.

 2. Unrestricted usage: I want to allow the software to be used in any way
    people see fit. I don't want to limit how it is used, and I don't want
    to impose a license on their work either.

 3. Reciprocity: If you take my code and modify it, I want to be able to
    merge those modifications back.

 4. Patent protection and limited liability: I don't want be held liable for
    anything, and both parties are protected from patent claims from each
    other.

 5. Simplicity: I want it in one not-too-long file, readable in one sitting.

Other people and other projects may have different requirements. For example,
Stefan Karpinski [made a good
point](https://discourse.julialang.org/t/package-license/7109/15) that
infrastructure-like software can get away with a more permissive license than
an end-user product intended to be sold.

The kinds of projects I am thinking about fall somewhere in-between. I don't
expect the number of users to be very large, ever, so I am not concerned about
monetization. On the other hand, I think it is far enough along the toolchain
to warrant reciprocity. That is, that modifications can always be merged back.

Reciprocity is also a matter of fairness. I share my code, and if someone else
benefits from it makes modifications that I could benefit from as well, then I
want those back. You taketh, you giveth.

The rest of the points above are really just practical considerations.

The licenses I am considering are the following, roughly
[sorted](https://choosealicense.com/licenses/) by how restrictive they are:

 1. GPL: GNU General Public License
 3. LGPL: GNU Lesse General Public License
 4. MPL: Mozilla Public License Version 2.0
 5. EUPL: European Public License Version 1.2
 6. Apache: Apache License Version 2.0
 7. MIT License
 8. BSD License

Another good site for comparison is the [License
Assistant](https://joinup.ec.europa.eu/collection/eupl/joinup-licensing-assistant-jla).

First, let's start throwing out licenses: The GPL is too viral. It imposes on
programs using GPL'd code that they also need to be GPL. That seems a little
too much imposing for my projects.

Next, BSD is very similar to MIT, but the Julia ecosystem is mostly on MIT, so
no reason to choose BSD for me. The ecosystem argument is a strong one, so MIT
is still in the running, but it lacks reciprocity, so I prefer not to.

Similarly, the Apache license is stronger than MIT, but also lacks reciprocity.

So I am left with LGPL, MPL, and EUPL. (And maybbe GPLv2-only, but I don't want
to open that hornest's nest.)

The LGPL is a mess. I am not even sure if there is a single document for it.
Otherwise, I probably would consider it.

We are left with MPL and EUPL. The EUPL appears to be a little more annoying to
deal with, requiring to be explicit about what changes someone else made. But
probably a good license.

The MPL seems to fit my purpose quite nicely. It is relatively short, appears
to be legally robust by not leaving too much open for interpretation, has all
the protections in it, and ensures reciprocity. What's not to like?

So with the [MPL](https://www.mozilla.org/en-US/MPL/), people can use the
software as they see fit, and modifications need to be under the same license.

Also, sometimes I am a big fan of oversimplification:
[MPL/EUPL = MIT + more robust legalese + reciprocity +
credit](https://discourse.julialang.org/t/package-licenses-contemplations-and-considerations/117922/9).
