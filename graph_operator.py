import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

class GraphOperator:
    """
    TODO: describe what this does
    """
    def __init__ (self, graph, compute = True):
        """
        Parameters
        ----------
        graph -- a NetworkX graph
        compute -- Boolean, compute eigendecomposition?
        """
        self._graph = graph
        self.laplacian = None
        self.adjacency = None
        self.cached = False
        if compute:
            self.compute()

    def __repr__(self):
        out = "LaplacianGraph, cached = {}\n{}".format(self.cached,
                self._graph)
        return out

    def compute(self, matrix_type = "laplacian", k = 6, **kwargs):
        """
        Compute the eigendecomposition for the laplacian and store in
        self.eigvals, self.eigvecs

        Parameters
        ----------
        matrix_type -- "laplacian", "adjacency", TODO
        k -- Number of eigenvalues to compute
        **kwargs -- additional arguments to scipy.sparse.linalg.eigsh
        """
        self.cached = True
        if matrix_type == "laplacian":
            self.laplacian = nx.laplacian_matrix(self._graph).astype("d")
            self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.laplacian, k,
                which = 'SM')
        elif matrix_type == "adjacency":
            self.adjacency = nx.adjacency_matrix(self._graph).astype("d")
            self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.adjacency, k,
                which = 'SM')
        elif matrix_type == "normalized laplacian":
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

    @property
    def graph(self):
        self.cached = False
        return self._graph

if __name__ == "__main__":

    lob = nx.random_lobster(20, 0.6, 0.9, seed = 37)
    g = GraphOperator(lob, compute = False)
    g2 = GraphOperator(lob, compute = True)