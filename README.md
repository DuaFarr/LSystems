# LSystems
Python Based L System Solution
Youtube Link: https://youtu.be/6oCduWzAhBE
## L-System Graphical Modeling
The Lindenmayer system, often known as the L-system, is a parallel rewriting system and a sort 
of formal grammar. An L-system is made up of an alphabet of symbols that may be used to 
produce strings, a set of production rules that extend each symbol into some larger string of 
symbols, a starting "axiom" string from which to build, and a mechanism for translating the 
generated strings into geometric structures.
## Features: 
L-systems are important to this project; however, the rewriting and geometric interpretation 
of such L-systems is handled using Python 3's Turtle package. The fundamental concept of 
turtle interpretation is presented below. A Turtle state is described as a triplet (x, y,), where 
the Cartesian coordinates (x, y) represent the turtle's position and the angle, called the 
heading, represents the direction the turtle is facing. The turtle can respond to commands 
expressed by a particular collection of symbols provided the step size d and the angle 
increment (i.e., "F" meaning "move forward").
Using the same rewriting rules, this project may generate Fractals of various shapes using a 
recursive set of rules provided by the user.
## GUI Features: 
You can define an L-system by specifying:
• Starting Axiom
• Production Rule
• Number of iterations
• Segment Length
• Initial Angle
• Drawing Angle
## Detail: 
How does it work?
We choose an axiom, for example: 'A'
2
Now we have rules like: "A becomes AF" and "F becomes FA"
The next step is to iterate the axiom through the rules by a specific amount, the output will be 
fed through the rules again.
For example we iterate 3 times:
A -> AF
AF -> AFFA
AFFA -> AFFAFAAF
Our result string is now AFFAFAAF
The processing of the string works by checking char for char against the processing rules and 
do what they say. If we have something that doesn't fit any rules, it doesn't matter, we will just 
ignore it.
Processing the upper string would be lame, it will create a straight line. Let’s add a few more 
interesting chars to the production rules:
F -> a2FF-[c1-F+F+F]+[c1+F-F-F]
Axiom: F
Angle: 23
Iteration: 5
Well, that looks a little bit more complicated, and it is. This production rule contains nearly 
every possible processing rule and will create a colored tree with different-sized lines.
 
## Implementation: 
An L-System renderer's job is to take an L-System description (axiom, angle increment, and 
replacement rules) and an iteration count and generate a list of line segments to draw. I want 
to be clear that my goal is not to draw line segments rapidly; rather, I want to compute the 
(x,y) coordinates for all line segments as soon as feasible for a particular L-System and iteration 
count. Therefore, the metric for benchmarking is unit time per line segment computed (lower 
is better).
These are the supported commands and Variables:
R: recursive string-rewriting where symbols on the right side of the recursive formulas are 
substituted by corresponding strings on the left side.
3
L: recursive string-rewriting where symbols on the left side of the recursive formulas are 
substituted by corresponding strings on the right side.
+: turn angle left.
-: turn angle right.
[: push string / state to the memory stack.
]: lift pen up / stop drawing / pop string / state off the memory stack
