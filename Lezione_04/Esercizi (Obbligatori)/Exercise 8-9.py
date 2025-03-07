'''8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.'''

def show_messages(text: list[str]) -> None:
    for i in text:
        print(i)

text: list[str] = [
    "hello there!",
    "I love pizza",
    "functions are cool",
    "ICT ITS Academy",
    "Rainbow dash",
    "The cake is a lie",
    "How did we get here?"
    ]
show_messages(text)