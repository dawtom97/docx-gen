

# with open("test.txt","w", encoding="utf8") as file:
#     file.write("8. To jest pierwsza linia \n")
#     file.write("6. druga linia ĄĘŁ")

# with open("test.txt","r", encoding="utf8") as file:
#     for line in file:
#         print(line.strip())

# content = input("Napisz co myślisz: ")
#
# with open("test.txt","a", encoding="utf8") as file:
#     file.write(f"- {content} \n")

with open("test.txt","r+",encoding="utf8") as file:
    lines = file.readlines()
    line = int(input("Podaj linię, którą chcesz odczytać: "))
    update = input("Nowa treść: ")
    lines[line] = update + "\n"
    file.seek(line)
    file.writelines(lines)


