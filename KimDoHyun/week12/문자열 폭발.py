import sys
sentence=sys.stdin.readline().rstrip()
bomb=sys.stdin.readline().rstrip()
bomb_len=len(bomb)
stack=[]
for i in range(len(sentence)):
    stack.append(sentence[i])
    if ''.join(stack[-bomb_len:])==bomb:
        for j in range(bomb_len):stack.pop()


if stack:print(''.join(stack))
else:print("FRULA")