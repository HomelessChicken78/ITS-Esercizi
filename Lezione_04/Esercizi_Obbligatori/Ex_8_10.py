'''8-10. Sending Messages:
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

def send_messages(text: list[str]) -> list[str]:
    sent_messages: list[str] = []
    original: list[str] = text[:]
    for i in original:
        print(i)
        sent_messages.append(i)
        text.remove(i)
    return sent_messages

text: list[str] = [
    "hello there!",
    "I love pizza",
    "functions are cool",
    "ICT ITS Academy",
    "Rainbow dash",
    "The cake is a lie",
    "How did we get here?"
    ]
sent_messages:list[str] = send_messages(text)
print("Here are both the lists:\ntext:\t\t",text, "\nsent_messages:\t", sent_messages)