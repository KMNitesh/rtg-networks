# rtg-networks

##References

##Datasets
http://snap.stanford.edu/data/index.html

##Software

####1.[Networkx](https://networkx.github.io/)
(Open Scourse)
- A graph created with NetworkX
- Classes for graphs and digraphs.
- Conversion of graphs to and from several formats.
- Ability to construct random graphs or construct them incrementally.
- Ability to find subgraphs, cliques, k-cores.
- Explore adjacency, degree, diameter, radius, center, betweenness, etc.
- Draw networks in 2D and 3D. 
  
####2.[Igraph](http://igraph.org/python/#startpy)
(Open Scourse)
- igraph is easy to combine with Networkx
- igraph can be used to generate graphs, compute centrality measures and path length based properties as well as graph components and graph motifs. It also can be used for Degree-preserving randomization. Igraph can read and write Pajek and GraphML files, as well as simple edge lists. The library contains several layout tools as well.
- [reference manual](http://igraph.org/c/doc/igraph-docs.pdf) and [Preview](http://www.necsi.edu/events/iccs6/papers/c1602a3c126ba822d0bc4293371c.pdf)

####3.[graph-tool](https://graph-tool.skewed.de/)
[Open Scourse]
- Graph-tool is a python module for efficient analysis of graphs. Its core data structures and algorithms are implemented in C++, with heavy use of Template metaprogramming, based on the Boost Graph Library. It contains a comprehensive list of algorithms.
- Creation and manipulation of directed or undirected graphs.
- Association of arbitrary information to the vertices, edges or even the graph itself, by means of property maps.
- Filter vertices and/or edges "on the fly", such that they appear to have been removed.
- Support for dot, Graph Modelling Language and GraphML formats.
- Convenient and powerful graph drawing based on cairo or Graphviz.
- Support for typical statistical measurements: degree/property histogram, combined degree/property histogram, vertex-vertex correlations, assortativity, average vertex-vertex shortest path, etc.
- Support for several graph-theoretical algorithms: such as graph isomorphism, subgraph isomorphism, minimum spanning tree, connected components, dominator tree, maximum flow, etc.
- Support for several centrality measures.
- Support for clustering coefficients, as well as network motif statistics and community structure detection.
- Generation of random graphs, with arbitrary degree distribution and correlations.
- Support for well-established network models: Price, Barabási-Albert, Geometric Networks, Multidimensional lattice graph, etc.
  
####4.[NetworKit](https://networkit.iti.kit.edu/get_started.html)
[Open Scourse]
- NetworKit is a growing open-source toolkit for large-scale network analysis. Its aim is to provide tools for the analysis of large networks in the size range from thousands to billions of edges. For this purpose, it implements efficient graph algorithms, many of them parallel to utilize multicore architectures. These are meant to compute standard measures of network analysis, such as degree sequences, clustering coefficients, and centrality measures. In this respect, NetworKit is comparable to packages such as NetworkX, albeit with a focus on parallelism and scalability. NetworKit is also a testbed for algorithm engineering and contains novel algorithms from recently published research (see list of Publications).
- NetworKit is a Python module. Performance-aware algorithms are written in C++ (often using OpenMP for shared-memory parallelism) and exposed to Python via the Cython toolchain. Python in turn gives us the ability to work interactively and with a rich environment of tools for data analysis. Furthermore, NetworKit’s core can be built and used as a native library.

####5.[graphviz](http://www.graphviz.org)
[Open Scourse]
- This package facilitates the creation and rendering of graph descriptions in the DOT language of the Graphviz graph drawing software (repo) from Python.
- Create a graph object, assemble the graph by adding nodes and edges, and retrieve its DOT source code string. Save the source code to a file and render it with the Graphviz installation of your system.
- Use the view option/method to directly inspect the resulting (PDF, PNG, SVG, etc.) file with its default application. Graphs can also be rendered and displayed within Jupyter notebooks (a.k.a. IPython notebooks, example).

####6.[metaknowledge](http://networkslab.org/metaknowledge/)
[Open Scourse]
- metaknowledge is a Python3 package for doing computational research in bibliometrics, scientometrics, and network analysis. It can also be easily used to simplify the process of doing systematic reviews in any disciplinary context.

####7.[MuxViz](http://muxviz.net/index.php)
[Open Scourse]
- MuxViz is based on R and GNU Octave.
- MuxViz is a framework for the multilayer analysis and visualization of networks. It allows an interactive visualization and exploration of multilayer networks, i.e., graphs where nodes exhibit multiple relationships simultaneously. It is suitable for the analysis of social networks exhibiting relationships of different type (e.g., family, work, etc) or interactions on different platforms (Twitter, Facebook, etc), biological networks characterized by different type of interactions (e.g., electric, chemical, etc, or allelic, non-allelic, etc), transportation networks consisting of different means of transport (e.g., trains, bus, etc), to cite just some of the possible applications.
  
####8.[Netminer](http://www.netminer.com/main/main-read.do)
[Commercial]
- NetMiner can only be installed only on Microsoft Windows OS

####9.[Gephi](https://gephi.org/features/)
[Open Scourse]
- Language: Java 1.7+
- Probably the most popular network visualization package out there. Gephi doesn't require any programming knowledge. It's strength is that it is able to produce very high quality visualizations. It can also handle relatively large graphs - the actual size will depend on your infrastructure (particularly RAM) but you should be able to go up to 100,000 nodes without a problem. It does have the ability to calculate a few of the more common metrics such as degree, centrality, etc. but it's a stronger tool for visualization than analysis. 
