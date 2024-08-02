with open("file1.txt") as file:
    file1=file.readlines()
    file1=[ num.rstrip() for num in file1 if num.rstrip()]
print(file1)

with open("file2.txt") as file:
    file2=file.readlines()
    file2=[ num.rstrip() for num in file2 if num.rstrip() ]
print(file2)

cammon=[num for num in file2 if num in file1]
print(cammon)
