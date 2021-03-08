
fileName = input("파일 이름을 입력하세요:")

f = open(fileName)

t = f.read()
word = t.split()

print(t)
print("단어의 갯수: ", len(word))
print("문자 수: ", len(t))
print("행의 수: ", len(t.split('\n')))
f.close()