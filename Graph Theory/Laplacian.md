<h1>Laplacian</h1>

For any graph $G = (V,E)$, one can define a matrix to represent the similarity of vertices in $V$. The most simple of these matrices is the <b>adjacency matrix</b> $W$, defined by 
$$W_{i,j} = 1 \quad \text{if   } (i,j) \in E$$
and $W_{ij} = 0$ otherwise. The adjacency matrix $W$ is simple because the $ij$th off-diagonal entry of $W$ is 1 if and only if there exists an edge between vertices $i$ and $j$. 

Another commonly used similarity matrix is some form of <b>distance matrix</b> $W^D$ of the form:
$$W^D_{i,j} = g(i,j) \quad \text{if   } ||F(i) - F(j)||_2 < r$$
and $W^D_{i,j} = 0$ otherwise, where $g$ and $F$ are functions and $r > 0$ is a parameter. Commonly, the kernal function 