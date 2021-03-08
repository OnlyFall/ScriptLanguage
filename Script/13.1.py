f = open("test.txt", "w")
f.write("morning kpu game morning\n morning entertainment\n morning")
f.close()

fileName = input("파일 이름 입력: ")
f = open(fileName)
s = input("제거할 단어 입력: ")

content = f.read()


print(content)
f.close()

f = open(fileName, "w")
f.write(content.replace(s, ""))
f.close()