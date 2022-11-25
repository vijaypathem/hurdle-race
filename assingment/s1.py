height = [1,2,3,3,2]
k = 1
max_height=0
def main(k,max_height,height):
    for h in height:
        if h>max_height:
            max_height=h
    if max_height>k:
        return max_height-k
    else:
        return 0

print(main(1, max_height, height))
