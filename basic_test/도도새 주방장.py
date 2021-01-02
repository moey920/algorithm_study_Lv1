dodo = list(map(int,input().split()))
cook_time = list(map(int,input().split()))
sum_cook = 0

for i in range(len(cook_time)) :
    sum_cook += cook_time[i]
    if sum_cook > dodo[1] :
        sum_cook -= cook_time[i]
        print(i)
        break
        
# print(sum_cook)
