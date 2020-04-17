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
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

# Start by writing an algorithm that picks a random unexplored direction from the player's current room,
# travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal.
# When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does
# contain an unexplored path.

# Pseudo-Code
# Initialization Process
# get the current room - 0
# starting_room = player.current_room.id
# # get the exits for current room - {n, s, w, e}
# # starting_exits = player.current_room.get_exits()

# # add to visited
# # should look like this:
# # {0: {n: '?', s: '?', w: '?', e: '?'}
# visited = {}
# # visited[starting_room] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# # print(visited)
# # Initialize Stack
# stack = Stack()
# # prev_room = None
# stack.push(starting_room)

# stack push first room --> 0
# (direction = 0, prev_room = None)
# stack = [direction = None, prev_room = None]
# stack.append(starting_room)
# print(stack)
# Start DFT mode
# while len(visited) < len(room_graph):
#     current_room = player.current_room.id
# # room info = stack pop
# # prev room = get room info
# # get the current room exits from visited

# # check if current room is in visited
#     if current_room not in visited:
#         # if not, add to visited
#         exits = player.current_room.get_exits()
#         visited[current_room] = exits
# # should look like this:
# # {current room: {fill in exit --> n: '?', s: '?', w: '?', e: '?'}
#         for exit in exits:
#             stack.push(exit)
#             player.travel(exit)

# (this should fail on 1st iteration)
# if previous room is not None:
# this is where we update our previous room
# visited[prev_room][direction] = current_room

# (this should fail on 1st iteration)
# update current room exits if we have a direction
# direction is not None
# visited[current room][reverse direction] = prev room

# loop unvisited exits or maybe all exits?
# move in that direction
# update traversal path --> direction
# update the stack --> (direction, current room)

# if there are no exits that are unvisited
# enter into BFs mode using visited graph
# the destination is a room with a question mark
# building a path to traverse after finding the destination


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
