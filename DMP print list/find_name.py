import os
listOfA = []
for root, dirs, files in os.walk("C:/Users/Varun Kharkwal/Desktop/Programmer's Space/Python with Varun Kharkwal/08_AUGUST_P\DMP sheets - VKbrawler", topdown=False):
    for name in dirs:
        with open(f"DMP sheets - VKbrawler/{name}/1.c") as f:
            content = f.read()
            # locA = content.find("Section- A")
            locB = content.find("Section- B")
            if locB!= -1:
                listOfA.append(name)

with open("Section B.txt", 'a') as f:
    for i in range(len(listOfA)):
        f.write(listOfA[i] + "\n")