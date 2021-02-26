
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
- improvisated key patterns, e.g. using a random seed.

---

I think 'order' means, distance along the diagonal, thus 3/1 . 12 . 3/1 means a box 3 wide 1 tall, a diagonal 12 long, and the same box at the end of the diagonal.  It could therefore be referring to the three stages in the diagram of the book, stage 1,2,3 drawing lines.  This is a different approach to the network/graph based approach I've already tried.

Mitring seems to refer to the index of the triangles in the corners of repetitions.  e.g. 4.9.14.19.24 on a given edge, e.g. top or bottom = 5 less 1.