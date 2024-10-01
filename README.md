## mandelbrot

The Mandelbrot Set is a set of complex numbers that, when plotted, create an interesting fractal structure.

The test to determine if a complex number $c$ is part of the Mandelbrot Set:

1. Start with $z_0=0$ and recursively apply $z_{i + 1}=z_i^2+c$. 
2. If you converge to a finite point or fluctuate between points, $c$ is in the set. If you tend towards infinity, $c$ isn't in the set.

So how do we test if $z_n$ converges or diverges?

Essentialy, if $|z_i| >2$ at any point in the recursion, you'll tend towards infinity. This is what we wrote in our code way back when, but we didn't go through any proof if I remember correctly.

### proof:
Shoutout Sid for the help with this. 
#### Claim 1: Once you leave 2, the ratio of consecutive terms is greater than 1. With this, we can at least prove that $z$ is strictly increasing. 
$$|z_i|>2 \text{ and } |z_i| >= |c|, \text{ then } \frac{|z_{i+1}|}{|z_i|} > 1$$

Why do we care about this? In general, if we're tending towards infinity, $z_i$ will go further away from the origin than $c$. At some point, it should pass $2$ if it's on the way to infinity.

At first I bashed my way to prove this, but there's an easier way to think about it: Let $|z_i|$ be $x$ away from the origin. $|z_i^2|$ is $x^2$ away.
