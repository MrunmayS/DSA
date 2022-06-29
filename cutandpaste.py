n = int(input())
m = 1000000007
for _ in range(n):
    x = int(input())
    c = ''
    s = input()
    l = 0
    while l != x:
        l = l + 1
        c = s[l:]
        s = s[0:l]
        sl = int(s[-1])
        s = "".join([s, c*sl])

    print(len(s)%m)
        
