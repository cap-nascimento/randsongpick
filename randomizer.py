import random

file = open("songs.txt", "r")
links = [line.replace('\n', '') for line in file]
indexes = [x for x in range(len(links))]
file.close()

for i in range(10):
    random.shuffle(indexes)
    
new_links = []

for index in indexes:
    new_links.append(links[index])

file = open("songs.txt", "w")
for link in new_links:
    file.write(link+'\n')
file.close()