B = int(input()) # 업무일지 B의 길이를 나타내는 정수 N을 입력합니다.
Bi = list(map(int,input().split())) #업무일지 Bi이루는 N개의 정수를 입력합니다.
j = [4,3,2,1,0]
a = []


for i in range(5) :
    a.insert(i, Bi[i]*(B-j[i]))
    # a [1,4,6,12,20]

result = a
result[4] = a[4]-a[3]
result[3] = a[3]-a[2]
result[2] = a[2]-a[1]
result[1] = a[1]-a[0]
result[0] = a[0]
