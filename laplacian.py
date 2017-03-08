import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt


class GraphLaplacian:
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
        return "TODO: think about what we want to print"

    def compute(self, k):
        self.laplacian = nx.laplacian_matrix(self._graph)
        self.eigvals, self.eigvecs = sparse.linalg.eigsh(self.laplacian, k,
                which = 'SM')

    @property
    def graph(self):
        self.cached = False
        return self._graph

    def plot_eigenvals(self):
        plt.plot(self.eigvals)
      
        
class ScipyMatrix(Matrix):
    def __init__(self, matrix, edgelist):
        Matrix.__init__(self, matrix, edgelist)
        self.s_eigvals, self.s_eigvecs = sparse.linalg.eigsh(matrix.asfptype(), k = matrix.shape[0] -1, which = 'SM')
        
    def plot_eigenvals(self):
        plt.plot(self.s_eigvals)
        plt.show()
        
    def plot_edge_eigenvecs(self, p, q):
        """
        Scatters the pth and qth eigenvectors of the Laplacian Matrix and plots edges according to edgelist 

        Parameters
        ----------
        p --- pth eigenvectors
        q --- qth eigenvectors

        Notes
        ----------
        eigenvectors are sorted by lowest to highest values of eigenvalues of the scipy matrix
        """        
        plt.scatter(self.s_eigvecs[:,p-1],self.s_eigvecs[:,q-1])
        vec1 = self.s_eigvecs[:,p-1]
        vec2 = self.s_eigvecs[:,q-1]
        for j,k in self.edgelist:
            plt.plot(vec1[[j,k]],vec2[[j,k]])
        plt.show()
