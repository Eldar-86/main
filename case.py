name =  input("").capitalize()
match name:
    case "Iron Mike" | "Mike" | "Kid Dynamite" | "The Baddest Man On The Planet" | "Mike Tyson": print("Michael Gerard Tyson")
    case "Mm" | "The Blond Bombshell" | "Marilyn Monroe": print("Norma Jeane Mortenson")
    case "Buster" | "Young Jimmy" | "Jimi" | "Jimi Hendrix": print("Johnny Allen Hendrix")
    case _: print("invalid input")
