import random


class TraversalGraph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, new_room, exits):
        self.rooms[new_room] = {}
        for exit in exits:
            self.rooms[new_room][exit] = '?'

    def add_connection(self, new_room, previous_room, direction, reverse_direction):
        self.rooms[previous_room][direction] = new_room
        if self.rooms[new_room][reverse_direction]:
            self.rooms[new_room][reverse_direction] = previous_room

    def explore_direction(self, current_room, exits):
        # find the next unexplored direction (?)
        random.shuffle(exits)
        for direction in exits:
            if self.rooms[current_room][direction] == '?':
                return direction

    def get_connections(self, room):
        if room in self.rooms:
            return self.rooms[room]
        else:
            return None

    # not finished.... supposed to return the longest loop possible
    def longest_dft(self, starting_room):
        visited = set()
        stack = []
        stack.append([starting_room])
        print('Stack: ', stack)
        longest_path = [starting_room]

        while len(stack) > 0:
            path = stack.pop()
            room = path[-1]
            if room not in visited:
                if len(path) > len(longest_path):
                    longest_path = path
                elif len(path) == len(longest_path):
                    if path[-1] < longest_path[-1]:
                        longest_path = path
                visited.add(room)
                print('Visited: ', visited)
                adjacent_rooms = self.get_connections(room)
                print('Adjacent Rooms: ', adjacent_rooms)
                for next_room in adjacent_rooms:
                    new_path = list(path)
                    new_path.append(adjacent_rooms[next_room])
                    stack.append(new_path)

        return longest_path

    def bfs(self, starting_room, target):
        pass
