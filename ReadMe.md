
# ReadMe

Key Patterns from Celtic Knotwork, experimentation from George Bain's book

![Key Pattern](https://raw.githubusercontent.com/ariejdl/key-patterns/master/images/pat1.png "Key Pattern")
![Key Pattern](https://raw.githubusercontent.com/ariejdl/key-patterns/master/images/pat3.png "Key Pattern")

## notes

notice there are bifurcations in some key patterns

```
     ----
 ---|
    -----
```

the patterns seems to consist in
symmetries and repetitions
including rotational symmetries

...representing these key patterns as a graph
would allow creation of loops (e.g. circular key patterns)

...one form of simple rendering could be simply drawing all edges

...node keys could simply be their coordinates
e.g. (0,0), (1,0)

...all edges must move only a maximum of one space

---

## ideas

- order based key patterns
- space filling key patterns (given an order)
- path following key patterns (given an order)
- improvised key patterns, e.g. using a random seed.

---

I think 'order' means, distance along the diagonal, thus 3/1 . 12 . 3/1 means a box 3 wide 1 tall, a diagonal 12 long, and the same box at the end of the diagonal.  It could therefore be referring to the three stages in the diagram of the book, stage 1,2,3 drawing lines.  This is a different approach to the network/graph based approach I've already tried.

Mitring seems to refer to the index of the triangles in the corners of repetitions.  e.g. 4.9.14.19.24 on a given edge, e.g. top or bottom = 5 less 1.

...not sure but I think the order of a pattern in conjunction with space filling of inner corners (and possibly outer corners) may be able to define a pattern, i.e. the strand must be able to double back on itself wherever it goes (I suppose this is the diffference between them and knotwork as the latter can weave above or below)...I'm looking for a minimalist algorithm from to generate patterns from orders.

---

*pseudo-alg* idea:

1. specify:
	- order/multiples
	- spaces down and spaces across
	- area to fill
- draw walls for:
	- order/multiples
	- edges
	- and perhaps corners
- Choose a direction.
- Let the path follow its present direction until it is deflected by a wall
- Path must always be beside a wall or edge (doubling back may be what enables exploration of a wall).  Preference may be for the edge which ends first.

does this work for the line travelling in both directions?  Is this necessary?: when on its current path it has no space to double back, let it double back.

edge cases for it:

- somewhat related:
	- bands between can be added as additional walls as is they were horizontal or vertical edges (these may be inset first)
	- sometimes rather than following a diagonal wall a horizontal and vertical segment cover the same spaces but leaving the wall.
	- sometimes rather than spiraling together from opposite directions two strands jump, therefore not making a square spiral
- potential solution to above: a point where departure from the line could be made

useful thing: convert pattern to fractional points (rather than decimal?) or multiply by sqrt(2)?