a=input("type a number:")
b=input("type another:")
a=int (a)
b=int(b)
try:
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("文字とゼロ以外の数字を入れてください")

