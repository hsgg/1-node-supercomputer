#!/usr/bin/env julia

using Pkg
packages = [:LaTeXStrings, :LinearAlgebra, :StatsPlots]
Pkg.add(string.(packages))
for p in packages
    @eval using $p
end


μ = [0, 0]
C1 = [1 1; 1 1]
C11 = [1 1; 1 1.1]
C101 = [1 1; 1 1.01]
C1001 = [1 1; 1 1.001]

p = plot(xlabel=L"d_1", ylabel=L"d_2", aspect_ratio=1, dpi=300)
xlims!(-4.5, 4.5)
ylims!(-3, 3)

covellipse!(μ, C11, n_std=1, color=2, alpha=0.1, label="ϵ = 0.1")
covellipse!(μ, C11, n_std=2, color=2, alpha=0.1, label="")

covellipse!(μ, C1001, n_std=1, color=1, label="ϵ = 0.001")
covellipse!(μ, C1001, n_std=2, color=1, label="")

# covellipse!(μ, C2, n_std=1, color=2, label="ϵ = 0.001")
# covellipse!(μ, C2, n_std=2, color=2, label="")

root = @__DIR__
mkpath("$root")
savefig("$root/coveps.png")

xx = -10:10
plot!(xx, -xx.-2, fillrange=-xx.+2, color=3, alpha=0.2, label="Pseudo-Inverse")
plot!(xx, -xx.+2, alpha=0.2, color=3, label="")
plot!(xx, -xx.-4, fillrange=-xx.+4, color=3, alpha=0.2, label="")
plot!(xx, -xx.+4, alpha=0.2, color=3, label="")

savefig("$root/coveps_pinv.png")

display(p)
