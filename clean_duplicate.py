import re

content = open('blue-team-generated-1.txt', 'r').readlines()

content_set = set(content)

clean = open('blue-team-generated-clean.txt', 'w')

for line in content_set:
    clean.write(line)