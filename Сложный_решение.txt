word =open('24(1).txt').readline().strip()
word.lower()
index_map = []
for i in range(len(word)):
    if word[i] != word[i-1]:
        index_map.append(word[i])
    
    
transitions = 0
for i in range(len(index_map) - 1):
    if ord(index_map[i+1]) == ord(index_map[i]) + 1:
        transitions += 1

print(transitions)
