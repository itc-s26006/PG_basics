def vv(s):
    try:
        return float(s)
    except(ValueError):
        print("数字ではないので処理中止")
    f=vv("")
    print(f)


