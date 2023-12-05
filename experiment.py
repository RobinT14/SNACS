# This script contains the code as presented in course paper: 'A novel study of
# “Fast approximation of betweenness centrality through sampling”'.
#
# This script will perform the follwing:
# - Exact calculation of betweenness centrality.
#
# Created by Roos Wensveen & Robin The

import argparse
import os
from Code.format import print_header
from Code.graph import read_file, print_graph_stats
from Code.betweenness import perform_experiments
from rich.console import Console

# from time import sleep
# from rich.progress import track
# def process_data():
#     sleep(0.02)
# for _ in track(range(100), description='[green]Processing data'):
#     process_data()


def main():
    parser = argparse.ArgumentParser(
        description='This script will perform exact calculation and approximation of betweenness centrality, and will present the statistics of this.')

    parser.add_argument(
        'input_file', help='Path to the input file, of a give graph')

    # Add optional argument
    # parser.add_argument(
    #     '-o', '--output', help='Write statistics to output file(CSV).')
    parser.add_argument(
        '-d', '--directed', help='Set input graph type to directed graph. True OR False, Default=False')

    args = parser.parse_args()

    # Arguments:
    input_file = args.input_file
    # output_file = args.output
    directed = True
    if args.directed is not None:
        if args.directed == "True":
            directed = True
        elif args.directed == "False":
            directed = False
        else:
            console.print(
                f"[bold red]Error: Command Line Argument '-d', '--directed' shoud be True or False.[/bold red]\n")
            exit(1)

    if os.path.isfile(input_file):
        console.print(
            f"[bold green]Reading graph from input file: '{input_file}'[/bold green]\n")
    else:
        console.print(
            f"[bold red]Error: Input file - '{input_file}' does not exist.[/bold red]\n")
        exit(1)

    graph = read_file(input_file, console, directed)
    print_graph_stats(console, input_file, graph)

    perform_experiments(console, graph, input_file)


if __name__ == "__main__":
    console = Console()
    print_header(console)
    main()
