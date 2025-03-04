'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters.
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

glossary: dict[str, str] = {
    "Algorhythm" : "A sequence of steps to be followed in calculations or other problem-solving operations, especially by a computer.",
    "Selection" : " At some point, a program may need to ask a question because it has reached a step where one or more options are available.\n\tDepending on the answer given, the program will follow a certain step and ignore the others.",
    "Iteration" : "Repetition of a mathematical or computational procedure applied to the result of a previous application",
    "Syntax" : "The arrangement of words and phrases to create well-formed sentences in a language.",
    "Code" : "Set of program instructions."
}

for word, meaning in glossary.items():
    print(
        f"{word}: \n\t"
        f"{meaning}\n------------------------------------------------------------------------------------------------------------------------------------------\n"
    )