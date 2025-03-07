'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.'''

def make_album(artist: str, album: str, number: int = None) -> str:
    info: dict = {
        "artist" : artist,
        "album" : album
        }
    if number is None:
        info["number of songs"] = 0
    else:
        info["number of songs"] = number
    return info

artists: list[str] = []
albums: list[str] = []
infos: list[dict[str, str]] = []
i: int = 0
while i < 3:
    artists.append(input("Insert an artist:\n>\t"))
    albums.append(input("Insert an album:\n>\t"))
    infos.append(make_album(artists[i], albums[i]))
    i += 1

for i in infos:
    for k, v in i.items():
        print(f"{k} : {v}")
    print("")