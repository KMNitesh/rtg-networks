<h1>Motivation for Spectral Methods</h1>
One natural problem that can arise while investigating a graph $G$ could be to find a partition $\{V_1,\ldots,V_k\}$ of $G$ such that the connectivity, or similarity, of vertices in each group $V_i$ is high and the level of connectivity between groups $V_i$ and $V_j$ is low.  This can be thought of as a problem of sorting vertices from $V$ into different clusters, or communities, of similarity.  Solving this type of problem using only the graph object itself can prove computationally difficult or inefficient.  However, we can overcome this problem by using an object called the <b>Laplacian</b> (See Laplacian.md for more).

For any graph $G$, one can define a matrix, the <b>combinatorial Laplacian</b>, which can be written as 
$$L = D - W$$
where $D$ is the $n \times n$ diagonal degree matrix and $W$ is the adjacency matrix. For any vector x, it can be seen immediately that $(L x)_i = \sum_{j=1}^n W_{i,j} (x_i - x_j)$. From this definition we can prove the following proposition:

<h2>Proposition 1</h2>
Suppose that $\{C_k\}_{k=1}^K$ are maximal connected sets of vertices of $G$ (the addition of any vertex to $C_k$ would be disconnected).  Then the null space of $L$, that is all vectors $x \in \mathbb{R}^n$ such that $Lx = 0$, is the span of the vectors 
$$\mathbf{1}_{C_k}, \quad k=1,\ldots,K$$
where $\mathbf{1}_A$ is 1 for the vertices in $A$ and 0 otherwise. (The proof of this is in the notes at the bottom of this page).

Note that for any vector $x \in \mathbb{R}^n$, the quadratic form of $L$
$$x^TLx = \sum_{i,j \in E}W_{i,j}(x_i - x_j)^2 \ge 0.$$ 
It immediately follows that the combinatorial Laplacian $L$ is a positive-semidefinite matrix, which means that all its eigenvalues are non-negative. 

<b>Proposition 1</b> tells us that for a graph with $K$ connected components, we can determine which vertices are in which connected component by examining the null space of $L$. In doing so, we can determine a grouping $\{C_k\}_{k=1}^K$ of vertices such that the level of connectivity between groups $C_i$ and $C_j$ is minimized (no edges between them). Because $L^K$ is a positive-semidefinite matrix, this information is stored equivalently in the span of the $K$ smallest eigenvectors of $L^K$.

Spectral methods have shown that when examining the laplacian $L^1$ of a fully connected graph, the $K$ smallest eigenvectors of $L^1$ will give information akin to that of the null space of $L^K$.  That it will help us find a grouping $\{V_k\}_{k=1}^K$ of vertices such that that the level of connectivity between groups $V_i$ and $V_j$ is low (according to some criterion). The methods explored in this repository are called spectral methods because they rely on the spectral decomposition of some similarity matrix of a graph, such as $L$.

<h2>Proof Appendix</h2>

Before proving <b>Proposition 1</b> it is useful to first prove the following lemma.

<h4>Lemma 1</h4>
For an unweighted, undirected graph $G$ that has only 1 connected component, the null space of its Laplacian $L$ is the span of the vector $\mathbf{1}$.

<h5>Proof (of Lemma 1)</h5>
Suppose a graph $G$ has only 1 connected component.  It is immediately evident for any $q \in \mathbb{R}$ that $span(\mathbf{1}) = (q\mathbf{1}) \subseteq null(L)$, since $$(L (q\mathbf{1}))_i = \sum_{j=1}^n W_{i,j} (q - q) = 0, \quad i = 1,\ldots,n.$$

Now suppose that there exists a vector $x \in null(L)$ such that $x$ can not be expressed in the form $q\mathbf{1}$ where $q \in \mathbb{R}$.  Then, $x_i \ne x_j$ for at least one $i \ne j$ and $$(L x)_i = \sum_{j=1}^n W_{i,j} (x_i - x_j) = 0, \quad i = 1,\ldots,n.$$  

This implies that the quadratic form $$x^TLx = \sum_{i,j : i > j}W_{i,j}(x_i - x_j)^2 = \sum_{i,j \in E}(x_i - x_j)^2 = 0,$$ 
which can only occur when $x_i = x_j, \forall i,j$. This contradicts the supposition that $x_i \ne x_j$ for at least one $i \ne j$. Therefore, if $x \in null(L)$ then $x_i = x_j, \forall i,j \Longleftrightarrow x \in span(\mathbf{1})$.  Thus, $null(L) \subseteq span(\mathbf{1})$.

Since $null(L) \subseteq span(\mathbf{1})$ and $span(\mathbf{1}) \subseteq null(L)$, it follows that $null(L) = span(\mathbf{1})$. $\Box$

<h3>Proof of Proposition 1</h3>
Let $L_i$ be the the Lapacian of the graph defined by the vertices from $C_i$, where $i = 1, \ldots, K$. Then, by reording the points, the Lapacian of a graph with $K$ connected components, denoted $L^K$, can be written as the block diagonal matrix below

$$
L^K =
\begin{bmatrix}
    L_{1} & 0 & \dots  & 0 \\
    0 & L_{2} & \dots  & 0 \\
    \vdots  & \vdots & \ddots & \vdots \\
    0 & 0 & \dots  & L_{K}
\end{bmatrix}
$$

Consider the Lapacian $L^1$ of a graph for which there is only one connected component ($K = 1$).  From **Lemma 1**, it follows that $null(L^1) = span(\mathbf{1}_{C_1})$. 

Suppose that the null space of the Lapacian $L^p$ for a graph $G$ with $p$ connected components is the span of the vectors $\mathbf{1}_{C_k}, k=1,\ldots,p$. Then if we write $L^p$ in the form 
$$
L^p =
\begin{bmatrix}
    L_{1} & 0 & \dots  & 0 \\
    0 & L_{2} & \dots  & 0 \\
    \vdots  & \vdots & \ddots & \vdots \\
    0 & 0 & \dots  & L_{p}
\end{bmatrix}
$$
then the null space is the span of the vectors
$$
\begin{bmatrix}
    1^{C_1} \\
    0 \\
    \vdots  \\
    0 
\end{bmatrix},
\begin{bmatrix}
    0 \\
    1^{C_2} \\
    \vdots  \\
    0 
\end{bmatrix},
\ldots,
\begin{bmatrix}
    0 \\
    0 \\
    \vdots  \\
    1^{C_p} 
\end{bmatrix},
$$
where $1^{C_k}$ is an all 1's vector with the same number of elements as the number of vertices in the connected component $C_k$.

Consider the Lapacian $L^{p+1}$ of a graph with one extra connected component. This can be written in the form
$$
L^{p+1} =
\begin{bmatrix}
    L^{p} & 0 \\
    0 & L_{p+1}
\end{bmatrix} = 
\begin{bmatrix}
    L_{1} & 0 & \dots & 0 & 0 \\
    0 & L_{2} & \dots & 0 & 0 \\
    \vdots & \vdots & \ddots & \vdots & \vdots \\
    0 & 0 & \dots & L_{p}  & 0 \\
    0 & 0 & \dots & 0 & L_{p+1}
\end{bmatrix}
$$
From **Lemma 1**, we know that the null space of $L_{p+1}$ is the span of $\mathbf{1}_{C_{p+1}}$. Because the columns and rows from $L_{p+1}$ are linearly independent from the rows and columns of $L^p$, it follows that the null space of $L^{p+1}$ is the span of the vectors
$$
\begin{bmatrix}
    1^{C_1} \\
    0 \\
    \vdots  \\
    0 \\
    0
\end{bmatrix},
\begin{bmatrix}
    0 \\
    1^{C_2} \\
    \vdots  \\
    0 \\
    0
\end{bmatrix},
\begin{bmatrix}
    0 \\
    0 \\
    \vdots  \\
    1^{C_p} \\
    0
\end{bmatrix},
\ldots,
\begin{bmatrix}
    0 \\
    0 \\
    \vdots  \\
    0 \\
    1^{C_{p+1}}
\end{bmatrix}.
$$
Therefore, by the Principle of Mathematical Induction, **Proposition 1** is true. $\Box$