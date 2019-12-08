from dijkstar import Graph, find_path

graph = Graph()

floors, flats = map(int, input('Enter Floors and Flats separated by space:\n').split())

flat_list = []
for i in range(floors):
    flat_list.append(list(map(int, input(f'For Floor: {i+1} enter {flats} Flats as:\n0: for flats that have stairs and 1: for flats that don\'t have stairs: ').split())))

print('Building Architecture\nNote: Floor number and Flat number start with 0 and not 1')

for floor in reversed(flat_list):
    print(f'Floor {flat_list.index(floor)}: {floor}')


src = input('Source Floor and Flat number without any space\nNote: Floor number and Flat number start with 0 and not 1\n')
tgt = input('Target Floor and Flat number without any space\nNote: Floor number and Flat number start with 0 and not 1\n')

for floor in range(floors):
    for flat in range(flats):
        if flat_list[floor][flat] == 1:
            graph.add_edge(str(floor)+str(flat), str(floor+1)+str(flat), 1)
        if flat < flats - 1:
            graph.add_edge(str(floor)+str(flat), str(floor)+str(flat+1), 1)

# print(graph)

print('Shortest Path Details\n', find_path(graph, src, tgt))
