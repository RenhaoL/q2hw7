import networkx as nx
from collections import defaultdict

G = nx.DiGraph()
# nx.draw_networkx_nodes(mygraph, node_size=2000, )
G.add_edge('Start', 'Seattle', weight=0)
G.add_edges_from([('Start', 'Newport', {'weight': 0}), ('Start', 'San Francisco', {'weight': 0}), ('Start', 'USC', {'weight': 0})])


G.add_edge('Seattle', 'Boise', weight=494)
G.add_edge('Newport', 'Boise', weight=561)
G.add_edge('San Francisco', 'Boise', weight=648)
G.add_edge('San Francisco', 'Salt Lake', weight=748)
G.add_edge('San Francisco', 'Las Vegas', weight=630)
G.add_edge('USC', 'Las Vegas', weight=275)
G.add_edge('USC', 'Tucson', weight=528)

#day 2
G.add_edge('Boise', 'Casper', weight=669)
G.add_edge('Salt Lake', 'Casper', weight=402)
G.add_edge('Salt Lake', 'Denver', weight=493)
G.add_edge('Salt Lake', 'Albuquerque', weight=609)
G.add_edge('Las Vegas', 'Albuquerque', weight=576)
G.add_edge('Las Vegas', 'El Paso', weight=724)
G.add_edge('Tucson', 'Albuquerque', weight=452)
G.add_edge('Tucson', 'El Paso', weight=320)

#day 3
G.add_edge('Casper', 'Pierre', weight=347)
G.add_edge('Casper', 'Lincoln', weight=635)
G.add_edge('Casper', 'Amarillo', weight=705)
G.add_edge('Denver', 'Pierre', weight=526)
G.add_edge('Denver', 'Lincoln', weight=667)
G.add_edge('Denver', 'Amarillo', weight=424)
G.add_edge('Albuquerque', 'Amarillo', weight=288)
G.add_edge('Albuquerque', 'San Antonio', weight=199)
G.add_edge('El Paso', 'Amarillo', weight=421)
G.add_edge('El Paso', 'San Antonio', weight=555)

#day 4
G.add_edge('Pierre', 'Minneapolis', weight=478)
G.add_edge('Pierre', 'Kansas City', weight=598)
G.add_edge('Lincoln', 'Minneapolis', weight=438)
G.add_edge('Lincoln', 'Kansas City', weight=207)
G.add_edge('Lincoln', 'Ft. Smith', weight=567)
G.add_edge('Amarillo', 'Kansas City', weight=613)
G.add_edge('Amarillo', 'Ft. Smith', weight=539)
G.add_edge('Amarillo', 'Houston', weight=614)
G.add_edge('San Antonio', 'Houston', weight=199)

#day 5
G.add_edge('Minneapolis', 'Chicago', weight=465)
G.add_edge('Minneapolis', 'St. Louis', weight=593)
G.add_edge('Kansas City', 'Chicago', weight=527)
G.add_edge('Kansas City', 'St. Louis', weight=256)
G.add_edge('Kansas City', 'Nashville', weight=618)
G.add_edge('Ft. Smith', 'St. Louis', weight=545)
G.add_edge('Ft. Smith', 'Nashville', weight=501)
G.add_edge('Ft. Smith', 'New Orleans', weight=601)
G.add_edge('Houston', 'New Orleans', weight=352)

#day 6
G.add_edge('Chicago', 'Pittsburg', weight=532)
G.add_edge('Chicago', 'Roanoke', weight=717)
G.add_edge('St. Louis', 'Pittsburg', weight=659)
G.add_edge('St. Louis', 'Roanoke', weight=689)
G.add_edge('Nashville', 'Roanoke', weight=435)
G.add_edge('Nashville', 'Charlotte', weight=434)
G.add_edge('Nashville', 'Talluhassee', weight=495)
G.add_edge('New Orleans', 'Charlotte', weight=725)
G.add_edge('New Orleans', 'Talluhassee', weight=388)

#day 7
G.add_edge('Pittsburg', 'MIT', weight=680)
G.add_edge('Pittsburg', 'Washington', weight=259)
G.add_edge('Roanoke', 'MIT', weight=750)
G.add_edge('Roanoke', 'Washington', weight=233)
G.add_edge('Roanoke', 'Wilmington', weight=306)
G.add_edge('Roanoke', 'Daytona Beach', weight=480)
G.add_edge('Charlotte', 'Washington', weight=397)
G.add_edge('Charlotte', 'Wilmington', weight=206)
G.add_edge('Charlotte', 'Daytona Beach', weight=480)
G.add_edge('Talluhassee', 'Wilmington', weight=496)
G.add_edge('Talluhassee', 'Daytona Beach', weight=316)


#end nodes
G.add_edge('MIT', 'End', weight=0)
G.add_edge('Washington', 'End', weight=0)
G.add_edge('Wilmington', 'End', weight=0)
G.add_edge('Daytona Beach', 'End', weight=0)

# Calculate the shortest route and distance

def inital_shortest_dis(start_point='Start'):
    """
    return the shortest distance out of all possible paths in day 1 and day2
    i.e. {'Boise': {'Seattle': 494}, 'Salt Lake': {'San Francisco': 748}, 'Las Vegas': {'USC': 275}, 'Tucson': {'USC': 528}})
    meaning, the shortest distance in all path from Seattle is that from seattle to boise
    """
    start_node = G.__getitem__(start_point)
    dis_dict = defaultdict(dict) # contain all possible paths with distance
    shortest_path = defaultdict(dict) # calculate the shortest, and return the result. key is the arriving city and in value, key is the previous city and value is the shortest distance.
    for k, v in start_node.items():
        next_edge = G.__getitem__(k)
        for city, mile in next_edge.items():
            dis_dict[city][k] = v['weight'] + mile['weight']

    for k, v in dis_dict.items():
        distance = []
        for k1, v1 in v.items():
            distance.append((k1, v1))
        target = min(distance, key = lambda x: x[1])
        shortest_path[k][target[0]] = target[1]
    return shortest_path


def short_distance(previous:dict):
    """
    Return a dictionary with the shortest distance between adjacent days and cities.
    """
    dis_dict = defaultdict(dict) # all the possible paths
    for k, v in previous.items():
        next_edge = G.__getitem__(k)
        for k1, v1 in v.items():
            for new_city, new_mile in next_edge.items():
                dis_dict[new_city][k] = v1 + new_mile['weight']

    shortest_dis = defaultdict(dict) # select the shortest path.
    for k, v in dis_dict.items():
        distance = []
        for k1, v1 in v.items():
            distance.append((k1, v1))
        target = min(distance, key = lambda x: x[1])
        shortest_dis[k][target[0]]=target[1]
    return shortest_dis

d12 = inital_shortest_dis()
# print(d12)
day3 = short_distance(d12)
# print(day3)
day4 = short_distance(day3)
# print(day4)
day5 = short_distance(day4)
# print(day5)
day6 = short_distance(day5)
# print(day6)
day7 = short_distance(day6)
# print(day7)
end = short_distance(day7)
# print(end)

trip = [day7, day6, day5, day4, day3, d12]


def final_node(destination):
    '''
    deal with the final node and return a list with the last 2 cities on the shortest route
    '''
    track_back = []
    total_dis = []
    for k, v in end.items():
        for k1, v1 in v.items():
            total_dis.append((k, k1, v1))
    min_dis = min(total_dis, key = lambda x: x[-1])
    track_back.append(min_dis[0])
    track_back.append(min_dis[1])
    return track_back, min_dis[-1]

def extract_cities(target_city, pool):
    '''
    This is a helper function
    return a city name on the shortest route. Used later in a for loop to return the list of all the cities on the route.
    '''
    result = []
    for k, v in pool.items():
        if k == target_city:
            for k1, v1 in v.items():
                result.append(k1)
    return result

final_route, final_dis = final_node(end)

for i in trip:
    final_route.extend(extract_cities(final_route[-1], i))

final_route = final_route[::-1] # the final list of the cities' names on the shortest route from west coast to east coast


print('The shortest route from west coast to east coast is: ')
print(' -> '.join(i for i in final_route))
print('The shortest distance is: {:4d} miles'.format(final_dis))

