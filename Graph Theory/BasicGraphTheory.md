<h1>Basic Graph Theory</h1>

At the most simple level, a <b>graph</b> $G = (V,E)$ is an ordered set that is comprised of a set of vertices $V$ and an edge-set $E$. Each element of $E$ is a set of 2 elements from the vertex set $V$. If two vertices $u,v \in V$ are such that $\{u,v\} \in E$, then we say that an edge exists between $u$ and $v$ and intuitively $u$ and $v$ are thought of to be "similar". Below is an example of how one could represent the graph $G = (\{1, \ldots, 6\}, \{\{1,2\}, \{1,5\}, \{2,3\}, \{2,5\}, \{3,4\} \{4,5\}, \{4,6\}\})$ visually:

![Simple Graph](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/250px-6n-graf.svg.png)

(Credit: Wikipedia)

Graphs have many practical applications and are commonly used to represent networks in disciplines including computer science, physics, biology, climatology, and sociology. For example, when examining a social circle, each person in the circle can each be represented by a separate vertices and their level of friendship could determine whether or not their corresponding vertices are connected by an edge. 

If the edge-set $E$ of a graph $G = (V,E)$ consists of ordered pairs of elements from $V$, then the graph $G$ is called a <b>directed graph</b>.  In this context, an edge can be thought of as a one-way relation that point from one vertex to another like an arrow.  Directed graphs can be used to represent a network such as Twitter, in which a vertex would represent a user and an edge would represent a follow. (i.e. one user follows another, but the other user doesn't follow them back.) Like undirected graphs, directed graphs have many applications.

There are many, many more variations on how to define a particular graph.  For brevity, every way is not included here. However, one may be able to learn more using the following resources:

* http://www.people.vcu.edu/~gasmerom/MAT131/graphs.html
* http://mathworld.wolfram.com/AdjacencyMatrix.html
* https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms