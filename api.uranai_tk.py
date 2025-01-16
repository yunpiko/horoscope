"""
ボタンを押したときの動き

・占い結果を取得する  関数名:get_uranai
・今あるボタンを消す  関数名:clear_btn
※tkinter画面上からオブジェクトを消すのはdestroy()を使う
・占い結果を表示する  関数名:view_uranai
・戻るボタンを表示する  関数名:make_return
・スタート画面に戻る  関数名:back_main
"""

import tkinter as tk
import requests
import json
from datetime import date

#画面作成
root = tk.Tk()
root.title("占い")
root.minsize(250,330)

# 関数たち
# 占い結果を取得する関数を作る
def get_uranai(num):
    """引数で受け取った星座の結果を辞書型で取得してprintする関数"""
    # 今日の日付を取得(yyyy-mm-'dd)
    today = str(date.today()).replace("-","/")
    res = requests.get(f"https://api.jugemkey.jp/api/horoscope/free/{today}")
    result = json.loads(res.text)
    # print(result['horoscope'][today][num])
    view_uranai(result['horoscope'][today][num])


# ボタンを作る関数
def make_btn():
    global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11,btn_12,btn_list

    # 一段目
    btn_1 = tk.Button(text="牡羊座",font=("游ゴシック",10))
    btn_1.bind("<1>",lambda event:clear_btn(event,0)) # ここでラムダ式
    btn_1.place(x=70,y=70)

    btn_2 = tk.Button(text="牡牛座",font=("游ゴシック",10))
    btn_2.bind("<1>",lambda event:clear_btn(event,1))
    btn_2.place(x=130,y=70)

    # 二段目
    btn_3= tk.Button(text="双子座",font=("游ゴシック",10))
    btn_3.bind("<1>",lambda event:clear_btn(event,2))
    btn_3.place(x=70,y=110)

    btn_4= tk.Button(text="蟹座",font=("游ゴシック",10))
    btn_4.bind("<1>",lambda event:clear_btn(event,3))
    btn_4.place(x=130,y=110)

    # 三段目
    btn_5 = tk.Button(text="獅子座",font=("游ゴシック",10))
    btn_5.bind("<1>",lambda event:clear_btn(event,4))
    btn_5.place(x=70,y=150)

    btn_6 = tk.Button(text="乙女座",font=("游ゴシック",10))
    btn_6.bind("<1>",lambda event:clear_btn(event,5)) 
    btn_6.place(x=130,y=150)

    # 四段目
    btn_7 = tk.Button(text="天秤座",font=("游ゴシック",10))
    btn_7.bind("<1>",lambda event:clear_btn(event,6))
    btn_7.place(x=70,y=190)

    btn_8= tk.Button(text="蠍座",font=("游ゴシック",10))
    btn_8.bind("<1>",lambda event:clear_btn(event,7))
    btn_8.place(x=130,y=190)

    # 五段目
    btn_9 = tk.Button(text="射手座",font=("游ゴシック",10))
    btn_9.bind("<1>",lambda event:clear_btn(event,8))
    btn_9.place(x=70,y=230)

    btn_10 = tk.Button(text="山羊座",font=("游ゴシック",10))
    btn_10.bind("<1>",lambda event:clear_btn(event,9))
    btn_10.place(x=130,y=230)

    # 六段目
    btn_11 = tk.Button(text="水瓶座",font=("游ゴシック",10))
    btn_11.bind("<1>",lambda event:clear_btn(event,10))
    btn_11.place(x=70,y=270)

    btn_12 = tk.Button(text="魚座",font=("游ゴシック",10))
    btn_12.bind("<1>",lambda event:clear_btn(event,11))
    btn_12.place(x=130,y=270)

    # ボタン型が入ったリストを作る（消す時便利）
    btn_list = [btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11,btn_12]



# ボタンを消す関数
def clear_btn(event,num):
    global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11,btn_12,btn_list
    for val in btn_list:
        val.destroy()

    # 占い結果を表示する関数を呼び出す
    get_uranai(num)


# 占い結果を表示する関数
def view_uranai(dic):
    """辞書型の引数を受け取り内容を画面に表示"""
    # print(dic["content"])
    global name,text1,text2,text3,text4,text5,text6,text7
    name = tk.Label(text=dic["sign"])
    name.pack(pady=3)

    text1 = tk.Text(width=33,height=4)
    text1.insert(tk.END,dic["content"])
    text1.pack()

    color = f"ラッキーカラー:{dic['color']}"
    text2 = tk.Label(text=color)
    text2.pack()

    item = f"ラッキーアイテム:{dic['item']}"
    text3 = tk.Label(text=item)
    text3.pack()

    total = "★" * dic["total"]
    text4 = tk.Label(text=f"全体運:{total}")
    text4.pack()

    love = "★" * dic["love"]
    text5 = tk.Label(text=f"恋愛運:{love}")
    text5.pack()

    money = "★" * dic["money"]
    text6 = tk.Label(text=f"金運:{money}")
    text6.pack()

    job = "★" * dic["job"]
    text7 = tk.Label(text=f"仕事運:{job}")
    text7.pack()

    make_return()


# 戻るボタンを表示する
def make_return():
    global back
    back = tk.Button(text="前のページに戻る")
    back.bind("<1>",back_main)
    back.pack()


# スタート画面に戻る
def back_main(event):
    global name,text1,text2,text3,text4,text5,text6,text7,back
    # まずは↑を消す
    name.destroy()
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()
    back.destroy()
    # 次に生む
    make_btn()


#ずっと出てる文字
ttl = tk.Label(text="今日の占い",font=("游ゴシック",16),fg="#336699")
ttl.pack()


# img_file = tk.PhotoImage(file = "image/fm.")

# canvas = tk.Canvas(bg = "white", width = 250,height = 330)
# canvas.place(x = 0,y = 0)
# canvas.create_image(0,0,image = img_file)




# ボタン類
make_btn()

root.mainloop()
