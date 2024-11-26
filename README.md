## julia

The Julia Set is another family of fractal structures. In Mandelbrot, we'd start at $z_0=0$ and for every $c$ in the plane, if we recursed out of 2, then our point $c$ isn't in the set. In Julia, we choose some $c$ and for every $z_0$ in the plane, if we recurse out of 2, then our point $z_0$ isn't in the set. 

Since we can choose any $c$ and then go over every point $z_0$, we have infinitely many julia sets. Some of which look more interesting than the others.

The test to determine if a complex number $z_0$ is part of the Julia Set grounded at some $c$:

1. Recursively apply $z_{i + 1}=z_i^2+c$. 
2. If you converge to a finite point or fluctuate between points, $z_0$ is in the set. If you tend towards infinity, $z_0$ isn't in the set.

So how do we test if $z_n$ converges or diverges? This is the same proof as Mandelbrot - all we did is change what we choose for $z$ and $c$. Same coloring as well. 
