name =  input("> ").lower()
match name:
    case "iron mike" | "mike" | "kid dynamite" | "the baddest man on the planet" | "mike tyson": print("Michael Gerard Tyson")
    case "mm" | "the blond bombshell" | "marilyn monroe": print("Norma Jeane Mortenson")
    case "buster" | "young jimmy" | "jimi" | "jimi hendrix": print("Johnny Allen Hendrix")
    case _: print("invalid input", name)
