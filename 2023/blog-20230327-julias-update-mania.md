# Julia's Update-Mania

By default [JuliaLang](julialang.org) updates its registry on every opportunity
it gets, for example when you `]add` or `]rm` a package.

This is especially annoying when you have packages like
`DifferentialEquations.jl` that update frequently and take a long time to
compile. Removing `DifferentialEquations.jl` is not an option because it is a
great package, and I want to use it.

Thus, just to do a few package operations can take a very long time, where
"very long" means about 2-5 minutes per operation. That is too much. It is a
brake that is unacceptably long and generates a lot of frustration.

Of course, Julia doesn't quite upate every single time. Once in a session, it
generally doesn't update again. This is because of the
`Pkg.UPDATED_REGISTRY_THIS_SESSION` variable. And herein lies the solution: Set
that variable on every startup of Julia, in the file
`~/.julia/config/startup.jl`:

    using Pkg: Pkg
    Pkg.UPDATED_REGISTRY_THIS_SESSION[] = true

And, voila, no more update-mania.

Updating now needs to be done explicitly with `]up`.
