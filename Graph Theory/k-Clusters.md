<h1>$K$-Way Spectral Clustering</h1>
Often we may wish to determine whether or not $K$ communities are present in a particular graph, and if so, to uncover them efficiently.  Methods similar to Shi and Malik's Normalized Cut algorithm, which use the second smallest eigenvector of the Laplacian to bi-partition a graph, can be used recursively in order to obtain $K$ clusters of verticies.However, if $K$ is not an order of 2, these bipartitioning methods can be shown to perform poorly.

Thus, in [On Spectral Clustering: Analysis and an algorithm](http://ai.stanford.edu/~ang/papers/nips01-spectral.pdf "Title"), Ng, Jordan, and Weiss sought to devise a practical algorithm that would simultaneously partition a graph $G$ into $K$ parts effectively.  But, what does it mean for a partition to be effective in this case? Similar to the Shi and Malik problem, a partition $\{V_1, \ldots, V_K\}$ of a graph $G = (V,E)$ is effective if it minimizes either the <b>General Normalized Cut criterion</b>
$$\sum_{i=1}^KNCut(V_i, V_i^C) = \sum_{i=1}^K\frac{cut(V_i,V_i^C)}{assoc(V_i,V)},$$
which is biased to balancing the number of *edges* in each set $V_i$ of the partition, or the <b>General Ratio Cut criterion</b>
$$\sum_{i=1}^KRCut(V_i, V_i^C) = \sum_{i=1}^K\frac{cut(V_i,V_i^C)}{|V_i|},$$
which is biased to balancing the number of *nodes* in each set $V_i$.

Because optimizing either of these quantities exactly is an NP-hard problem, their method uses the $K$ smallest orthogonal eigenvectors of the Normalized Laplacian ($D^{-\frac{1}{2}}LD^{-\frac{1}{2}}$) to approximate the optimization of the Normalized Cut criterion and the $K$ smallest orthogonal eigenvectors of the Combinatorial Laplacian ($L$) to approximate the optimization of Ratio Cut criterion. 

<h3>Algorithm</h3>

The summary of the algorithm used in their paper is given below:

1. Set up an undirected graph $G=(V,E)$ for which you want to cluster into $k$-groups.
2. Find $x_1, x_2, \ldots, x_k$ the $k$ smallest eigenvectors of the Laplacian used (where $x_1, x_2, \ldots, x_k$ are orthogonal to one another).
3. Form the matrix $X = [x_1, x_2, \ldots, x_k] \in \mathbb{R}^{n \times k}$.
4. Form the matrix $Y$ by renormalizing each row of $X$ to have unit length (i.e. $Y_{ij} = X_{ij}/(\sum_{j}X_{ij})^2$).
5. Treat each row of Y as a point in $\mathbb{R}^k$ and cluster using [K-means clustering](https://sites.google.com/site/dataclusteringalgorithms/k-means-clustering-algorithm "Title") (or another algorithm that minimizes distortion).
6. Assign point $s_i$ to cluster $j$ if and only if the $i$-th row of $Y$ was assigned to cluster $j$ in section 5.

The idea behind using this type of algorithm is intuitive. Under the ideal case where there are $K$ disconnected components in a graph $G$