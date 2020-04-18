from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = ['n', 'n', 's', 's', 's', 's',
#                   'n', 'n', 'e', 'e', 'w', 'w', 'w', 'w']
# traversal_path = ['s', 's', 'w', 'w', 'n', 'n', 'e', 'e', 'e', 'e',
#                   'w', 'w', 'n', 'n', 's', 'e', 'e', 'n', 's', 'w', 'w', 'w', 'w', 'n']
traversal_path = []

# Allows the user to backtrack and retrace traversal path in opposite direction
reversal_path = [None]
reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Log will keep track of rooms with unexplored exits
log = {}
# Initialize the starting room
log[player.current_room.id] = player.current_room.get_exits()

while len(log) < len(room_graph):
    current_room = player.current_room.id
    exits = player.current_room.get_exits()
    reverse_direction = reversal_path[-1]

    print('-----------------------------------------------------------------------------------------')
    print('Log: ', log)
    print('Current Room: ', current_room)
    print('Unexplored Exits: ', exits)

    # if player hasn't visited the room yet...
    if current_room not in log:
        # add the room and its exits
        log[current_room] = exits
        # if the player already explored that direction...
        if reverse_direction:
            print(f'Already explored: {reverse_direction}')
            # then remove that exit option
            exits.remove(reverse_direction)

    # if player has already visited a room, but it has unexplored exits in the log...
    elif len(log[current_room]) > 0:
        # move in another unexplored direction
        direction = log[current_room].pop()
        player.travel(direction)
        # update traversal and reversal paths
        traversal_path.append(direction)
        reversal_path.append(reverse[direction])

        print('Travel Direction: ', direction)
        print('Traversal Path: ', traversal_path)
        print('Reversal Path: ', reversal_path)
        print('New Room: ', player.current_room.id)

    # if a player has visited a room and all exits have been explored in the log...
    elif len(log[current_room]) == 0:
        # retrace the path in reverse
        direction = reversal_path.pop()
        player.travel(direction)
        traversal_path.append(direction)

        print('Travel Reverse Direction: ', direction)
        print('Traversal Path: ', traversal_path)
        print('Reversal Path: ', reversal_path)
        print('New Room: ', player.current_room.id)


# --- OLD APPROACH ---
# trying too hard to make use of question marks
# visited = {}

# while len(visited) < len(room_graph):
    # current_room = player.current_room.id
    # exits = player.current_room.get_exits()

    # for exit in exits:
    #     if exit not in visited[current_room]:
    #         visited[current_room][exit] = '?'

    # direction = exits[-1]
    # print(visited)
    # if visited[current_room][direction] == '?':
    #     previous_room = current_room

    #     player.travel(direction)
    #     traversal_path.append(direction)

    #     new_room = player.current_room.id

    #     visited[previous_room][direction] = new_room
    #     if new_room not in visited:
    #         visited[new_room] = {}
    #     visited[new_room][reverse[direction]] = previous_room

    # if visited[current_room][direction] != '?':
    #     break

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    # for room in visited_rooms:
    #     print(room.id)
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
