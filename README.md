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

At first I bashed my way to prove this, but there's an easier way to think about it: Let $|z_i|$ be $x$ away from the origin, where $x$ is a positive number. $|z_i^2|$ is $x^2$ away. We want $c$ to bring $z_i^2$ back to the origin as much as possible. This is done when $c$ is directly opposite $z_i^2$ and is as far away from the origin as possible. So, let's assume it's directly across and has maximum distance, which is also $|z_i|$ or $x$. Therefore, $|z_i^2+c|$ is at least $x^2-x$. Is this greater than $|z_i| = $x$?. Solving $x^2-x>x$ leads to $x(x-2) > 0$. This has solutions for $x < 0$ and $x > 2$. We assumed $x$ is positive, so the only solution is $x > 2$. 

Therefore, when $x > 2$, $|z_i^2+c| > |z_i|$ is true.

However, there is a possibility of asymptotically approaching some value, like 3, where consecutive terms are getting closer to 3, but are bounded above by some value. This is still convergence. To get around this, we can prove that the difference between consecutive terms is >= 0.

#### Claim 2: The difference between consecutive terms is either constant or increasing.
If $|z_i|$ is $x$, then $|z_i^2|$ is $x^2$. Let $|c|$ be $y$ and let it, in the worst case, be exactly opposite $|z_i^2|$. Therefore, $|z_i^2 + c| = x^2-y$. Since $x > 2$, we know that $x^2>4 \to x^2 > 2x > 4$. Therefore, $|z_i^2 + c|$ can be viewed as always being bounded below by, or at least as big, as $2x-y$. Now, the difference between this and $|z_i|$ is $(2x-y)-x = x-y$. Since $|z_i| > |c|$, this value is guaranteed to be positive. Now, since $x$ is increasing, $x-y$ as a term is always increasing. With that, the difference between consecutive terms is always increasing.



