cleanfile = []
try:
    #employees tekst is opnened and pythong gets read priviledges while being able to read a danish keyboard
    with open("employees.txt", "r", encoding="utf-8") as employees:

        #read everyline and turn it into a list
        content = employees.readlines()

        #each line in the list gets \n removed and splits the line into another list with \t deciding when the next data begins
        for line in content:
            line = line.strip("\n")
            line = line.split("\t")
            cleanfile.append(line)

    #printing it nicely
    for person in cleanfile:
        print(f"firstname: {person[0]}\n"
              f"lastname: {person[1]}\n"
              f"role: {person[2]}\n"
              f"years of experience: {person[3]}\n\n")
    print(f"total employees{len(cleanfile)}")

#if the file isnt there it will tell the user
except FileNotFoundError:
    print("employees.txt not found")