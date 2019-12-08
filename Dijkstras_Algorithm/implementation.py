from dijkstar import Graph, find_path

# Create Graph
graph = Graph()

# Accept number of floors and flats from user
floors, flats = map(int, input('Enter Floors and Flats separated by space:\n').split())

# Accept each flat as 0 for flats that have stairs and 1 for flats that don't have stairs
flat_list = []
for i in range(floors):
    flat_list.append(list(map(int, input(f'For Floor: {i+1} enter {flats} Flats as:\n0: for flats that have stairs and 1: for flats that don\'t have stairs: ').split())))

# Display list in the order of floors on building
print('Building Architecture\nNote: Floor number and Flat number start with 0 and not 1')
for floor_number, floor in reversed(list(enumerate(flat_list))):
    print(f'Floor {floor_number}: {floor}')

# Accept source and target flat number
src = input('Source Floor and Flat number without any space\nNote: Floor number and Flat number start with 0 and not 1\n')
tgt = input('Target Floor and Flat number without any space\nNote: Floor number and Flat number start with 0 and not 1\n')

# Add Vertices to graph
for floor in range(floors):
    for flat in range(flats):
        # Add Vertices with names as a concatenation of floor_number and flat_number with Edge value as 1 between flats with stairs on each floor and corresponding flats on upper floor
        if flat_list[floor][flat] == 1:
            graph.add_edge(str(floor)+str(flat), str(floor+1)+str(flat), 1)
        # Add Vertices with names as a concatenation of floor_number and flat_number with Edge value as 1 between all Adjacent Flats on each floor
        if flat < flats - 1:
            graph.add_edge(str(floor)+str(flat), str(floor)+str(flat+1), 1)

# print(graph)

# Print Path with its details
print('Shortest Path Details\n', find_path(graph, src, tgt))

'''
To print a particular field (example total cost)
path_details = find_path(graph, src, tgt)
print("Total Cost: ", path_details.total_cost)
'''
