class Room:
    '''The Room class represents a classroom.\n
    Each classroom has an ID (id), a floor (floor), a number of seats (seats) and an area (area).\n
    The area is calculated as double the seats.'''
    id_list: list[str] = []
    def __init__(self, id: str, floor: int, seats: int):

        #Check if the id is unique
        if id in Room.id_list:
            raise ValueError(f"The id you typed (\"{id}\") already exists.\n Ids are unique and should not be repeated")
        else:
            self.__id = id
            Room.id_list.append(id)

        self.__floor = floor
        self.__seats = seats
        self.__area = seats*2
    
    def get_id(self) -> str:
        '''Returns the id of the room.'''
        return self.__id
    
    def get_floor(self) -> int:
        '''Returns the floor of the room.'''
        return self.__floor

    def get_seats(self) -> int:
        '''Returns the number of seats in the room.'''
        return self.__seats

    def get_area(self) -> int:
        '''Returns the area of the room.'''
        return self.__area
    
class Building:
    '''The Building class represents a building.\n
    Each building has a name (name), an address (address), a range of floors (floors), and a list of rooms (rooms).'''
    def __init__(self, name: str, address: str, floors: tuple, rooms: list[Room] = []):
        self.name = name
        self.address = address
        self.floors = floors

        self.__rooms = []
        for r in rooms:
            self.add_room(r)

    def get_floors(self):
        '''Returns the range of floors of the building.'''
        return self.floors

    def get_rooms(self) -> list[Room]:
        '''Returns the list of classrooms of the building'''
        return self.__rooms

    def add_room(self, room: Room) -> None:
        '''Adds a new classroom to the buidling, only if the floor of the classroom is between the range of floors of the building.'''
        if (room.get_floor() >= self.get_floors()[0] and room.get_floor() <= self.get_floors()[1]) and room.get_id() not in [stanza.get_id() for stanza in self.__rooms]:
            self.__rooms.append(room)

    def area(self) -> int:
        '''Returns the area of the building, by adding up the areas of all the classes'''
        tot: int = 0
        for r in self.get_rooms():
            tot += r.get_area()
        return tot