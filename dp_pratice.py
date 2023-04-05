# 總重4，求最佳組合
things = { "com":{1:60}, "guitar":{4:90}, "sound":{3:80} }
# 有一個2維陣列，x, y分別為重量/物品名稱，格子為重要程度
dp = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# 建立地回
count = len(things.keys()) # 填表次數
label = list(things.keys())
for x in range(count):
    for y in range(4):
        weight, point = tuple(things[label[x]].items())[0]
        # 第一排只要夠輕就可以加入dp_array
        if x == 0 or y == 0:
            if weight <= y + 1:
                dp[x][y] = point
            else: 
                if x != 0:
                    dp[x][y] = dp[x - 1][y]
        # 其他情況還要先比較過才知道
        else:   
            if weight < y + 1:  
                dp[x][y] = max(dp[x-1][y], (point + dp[x-1][y-weight+1]))
            elif weight == y + 1:
                dp[x][y] = point             
            else:
                dp[x][y] = dp[x][y-1]

    # print(f"{weight= } {point= } {x= } ---------------------------- ")
    # for x in dp:
    #     print(x)

for x in dp:
    print(x)



