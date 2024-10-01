## mandelbrot

The Mandelbrot Set is a set of complex numbers that, when plotted, create an interesting fractal structure.

The test to determine if a complex number $c$ is part of the Mandelbrot Set:

1. Start with $z_0=0$ and recursively apply $z_{i + 1}=z_i^2+c$. 
2. If you converge to a finite point or fluctuate between points, $c$ is in the set. If you tend towards infinity, $c$ isn't in the set.

So how do we test if $z_n$ converges or diverges?

Essentialy, if $|z_i| >2$ at any point in the recursion, you'll tend towards infinity. This is what we wrote in our code way back when, but we didn't go through any proof if I remember correctly.

