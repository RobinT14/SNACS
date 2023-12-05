# Social Network Analysis for Computer Scientists - Code

By Roos Wensveen & Robin The

The following repository contains all code as presented in our paper. This code is used for the several experiments that have been performed in order to exactly determine/approximate betweenness centrality.

## Files/Folders:

- experiment.py: script to perform betweenness centrality calculation/approximation using all of our created methods.
- Data: contains all datasets that are used within our paper

### experiment.py:

Usage of the script as follows:

```
usage: experiment.py [-h] [-d DIRECTED] input_file

This script will perform exact calculation and approximation of betweenness
centrality, and will present the statistics of this.

positional arguments:
input_file Path to the input file, of a give graph

optional arguments:
-h, --help show this help message and exit
-d DIRECTED, --directed DIRECTED
Set input graph type to directed graph. True OR False,
Default=False

```

This script will perform our experiment consisting of the following steps:

1. Exact calculation of betweenness centrality using NetworkX, Brandes implementation.
2. Approximation of betweenness centrality using NetworkX, Brandes implementation, with sampling/pivoting
   - Sample size of 60/80% of number of nodes.
3. Approximation of betweenness centrality using NetworKit,

### Data:

- Undirected graph: oregon1_010526.txt
  - Nodes: 11174 Edges: 23409

### Dependencies

- rich
- networkx
- networkit
