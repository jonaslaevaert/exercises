def word_count(string):
    if len(string) == 0:
        return 0
    woorden = 1
    for i in range (0, len(string)):
        if string[i] == " ":
            woorden += 1
    return woorden
