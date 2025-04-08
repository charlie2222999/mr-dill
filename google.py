L= [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
low = 0
high = len(L)-1
mid = low +high//2
target_value = int(input('enter a target value'))
if mid ==target_value:
    print(mid)
elif mid< target_value:
    low = mid+1
elif mid> target_value:
    high = mid-1
    

            