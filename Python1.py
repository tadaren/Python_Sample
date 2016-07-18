# -*- coding: UTF-8 -*-
'''
Created on 2016/07/16

@author: shopn_000
'''
import random
loop = True
win = 0
lose = 0
draw = 0
end = "stop"
instr = '数字を入力してください (1:ぐう 2:ちょき 3:ぱあ)'+end+'入力で終了\n'
while loop:
    stdIn = input(instr)
    if stdIn == end:
        loop = False
        continue
    elif stdIn != "1" and stdIn != "2" and stdIn != "3":
        print("入力がおかしいです")
        continue
    com = random.randint(1,3)
    player = int(stdIn)
    te = ('"ぐう"','"ちょき"','"ぱあ"')
    battle = ('"負け"','"勝ち"','"引き分け"')
    hantei = (player-com+2)%3
    if hantei == 0:
        lose+=1
    elif hantei == 1:
        win+=1
    elif hantei == 2:
        draw+=1
    print("プレイヤーの手は "+te[player-1]+" COMの手は "+te[com-1]+" でプレイヤーの"+battle[hantei])
    print("勝ち",win,":負け",lose,":引き分け",draw,"\n")
print("勝ち",win,":負け",lose,":引き分け",draw)