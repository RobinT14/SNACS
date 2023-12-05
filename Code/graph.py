import networkx as nx
import time
import math
# import networkit as nk


from rich.table import Table


def read_file(filename, diGraph=True):
    if diGraph:
        G = nx.read_edgelist(filename,
                             nodetype=int,
                             create_using=nx.DiGraph,
                             data=(("weight", float), ))
    else:
        G = nx.read_edgelist(filename,
                             nodetype=int,
                             create_using=nx.Graph,
                             data=(("weight", float), ))
    return G


def print_graph_stats(console, input_file, graph):
    table = Table(title="Graph Statistics")
    table.add_column("Graph File", justify="left", style="cyan")
    table.add_column(f"{str(input_file)}", justify="left", style="green")
    table.add_row("Directed", str(nx.is_directed(graph)))
    table.add_row("No Nodes", str(nx.number_of_nodes(graph)))
    table.add_row("No Edges", str(nx.number_of_edges(graph)))
    console.print(table)
    console.print("\n")


def perform_experiments(console, graph, input_file):
    table = Table(title="Experimental Results - Betweenness Centrality")
    table.add_column("Type", justify="left", style="cyan")
    table.add_column("Execution Time(s)", justify="left", style="green")

    # !Exact calculation of betweenness centrality using Brandes in NetworkX
    start_time_exact = time.time()
    # betweenness = nx.betweenness_centrality(graph)
    end_time_exact = time.time()
    # TODO Write Exact To File
    table.add_row("Exact - Brandes NetworkX",
                  str(end_time_exact - start_time_exact))

    # !Approximation of betweenness using sampling/pivotting in NetworkX:
    table.add_row("Approximation using sampling - Brandes/NetworkX")
    samples = [60, 80]  # TODO Add more sample percentages if wanted?
    for sample in samples:
        sampleSize = math.floor(len(graph.nodes) * (sample/100))
        average_time = 0
        for i in range(0, 10):
            # !Approximation of betweenness
            start_time_approx = time.time()
            # betweenness_approx = nx.betweenness_centrality(graph, k=sampleSize)
            end_time_approx = time.time()
            average_time += (end_time_approx - start_time_approx)
            # TODO Add if all output is wanted
            # table.add_row(f"\t {sample}% sampled, run {i}",
            #               str(end_time_approx - start_time_approx))
        average_time /= 10
        table.add_row(f"\t {sample}% sampled, average of 10 runs",
                      str(end_time_approx - start_time_approx))

    # !Approximation of betweenness using networkit:

    console.print(table)
    console.print("\n")
