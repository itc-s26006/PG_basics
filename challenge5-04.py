kanato = {
       "名前":"玉城かなと",
        "趣味":"ゲーム",
        "身長":"160",

}
print(kanato)
#調べたい特徴を尋ねる
ask=input("特徴を入力してください")
if ask in kanato:#if ask in kanato:もし、入力された言葉（ask）が、かなとさんのプロフィール帳の見出し（キー）にあるなら、という意味です。
   
   answer=kanato[ask]   #ある場合：kanato[ask] でその見出しの中身（値）を取り出して、画面に表示します。
    print(answer)
else:
    print("それはわかりません")
    
