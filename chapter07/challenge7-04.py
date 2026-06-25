li=[1,2,3,4,5]

while True:
    a = input("入力してください:'qで終了'")
    if a=="q":
        break
    try:
        num=int(a)

        if num in li:
            print("正解")
        else:
            print("不正解")

    except ValueError:
        print("数字か'q'を入力してください")

