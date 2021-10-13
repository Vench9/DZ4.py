import pydoc

a = 'London is a capital of great Britan'
print(a[0])
print(a[-1])
print(a[2])
print(a[-3])
print(len(a))
b = 'astrobiology'
print(b[0:8])
print(b[4:8])
print(b[::3])
b = 'astrobiology'[::-1]
print(b)
x = "my name is name"
y = "Vanya"
print("my name is {name}".format(name=y,))
test_tring = "Hello world "
print("Местоположение буквы 'w':", test_tring.find("w"))
start = -1
count = 0
while True:
    start = test_tring.find("l", start+1)
    if start == -1:
        break
    count += 1
print("Количество букв l : ", count )
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))


