import networkx as nx
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

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
        return A, B
    
    def partition(self, n_groups = 2, standardVal = 0):
        """
        Return a list of groups, each group is a subgraph corresponding to one cluster
        """
   
        sgs = [self]
   
        for i in range(n_groups - 1):
            sgs.sort(key = lambda x : x._graph.number_of_nodes(), reverse = True)
            largestgraph = sgs.pop(0)
            A, B = largestgraph._split_once(standardVal)
            g_A = largestgraph._graph.subgraph(A)
            G_A = GraphOperator(g_A, self.matrix_type)
            g_B = largestgraph._graph.subgraph(B)
            G_B = GraphOperator(g_B, self.matrix_type)
            sgs.extend([G_A, G_B])
            
        return [x._graph.nodes() for x in sgs]
    
    def removeEdge(self, A, B):
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
       
    def draw_partitionGraph(self, list_nodes, list_color, labels = True, node_size = 30, alpha = 0.5, width = 1):
        #if (self.labels == {}):
        #    self.getLabelsAndPos()
        
        for i in range(len(list_nodes)):
            nx.draw_networkx_nodes(self._graph, self.pos, nodelist = list_nodes[i], node_color=list_color[i], node_size = node_size, alpha = alpha)
        #nx.draw_networkx_nodes(self._graph, self.pos, nodelist = B, node_color=colorB, node_size = node_size, alpha = alpha)
        nx.draw_networkx_edges(self._graph, self.pos, edgelist = self._graph.edges(), width = width)
        if (labels):
            nx.draw_networkx_labels(self._graph, self.pos, self.labels)

            
            
    @property
    def graph(self):
        self.cached = False
        return self._graph


