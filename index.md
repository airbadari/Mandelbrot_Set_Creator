# notes

I took a class a few years ago at GHP where we wrote some basic stuff to visualize the famous Mandelbrot set. 

I realized recently that I couldn't remember how it was constructed, so these are just some notes for myself in case I forget it again.

## definition
The Mandelbrot Set is a set of points that, when plotted, create an interesting fractal structure.

Back when I took the class, I thought fractals were just self-similar shapes. You zoom in enough and eventually see the same thing. Apparently, that's not the case, and according to [3Blue1Brown](https://www.youtube.com/watch?v=gB9n2gHsHN4), we can define fractals more rigorously.

Some other definitions help with defining fractals. 

<strong>Scaling Factor:</strong> I was actually having trouble defining this well. I'm sure one of these will suffice:

Given two similar shapes: 
1. Choose the same curve/side on both shapes and take its length. Divide the larger length by the smaller length to find the factor to scale from the smaller to the larger shape. 1 over that to scale down.
2. Lay one of the shapes on the plane. If you multiply all points on the shape by some factor $s$, the resulting shape will be congruent to the other shape. That's the scaling factor from the one you laid down to the other one.

<strong>Mass: </strong> I guess area in a way. Some fractals are technically just a lot of lines (Sierpinski Triangle), so thinking of it as if you were measuring grams is actually better.


<strong>Dimension: </strong> Also not easy to define. Someone on Wolfram MathWorld says it's 'the number of coordinates needed to specify a point on the object'. Doesn't make much sense in terms of non-integer values.

It's easier to observe in practice. We'll need to reference Mass and Scaling Factor.
Given 

A <strong>Fractal</strong> is a shape with non-integer dimension. 








## About Me
- **Name:** Rishikesh Badari
- **Occupation:** Software Development Engineer Intern at Amazon

## Projects
- [Project 1](https://github.com/rishikeshbadari/project1)
- [Project 2](https://github.com/rishikeshbadari/project2)
