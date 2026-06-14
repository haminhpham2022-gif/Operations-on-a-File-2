import os

with open('file1.txt', 'w') as f:
    data = "to do list: \ndo the laundry \nclean my room \ndo the dishes \nmow the lawn"
    f.write(data)

with open('file2.txt', 'w') as f:
    data = "homework: \nenglish workbook p.13 \nmaths worksheet \nphysics presentation due tomorrow"
    f.write(data)

if os.path.exists('file1.txt') and os.path.exists("file2.txt"):
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
        data1 = f1.read()
        data2 = f2.read()
        f3.write(f"{data1} \n{data2}")
    print('file merged successfully')
else:
    print('one or both files do not exist')