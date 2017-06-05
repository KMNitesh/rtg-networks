<h1>$K$-Way Spectral Clustering</h1>
Often we may wish to determine whether or not $K$ communities are present in a particular graph, and if so, to uncover them efficiently.  Methods similar to Shi and Malik's Normalized Cut algorithm, which use the second smallest eigenvector of the Laplacian to bi-partition a graph, can be used recursively in order to obtain $K$ clusters of verticies. However, if $K$ is not an order of 2, these bipartitioning methods can be shown to perform poorly. 

Intuitively, this makes sense. For example, if $K = 3$, then the only 

Thus, in [On Spectral Clustering: Analysis and an algorithm](http://ai.stanford.edu/~ang/papers/nips01-spectral.pdf "Title"), Ng, Jordan, and Weiss sought to devise a practical algorithm that would simultaneously partition a graph $G$ into $K$ parts effectively.

<h3>Algorithm</h3>

1. Set up an undirected graph $G=(V,E)$ for which you want to cluster into $k$-groups.
2. Find $x_1, x_2, \ldots, x_k$ the $k$ smallest eigenvectors of the Laplacian used (where $x_1, x_2, \ldots, x_k$ are orthogonal to one another).
3. Form the matrix $X = [x_1, x_2, \ldots, x_k] \in \mathbb{R}^{n \times k}$.
4. Form the matrix $Y$ by renormalizing each row of $X$ to have unit length (i.e. $Y_{ij} = X_{ij}/(\sum_{j}X_{ij})^2$).
5. Treat each row of Y as a point in $\mathbb{R}^k$ and cluster using [K-means clustering](https://sites.google.com/site/dataclusteringalgorithms/k-means-clustering-algorithm "Title") (or another algorithm that minimizes distortion).
6. Assign point $s_i$ to cluster $j$ if and only if the $i$-th row of $Y$ was assigned to cluster $j$ in section 5.

The idea behind using this type of algorithm is intuitive: Recall that when a graph has $K$ disconnected components, $\{C_k\}_{k=1}^K$, the smallest $K$ eigenvectors of its Laplacian $L$ will be the span of the vectors 
$$\mathbf{1}_{C_k}, \quad k=1,\ldots,K$$
where $\mathbf{1}_A$ is 1 for the vertices in $A$ and 0 otherwise. Therefore, under the ideal case where there are $K$ disconnected components in a graph, the transformation $L \rightarrow Y$ maps of each row of $L$ to one of $K$ mutually orthogonal points on a unit $K$-sphere. Points are a $K$-touple of the form $1_k$, or are 1 at the $k$-th entry if it is in the $k$-th disconnected component and 0s elsewhere. Using k-means on these points recovers the seperate disconnected components (as all points in the same disconnected component are mapped to the same point and are thus infinitely close).

If there is only 1 disconnected component, then the transformation $L \rightarrow Y$ maps each row of $L$ to a point within a unit $K$-sphere. In this case, each row is not mapped to exactly the same point, but using k-means clustering on these points can determine a good clustering of verticies. The intuition here is that if points are close to one another in this reduced $K$-dimensional eigenspace, they are more similiar to one another than points farther away.

Although not directly maximizing or minimizing any specific criterion, using the Normalized Laplacian (${D}^{-\frac{1}{2}}{L}{D}^{-\frac{1}{2}}$) when performing the algorithm tends to balance the number of edges across the $K$ clusters, while using the Combinatorial Laplacian ($L$) tends to balance the number of nodes across the resulting $K$ clusters. 