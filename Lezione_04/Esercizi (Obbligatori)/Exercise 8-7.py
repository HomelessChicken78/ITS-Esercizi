'''8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title,
and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.'''

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

for k, v in (make_album("Red hot Chili Peppers", "Californication", 20)).items():
    print(f"{k} : {v}")
print("\n----------------\n")

for k, v in (make_album("Periphery", "Periphery 2 This is personal", 12)).items():
    print(f"{k} : {v}")
print("\n----------------\n")

for k, v in (make_album("Tesseract", "War of being")).items():
    print(f"{k} : {v}")
print("\n----------------\n")