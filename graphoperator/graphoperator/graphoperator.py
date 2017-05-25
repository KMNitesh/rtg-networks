import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


__all__ = ["GraphOperator"]


class GraphOperator:
    """
    Generate a sparse matrix for a graph, and get eigenvalues and eigenvectors
    """
    def __init__ (self, graph, matrix_type, compute = True):
        """
        Parameters
        ----------
        matrix_type -- "combinatorial laplacian", "adjacency", "normalized laplacian"
        graph -- a NetworkX graph
        compute -- Boolean, compute eigendecomposition?
        """
        self._graph = graph
        self.laplacian = None 
        self.adjacency = None
        self.matrix_type = matrix_type
        self.cached = False
        self.sgs = []
        if compute:
            self.compute()

    def __repr__(self):
        out = "Graph, cached = {}\n{}\n{}".format(self.cached,
                self._graph,self.matrix_type)
        return out

    def compute(self, k = 6, **kwargs):
        """
        Compute the eigendecomposition for the laplacian and store in
        self.eigvals, self.eigvecs

        Parameters
        ----------
        k -- Number of eigenvalues to compute
        **kwargs -- additional arguments to scipy.sparse.linalg.eigsh
        """
        self.cached = True
        if self.matrix_type == "combinatorial laplacian":
            self.laplacian = nx.laplacian_matrix(self._graph).astype("d")
            self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.laplacian, k,
                which = 'SM')
        elif self.matrix_type == "adjacency":
            self.adjacency = nx.adjacency_matrix(self._graph).astype("d")
            self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.adjacency, k,
                which = 'SM')
        elif self.matrix_type == "normalized laplacian":
            self.normalized_laplacian = nx.normalized_laplacian_matrix(self._graph).astype("d")
            self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.normalized_laplacian, k,
                which = 'SM')
          
        else:
            self.cached = False
            raise ValueError("Needs to be one of ... TODO")
        
        self.getLabelsAndPos()
            
    def plot_eigenvals(self):
        """
        Plot eigenvalues from smallest to largest
        """
        plt.plot(self.eigvals)
        plt.xlabel("Index of Eigenvalues, smallest to largest")
        plt.ylabel("Eigenvalue")

    def plot_eigenvectors(self, p = 2, q = 3):
        """
        >>> g = ...
        >>> l = GraphLaplacian(g)
        >>> l.plot_eigenvectors()
        """
        plt.scatter(self.eigvecs[:,p-1],self.eigvecs[:,q-1])
        plt.xlabel("2nd Eigenvector")
        plt.ylabel("3rd Eigenvector")
        vec1 = self.eigvecs[:,p-1]
        vec2 = self.eigvecs[:,q-1]
        for j,k in self._graph.edges():
            plt.plot(vec1[[j,k]],vec2[[j,k]])
        
               
    def _split_once(self, standardVal):
        secondEigVec = self.eigvecs[:,1]
        nodes = self._graph.nodes()
        A = []
        B = []
        for i in range(0, len(secondEigVec)):
            if (secondEigVec[i] >= standardVal):
                A.append(nodes[i])
            else:
                B.append(nodes[i])
                
        self._removeEdge2(A, B)
        return A, B
    
    def partition(self, n_groups = 2, standardVal = 0):
        """
        self.sgs contain GraphOperator objects, each is a subgraph 
        Return a list of subgroups nodes, each subgraph is corresponding to one cluster
        """
   
        self.sgs = [self]
        self.nsgs = [self._graph]
   
        for i in range(n_groups - 1):
            self.sgs.sort(key = lambda x : x._graph.number_of_nodes(), reverse = True)
            largestgraph = self.sgs.pop(0)
            A, B = largestgraph._split_once(standardVal)
            largestgraph._removeEdge(A, B)
            g_A = largestgraph._graph.subgraph(A)
            G_A = GraphOperator(g_A, self.matrix_type)
            g_B = largestgraph._graph.subgraph(B)
            G_B = GraphOperator(g_B, self.matrix_type)
            self.sgs.extend([G_A, G_B])
        return [x._graph.nodes() for x in self.sgs]
    
    def _removeEdge2(self, A, B):
        for (i,j) in self._graph.edges():
            if ((i in A and j in B) or (i in B and j in A)):
                self._graph.edges().remove((i,j))
        return self._graph.edges()
    
    def _removeEdge(self, A, B):
        edgelist = self._graph.edges()
        for (i,j) in edgelist:
            if ((i in A and j in B) or (i in B and j in A)):
                edgelist.remove((i,j))
        return edgelist
    
    def getLabelsAndPos(self):
        self.pos = nx.spring_layout(self._graph)
        self.labels = {}
        nodes = self._graph.nodes()
        for i in range(0, len(nodes)):
            self.labels[nodes[i]] = i
    
    def draw_graph(self, colorA = 'lightsalmon', labels = True, node_size = 30, alpha = 0.5, width = 1):
        #  if (self.labels == {}
        #   self.getLabelsAndPos()
        
        nx.draw_networkx_nodes(self._graph, self.pos, node_color=colorA, node_size = node_size, alpha = alpha)
        nx.draw_networkx_edges(self._graph, self.pos, width = width)
        if (labels):
            nx.draw_networkx_labels(self._graph, self.pos, self.labels)
       
    def draw_partitionGraph(self, list_nodes, list_color, labels = True, node_size = 30, alpha = 0.5, width = 1, removeEdges = False):
        #if (self.labels == {}):
        #    self.getLabelsAndPos()
        
        for i in range(len(list_nodes)):
            nx.draw_networkx_nodes(self._graph, self.pos, nodelist = list_nodes[i], node_color=list_color[i], node_size = node_size, alpha = alpha)
        
        if (removeEdges and len(list_nodes) == 2):
            nx.draw_networkx_edges(self._graph, self.pos, edgelist = self._removeEdge(list_nodes[0], list_nodes[1]), width = width)
        else:
            nx.draw_networkx_edges(self._graph, self.pos, edgelist = self._graph.edges(), width = width)
        
        
        if (labels):
            nx.draw_networkx_labels(self._graph, self.pos, self.labels)

    def KMeans(self, n_clusters, **kwargs):
        X = np.array([np.sqrt(eigval) * self.eigvecs[:, i] for i, eigval in enumerate(self.eigvals)]).T
        return KMeans(n_clusters, **kwargs).fit(X)
    
    def KMeans_partition(self, n_clusters):
        kmeans = self.KMeans(n_clusters)
        index = np.arange(kmeans.labels_.shape[0])
        list_nodes = []
        nodes = self._graph.nodes()
        for i in range(n_clusters):
            list_nodes.append([nodes[i] for i in index[kmeans.labels_ == i]])
        return list_nodes

        
    @property
    def graph(self):
        self.cached = False
        return self._graph
