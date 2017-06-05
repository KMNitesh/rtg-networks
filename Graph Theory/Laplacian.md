<h1>Laplacian Theory</h1>

For any graph $G = (V,E)$, one can define a matrix to represent the similarity of vertices in $V$. The most simple of these matrices is the <b>adjacency matrix</b> $W$, defined by 
$$W_{i,j} = 1 \quad \text{if   } (i,j) \in E$$
and $W_{ij} = 0$ otherwise. The adjacency matrix $W$ is simple because the $ij$th off-diagonal entry of $W$ is 1 if and only if there exists an edge between vertices $i$ and $j$. 

Another commonly used similarity matrix is some form of <b>distance matrix</b> $W^D$ of the form:
$$W^D_{i,j} = g(i,j) \quad \text{if   } ||F(i) - F(j)||_2 < r$$
and $W^D_{i,j} = 0$ otherwise, where $g$ and $F$ are functions, $g$ is strictly positive, and $r > 0$ is a user-defined parameter. Commonly, $g(i,j)$ is taken to be the kernal function so that
$$W^D_{i,j} = exp(-\frac{||F(i) - F(j)||_2}{\sigma^2}) \quad \text{if   } ||F(i) - F(j)||_2 < r$$
where $\sigma^2$ is another user-defined parameter. 

For any similarity matrix, the <b>degree matrix</b> is defined as $D_{i,i} = \sum_{j}W_{i,j}$ on the diagonal and 0 off-diagonal. The $i$-th diagonal entry of the degree matrix represents the total number of connections that the node $i$ has to all other nodes in the graph.

For any graph $G$, one can define a matrix, the <b>combinatorial Laplacian</b>, which can be written as 
$$L^{comb} = D - W$$
where $D$ is the $n \times n$ diagonal degree matrix and $W$ is the adjacency matrix.

For an undirected graph with a combinatorial Laplcian L, then

* L is symmetric.
* L is positive-semidefinite.
* The smallest eigenvalue of L is 0.
* The dimension of the nullspace of L is the number of connected components in G.
* has all of its rows and all of its columns sum to 0

For any graph $G$ one is also able to define the <b>normalized Laplacian</b>, which can be written as
$$L^{norm} = D^{-\frac{1}{2}}L^{comb}D^{-\frac{1}{2}} = I - D^{-\frac{1}{2}}WD^{-\frac{1}{2}}$$
where $I$ is the identity matrix, $W$ is the adjacency matrix, and $D$ is the degree matrix. 

The combinatorial and normalized Laplacian matricies are useful objects because it can be shown that their eigenvectors with small eigenvalues (near 0) can help to form a good partition of a graph. But what is considered an effective partition a graph?

<h3>Partitioning criterion</h3>

Typically, a partition $\{V_1, \ldots, V_K\}$ of a graph $G = (V,E)$ is effective if it minimizes either the <b>Normalized Cut criterion</b>
$$\sum_{i=1}^KNCut(V_i, V_i^C) = \sum_{i=1}^K\frac{cut(V_i,V_i^C)}{assoc(V_i,V)},$$
which is biased to balancing the number of *edges* in each set $V_i$ of the partition, or the <b>Ratio Cut criterion</b>
$$\sum_{i=1}^KRCut(V_i, V_i^C) = \sum_{i=1}^K\frac{cut(V_i,V_i^C)}{|V_i|},$$
which is biased to balancing the number of *nodes* in each set $V_i$.

Optimizing either of these quantities exactly is an NP-hard problem. However, it can be shown (in a way similar to the Shi and Malik) that the 2nd to $K+1$ smallest eigenvectors of the normalized Laplacian ($L^{norm}$) can be used to approximate the optimal solution to the minimimum normalized cut problem and the 2nd to $K+1$ smallest eigenvectors of the combinatorial Laplacian ($L^{comb}$) can be used to approximate the optimal solution to the minimum ratio cut problem. 

In general, clustering using the normalized Laplacian ($L^{norm}$) tends to balance the number of edges in each of the sets $V_i$ in the partition $\{V_1, \ldots, V_K\}$, while clustering using the combinatorial Laplacian ($L^{comb}$) tends to balance the number of nodes.