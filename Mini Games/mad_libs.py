# Mad Libs --> make a list of words to substitute for each blank in a story before reading aloud.

## Shakespeare's Hamlet

verb1 = input("Verb: ")
adj1 = input("Adjective: ")
verb2 = input("Verb: ")
noun1 = input("Noun (plural): ")
noun2 = input("Noun (plural): ")
adj2 = input("Adjective: ")
noun3 = input("Noun: ")
food = input("Food: ")
verb3 = input("Verb: ")
adj3 = input("Adjective: ")
noun4 = input("Noun: ")


madlib = f"To {verb1}, or not to {verb1},--that is the question:--\
    \nWhether 'tis more {adj1} in the mind to {verb2}\
    \nThe {noun1} and {noun2} of {adj2} fortune\
    \nOr to take {noun3} against a sea of {food},\
    \nAnd by opposing end them?--To die,--to {verb3},--\
    \nNo more; and by a {verb3} to say we end\
    \nThe heartache, and the thousand {adj3} shocks\
    \nThat flesh is heir to,--'tis a {noun4}\
    \nDevoutle to be wish'd."

print(madlib)