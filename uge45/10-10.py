with open("book.txt","r", encoding="utf-8") as book:
    count = 0
    for line in book:
        count += line.count("the")
print(count)