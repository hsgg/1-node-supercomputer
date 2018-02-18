#!/usr/bin/env julia


module Shue

using PyPlot

function main()
    x = 0:0.01:2pi
    y = sin.(x)
    plot(y,x)

    x = -0.8:0.01:0
    y = - 8x
    plot(x+2, y+0.5)
    x = -0.31:0.01:0.5
    y = 3.5 - 10x.^2
    plot(x+2, y+0.5)

    x = -0.5:0.01:0.5
    y = 10x.^2
    plot(x+4,y+1.5)

    t = 0.7:0.01:6
    x = sin.(t) + 0.4t
    y = - 0.2t .* cos.(t)
    plot(x+4.5,y+3.5)

    xlabel("Time")
    ylabel("Importance")

    savefig("shue.png")
end

end

Shue.main()


# vim: set sw=4 et sts=4 :
