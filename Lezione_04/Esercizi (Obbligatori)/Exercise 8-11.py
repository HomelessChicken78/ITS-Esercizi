'''8-11. Archived Messages: Start with your work from Exercise 8-10.
Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.'''

def send_messages(text: list[str]) -> list[str]:
    sent_messages: list[str] = []
    for i in text:
        print(i)
        sent_messages.append(i)
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