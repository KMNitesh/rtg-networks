import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt


class GraphLaplacian:
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
        self.laplacian = nx.laplacian_matrix(self._graph).astype("d")
        self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.laplacian, k,
                which = 'SM')
        self.cached = True

    def plot_eigenvals(self):
        """
        Plot eigenvalues from smallest to largest
        """
        plt.plot(self.eigvals)
        plt.xlabel("Index of Eigenvector, smallest to largest")
        plt.ylabel("Eigenvalue")

    def plot_eigenvectors(self, x = 1, y = 2):
        """
        Plot eigenvalues from smallest to largest

        #TODO: plot graph with known 2 clusters (say)
        >>> g = ...
        >>> l = GraphLaplacian(g)
        >>> l.plot_eigenvectors()
        """
        pass

    @property
    def graph(self):
        self.cached = False
        return self._graph

     

if __name__ == "__main__":

    lob = nx.random_lobster(20, 0.6, 0.9, seed = 37)
    g = GraphLaplacian(lob, compute = False)
    g2 = GraphLaplacian(lob, compute = True)


#def f()
        
#class ScipyMatrix(Matrix):
#    def __init__(self, matrix, edgelist):
#        Matrix.__init__(self, matrix, edgelist)
#        self.s_eigvals, self.s_eigvecs = sparse.linalg.eigsh(matrix.asfptype(), k = matrix.shape[0] -1, which = 'SM')
#        
#    def plot_eigenvals(self):
#        plt.plot(self.s_eigvals)
#        plt.show()
#        
#    def plot_edge_eigenvecs(self, p, q):
#        """
#        Scatters the pth and qth eigenvectors of the Laplacian Matrix and plots edges according to edgelist 
#
#        Parameters
#        ----------
#        p --- pth eigenvectors
#        q --- qth eigenvectors
#
#        Notes
#        ----------
#        eigenvectors are sorted by lowest to highest values of eigenvalues of the scipy matrix
#        """        
#        plt.scatter(self.s_eigvecs[:,p-1],self.s_eigvecs[:,q-1])
#        vec1 = self.s_eigvecs[:,p-1]
#        vec2 = self.s_eigvecs[:,q-1]
#        for j,k in self.edgelist:
#            plt.plot(vec1[[j,k]],vec2[[j,k]])
#        plt.show()
