import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

class GraphOperator:
    """
    TODO: describe what this does
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
        if compute:
            self.compute()

    def __repr__(self):
        out = "LaplacianGraph, cached = {}\n{}".format(self.cached,
                self._graph)
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
            
    def plot_eigenvals(self):
        """
        Plot eigenvalues from smallest to largest
        """
        plt.plot(self.eigvals)
        plt.xlabel("Index of Eigenvector, smallest to largest")
        plt.ylabel("Eigenvalue")

    def plot_eigenvectors(self, p = 2, q = 3):
        """
        Plot eigenvalues from smallest to largest

        #TODO: plot graph with known 2 clusters (say)
        >>> g = ...
        >>> l = GraphLaplacian(g)
        >>> l.plot_eigenvectors()
        """
        plt.scatter(self.eigvecs[:,p-1],self.eigvecs[:,q-1])
        vec1 = self.eigvecs[:,p-1]
        vec2 = self.eigvecs[:,q-1]
        for j,k in self._graph.edges():
            plt.plot(vec1[[j,k]],vec2[[j,k]])

               
    def partition(self, standardVal = 0):
        secondEigVec = self.eigvecs[:,1]
        A = []
        B = []
        for i in range(0, len(secondEigVec)):
            if (secondEigVec[i] >= standardVal):
                A.append(i)
            else:
                B.append(i)
        return (A,B)
    
    def removeEdge(self, A, B):
        edgelist = self._graph.edges()
        for (i,j) in edgelist:
            if ((i in A and j in B) or (i in B and j in A)):
                edgelist.remove((i,j))
        return edgelist
    
    def draw_graphWithLabel(self):
        pos = nx.spring_layout(self._graph)
        labels = {}
        for i in range(0, len(self._graph.nodes())):
            labels[i] = i
        nx.draw_networkx_nodes(self._graph, pos)
        nx.draw_networkx_edges(self._graph, pos)
        nx.draw_networkx_labels(self._graph, pos, lables)
       
    def draw_partitionGraph(self, A, B):
        pos = nx.spring_layout(self._graph)
        labels = {}
        for i in range(0, len(self._graph.nodes())):
            labels[i] = i
        nx.draw_networkx_nodes(self._graph, pos, nodelist = A, node_color='y')
        nx.draw_networkx_nodes(self._graph, pos, nodelist = B, node_color='g')
        nx.draw_networkx_edges(self._graph, pos, edgelist = self.removeEdge(A, B))

            
            
    @property
    def graph(self):
        self.cached = False
        return self._graph

if __name__ == "__main__":

    lob = nx.random_lobster(5, 0.6, 0.9, seed = 37)
    g = GraphOperator(lob, "combinatorial laplacian", compute = False)
    g2 = GraphOperator(lob, "combinatorial laplacian", compute = True)
    g3 = GraphOperator(lob, "normalized laplacian")
