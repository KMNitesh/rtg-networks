<h1>Bi-Partition</h1>

![Karate Club](http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/_images/karate_factions.png)

A graph $G = (V,E)$ can be partitioned  or clustered into two disjoint sets $A$ and $B$ (where $A \cup B = V$ and $A \cap B = \emptyset$) by removing edges connecting the two parts. In graph theory, the *cut* of $A$ and $B$ 
$$cut(A,B) = \sum_{u \in A, v \in B}w(u,v)$$ 
is a measure of dissimilarity between the two pieces of the graph. In the case of an undirected unweighted graph, the cut is simply the number of edges in $E$ that are removed in forming the partition. 

<h3>Shi and Malik's Normalized Cut</h3>
As presented by Shi and Malik in [*Normalized Cuts and Image Segmentation*](https://people.eecs.berkeley.edu/~malik/papers/SM-ncut.pdf "Title") (2000), one should consider the following questions prior to partitioning a graph:

1. What is a criterion for a good partition?
2. How can such a criterion be computed efficiently?

A simple partitioning criterion, the *minimized cut*, claims that the optimal bi-partitioning of a graph minimizes the value of $cut(A,B)$.  However, this is biased to favor cutting small nodes in isolated portions of the graph. 

To avoid this unnatural bias, Shi and Malik proposed the **normalized cut**
$$Ncut(A,B) = \frac{cut(A,B)}{assoc(A,V)} + \frac{cut(A,B)}{assoc(B,V)}$$
where $assoc(A,V) = \sum_{u \in A, t \in V}w(u,t)$ is the total connection from nodes in A to all nodes in the graph. The intuition behind this measure is to examine the cut cost as a fraction of the total edge connections to all nodes in the graph. Shi and Malik argued that minimizing the normalized cut is a good criterion for forming a reasonable partition of $G$ because it simultaneously minimized dissociation between the groups and maximized association within the groups.

Using $min_{A:A \subset V}NCut(A,A^c)$ as a criterion for bi-partitioning directly is problematic in practice, as it has been shown to be an NP-hard problem. Therefore, in order for this criterion to be useful, an approximation must be used.

Through a rigorous derivation, Shi and Malik showed that if $x$ is an indicator variable such that $x_i=1$ if $i \in A$ and $x_i=-1$ if $i \in B$, then
$$min_{x}Ncut({x}) = min_{y}\frac{{y}^T{L}{y}}{{y}^T{D}{y}}$$
with the conditions that (1) ${y}(i) \in \{1,-b\}$ (for some $b \in \mathbb{R}^+$) and (2) ${y}^T{D}{1} = 0$ (or ${y}^T{D}$ is orthogonal to the ones vector).  [Note that $x(i)=1$ or $i \in B$ corresponds to $y(i) = 1$ and that $x(i)=-1$ or $i \in B$ corresponds to $y(i) = - b$]. The expression on the right of the above equation is a well studied form called the Rayleigh quotient, and therefore, if ${y}$ **is relaxed to take on real values**, then we can minimize the normalized cut above by solving the generalized eigenvalue system
$${L}{y} = \lambda{D}{y}$$ which we can re-write as 
$${D}^{-\frac{1}{2}}{L}{D}^{-\frac{1}{2}}{z}= \lambda{z}$$
where ${z} = {D}^{\frac{1}{2}}{y}$. Because vector ${z}_0 = {D}^{\frac{1}{2}}{1}$ is an eigenvector with eigenvalue 0 in the lower system, we can see that constraint ${y}^T{D}{1} = 0$ is automatically satisfied by the solution to generalized eigensystem.  

Because  ${L}$ is known to be a symmetric (undirected case), positive semidefinite matrix ${z}_0$ has the smallest eigenvalue in the lower system and that all eigenvectors of the lower system are orthogonal. Translating the constraints back into the higher generalized eigensystem we have (1) ${y}_0 = {1}$ is the smallest eigenvector with eigenvalue 0 and (2) $0 = {z}_1^T{z}_0 = {y}_1^T{D} {1}$, where ${z}_1$ and ${y}_1$ are the second smallest eigenvectors of the lower and upper systems respectively. Under constraint (2) (orthogonality of 2 smallest eigenvectors), it can be shown that the Rayleigh quotient is minimized by the 2nd smallest eigenvector, or the Fiedler Vector, and takes the minimum value equal to the eigenvalue of the Fiedler Vector. Therefore, it follows that the second smallest eigenvector ${y}_1$ of the higher generalized eigensystem
$${y}_1 = arg.min_{{y}^T{D}{1} = 0}\frac{{y}^T{L}{y}}{{y}^T{D}{y}}$$
is the real-valued solution to the problem. 

<h4>Summary of Minimum Normalized Cut Algorithm</h4>
In conclusion, the graph partitioning/clustering algorithm using the minimum normalized cut can be broken down into 4 steps:

1. Set up a fully connected, undirected graph $G = (V,E)$ for which you seek to partition.
2. Solve ${L}{y} = \lambda{D}{y}$ for eigenvectors with the smallest eigenvalues. (Or equivalently solve ${D}^{-\frac{1}{2}}{L}{D}^{-\frac{1}{2}}{z}= \lambda{z}$ and convert back to ${y}$ through the relation ${y} = {D}^{-\frac{1}{2}}{z}$)
3. Use the eigenvector with the second smallest eigenvalue to bipartition the graph. (Often 0 is chosen as a cut-off point, so that all nodes corresponding to negative entries in the second smallest eigenvector belong to one group and all nodes corresponding to positive entries in the second smallest eigenvector belong to another).
4. Decide if current partition should subdivided, then recursively sub-divided the two groups.

<h3>The Ratio Cut</h3>
An alternative to the minimum normalized cut criterion is the minimum ratio cut criterion. Let $|A|$ is the number of nodes in a set $A$. Then the ratio cut is defined as
$$Rcut(A,B) = \frac{Cut(A,B)}{|A|} + \frac{Cut(A,B)}{|B|} = n\frac{Cut(A,B)}{|A||B|}$$
The ratio cut uses number of nodes in each set of the partition as a normalizing factor to cost cut instead of the total connectivity of each set used in the Normalized Cut. This tends to create partitions in which the number of nodes in each of the two sets are roughly equal.

Similar to the normalized cut, it can be shown that for an indicator variable $x$, then minimum ratio cut is
$$min_{x}Rcut({x}) = min_{y}\frac{{y}^T{L}{y}}{{y}^T{y}}$$
under the conditions that (1) ${y}(i) \in \{1,-b\}$ (for some $b \in {R}^+$) and (2) ${y}^T{1} = 0$ (see [here](http://www.cis.upenn.edu/~cis515/cis515-15-spectral-clust-chap5.pdf) for more).  Because this is a special case of the minimum normalized cut problem with ${D}$ equal to the identity matrix, the real valued solution to our problem is the Fiedler Vector (eigenvector with the second smallest eigenvalue) of the eigensystem
$${L}{y} = \lambda{y}$$
Therefore, a similar algorithm to the Normalized Cut can be used to implement the ratio cut.

<h4>Summary of Minimum Ratio Cut Algorithm</h4>
In conclusion, the graph partitioning/clustering algorithm using the ratio cut can be broken down into 4 steps:

1. Set up an undirected graph ${G} = ({V},{E})$ for which you seek to partition.
2. Solve ${L}{y} = \lambda{y}$ for eigenvectors with the smallest eigenvalues.
3. Use the eigenvector with the second smallest eigenvalue to bipartition the graph. (Often 0 is chosen as a cut-off point, so that all nodes corresponding to negative entries in the second smallest eigenvector belong to one group and all nodes corresponding to positive entries in the second smallest eigenvector belong to another).
4. Decide if current partition should subdivided, then recursively sub-divided the two groups.
