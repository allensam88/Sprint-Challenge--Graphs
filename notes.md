Player starts in the room --> initially 0
Look for open doors --> exits / directions
	Can I go N or S or where ever?


add current room to visited, then travel to next available exit
player.current_room.get_exits() --> to find all available exits
this will show both N and S exits
assign direction traveled to point toward prev_room
player.travel('n') --> go to room 1

Stack Accounting
start at 0

move 'n' to 1
stack = ['s']
update visited
check for exits

move 'n' to 2
stack = ['s', 's']
update visited with room vertex and direction/exit pointers
check for exits
hit dead end only see exit to prev room

retrace the stack path
pop --> move

now we are back at room zero... original intersection, after reaching dead end 2, now what?

check for exits




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