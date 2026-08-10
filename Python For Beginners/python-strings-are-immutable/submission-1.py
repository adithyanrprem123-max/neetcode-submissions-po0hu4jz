def remove_fourth_character(word: str) -> str:
    pass
    a = word[0:3]
    b = word[4:len(word)]
    c= a + b
    return c
# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
