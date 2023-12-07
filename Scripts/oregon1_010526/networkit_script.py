from datetime import datetime
import networkit as nk
import time
import json


if __name__ == "__main__":
    filename = '../../Data/oregon1_010526.txt'
    current_datetime = datetime.now()
    current_date_string = current_datetime.strftime("%d-%m-%Y")

    try:
        G = nk.readGraph(filename, nk.Format.EdgeListTabZero, directed=False)
    except:
        try:
            G = nk.readGraph(
                filename, nk.Format.EdgeListSpaceZero, directed=False)
        except:
            print("Wrong format")
            exit(1)

    # "Geisberger" approach:
    for i in range(0, 10):
        start_time_geisberger = time.time()
        betweenness = nk.centrality.EstimateBetweenness(G, 50, True, False)
        betweenness.run()
        end_time_geisberger = time.time()

        # Write exact betweenness to file:
        path = f"NetworKit_Results/{current_date_string}_networkit_geisberger_{str(i)}.json"
        with open(path, 'w') as json_file:
            json.dump(dict(betweenness.ranking()), json_file,
                      indent=2, sort_keys=True)

         # Output statistics
        printLine = 'Approximation_Geisberger_NetworKit_,' + filename + ',' +\
            str(end_time_geisberger - start_time_geisberger) + ',' + path + '\n'
        with open('networkit_output.log', 'a') as file:
            file.write(printLine)
    exit(0)

    print("--- Geisberger approach --- ")
    print('Betweenness centrality ranked', betweenness.ranking())
    print("Total execution time: %s seconds " % (time.time() - start_time))

    # "Riondato" approach:
    start_time = time.time()
    betweenness_riondato = nk.centrality.ApproxBetweenness(G,
                                                           epsilon=0.1,
                                                           delta=0.1,
                                                           universalConstant=0.5)
    betweenness_riondato.run()
    print("--- Riondato approach --- ")
    print('Betweenness centrality ranked', betweenness_riondato.ranking())
    print("Total execution time: %s seconds " % (time.time() - start_time))

    # Van der Grinten A., Angriman E., and Meyerhenke H. (2019) approach of Kadabra algorithm
    start_time = time.time()
    kadabra = nk.centrality.KadabraBetweenness(
        G, 0.05, 0.8)  # these are the default settings
    kadabra.run()
    print("--- Kadabra approach --- ")
    print('Kadabra centrality ranked', kadabra.ranking())
    print("Total execution time: %s seconds " % (time.time() - start_time))

    # "Bergamini and Meyerhenke" approach:
    start_time = time.time()
    betweenness_bergamini = nk.centrality.DynApproxBetweenness(
        G, epsilon=0.2, delta=0.1, storePredecessors=True, universalConstant=0.5)
    print("test")
    print(betweenness_bergamini.getNumberOfSamples())
    betweenness_bergamini.run()
    print("--- Bergamini approach --- ")
    print('Betweenness centrality ranked', betweenness_bergamini.ranking())
    print("Total execution time: %s seconds " % (time.time() - start_time))
