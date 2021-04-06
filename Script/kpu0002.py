while True:
    N = eval(input())
    if N <= 10000:
        break

player1 = []
player2 = []

i = 0
while(i < N):
    Si, Ti = [eval(i) for i in input().split()]
    if 1 <= Si <= 1000 and 1 <= Ti <= 1000:
        player1.append(Si)
        player2.append(Ti)
        i+=1


print(player1)
print(player2)
L = 0
W = 1

play1 = 0
play2 = 0
for i in range(N):
    play1 += player1[i]
    play2 += player2[i]

    if play1 > play2:
        L = play1 - play2
    else:
        L = play2 - play1

if play1 > play2:
    W = 1
else:
    W = 2

print(W, L)
