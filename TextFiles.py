# 2 text files exists. Create the third file with the copies of the strings that exists in the first file and doesn't
# exist in the second file.

first_lines = []
second_lines = []
third_lines = []
first = open('first.txt')
second = open('second.txt')
for line in first:
    first_lines.append(line)
for line in second:
    second_lines.append(line)
first.close()
second.close()
# First method
#for line in first_lines:
#    if not (line in second_lines):
#        third_lines.append(line)
# Second method
third_lines = sorted(set(first_lines) - set(second_lines))

third = open('third.txt','w')
for line in third_lines:
    third.write(line)
third.close()
print(third_lines)