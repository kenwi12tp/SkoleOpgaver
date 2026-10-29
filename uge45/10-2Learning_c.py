lines = []
with open("python.txt","r") as file:
    for line in file:
        line = line.replace("loops", "python")
        lines.append(line)
with open("python.txt","w") as file:
    file.writelines(lines)