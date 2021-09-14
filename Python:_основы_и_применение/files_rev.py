
with open('dataset_24465_4.txt') as file:
    file_line = file.read().splitlines()

with open('answer.txt', 'w') as new_file:
    for line in file_line[::-1]:
        new_file.write('%s\n' %line)