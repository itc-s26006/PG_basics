kanato = {
    "名前": "玉城かなと",
    "趣味": "ゲーム",
    "身長": "160",
}

print(kanato)

# 調べたい特徴を尋ねる
ask = input("特徴を入力してください（例：名前、趣味、身長）：")

# もし、入力された言葉（ask）が、かなとさんのプロフィール帳の見出し（キー）にあるなら
if ask in kanato:
    # ある場合：kanato[ask] でその見出しの中身（値）を取り出して、画面に表示します。
    answer = kanato[ask]
    print(answer)
else:
    print("それはわかりません")
