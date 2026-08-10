def concatenate(s1: str, s2: str) -> str:
    pass
    my = s1+s2
    if len(my)>10:
        return "Too long!"
    else:
        return my


# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
