'''
Rudolf and Bernard decided to play a game with their friends. n
 people stand in a circle and start throwing a ball to each other. They are numbered from 1
 to n
 in the clockwise order.

Let's call a transition a movement of the ball from one player to his neighbor. The transition can be made clockwise or counterclockwise.

Let's call the clockwise (counterclockwise) distance from player y1
 to player y2
 the number of transitions clockwise (counterclockwise) that need to be made to move from player y1
 to player y2
. For example, if n=7
 then the clockwise distance from 2
 to 5
 is 3
, and the counterclockwise distance from 2
 to 5
 is 4
.

Initially, the ball is with the player number x
 (players are numbered clockwise). On the i
-th move the person with the ball throws it at a distance of ri
 (1≤ri≤n−1
) clockwise or counterclockwise. For example, if there are 7
 players, and the 2
nd player, after receiving the ball, throws it a distance of 5
, then the ball will be caught by either the 7
th player (throwing clockwise) or the 4
th player (throwing counterclockwise). An illustration of this example is shown below.


The game was interrupted after m
 throws due to unexpected rain. When the rain stopped, the guys gathered again to continue. However, no one could remember who had the ball. As it turned out, Bernard remembered the distances for each of the throws and the direction for some of the throws (clockwise or counterclockwise).

Rudolf asks you to help him and based on the information from Bernard, calculate the numbers of the players who could have the ball after m
 throws.

Input
The first line of the input contains a single integer t
 (1≤t≤104
) — the number of test cases. Then follow the descriptions of the test cases.

The first line of each test case contains three integers n,m,x
 (2≤n≤1000
, 1≤m≤1000
, 1≤x≤n
) — the number of players, the number of throws made, and the number of the player who threw the ball first, respectively.

The next m
 lines contain information about each throw in order. Each of them contains an integer ri
 (1≤ri≤n−1
) — the distance at which the i
-th throw was made, and a symbol ci
, equal to '0', '1', or '?':

if ci
='0', then the i
-th throw was made clockwise,
if ci
='1', then the i
-th throw was made counterclockwise,
if ci
='?', then Bernard does not remember the direction and the i
-th throw could have been made either clockwise or counterclockwise.
It is guaranteed that the sum n⋅m
 (n
 multiplied by m
) over all test cases does not exceed 2⋅105
.

Output
For each test case, output two lines.

In the first line, output the number of players k
 (1≤k≤n
) who could have the ball at the end of the game.

In the next line, output k
 numbers bi
 (1≤bi≤n
) — the numbers of the players in increasing order. All numbers must be different.

'''

case = input("cs: ")

for i in range(int(case)):
    prob_player = []
    n, m, x = input("nmx: ").split()
    
    for j in range(int(m)):
        r, c = input("r,c: ").split()
        if int(m)>1:
            if r not in prob_player:
                prob_player.append(r)
        counterCLock = int(x) + int(int(int(n)-int(r)))
        clock = int(x) + int(r)
        if c == '0':
            if clock not in prob_player:           
                prob_player.append(clock)
        elif c == '1':
            if counterCLock not in prob_player:
                prob_player.append(counterCLock)
        elif c == '?':
            if clock not in prob_player:
                prob_player.append(clock)
            if counterCLock not in prob_player:
                prob_player.append(counterCLock)
    prob_player = list(set(prob_player))
    prob_player = list(dict.fromkeys(prob_player))
    print(len(prob_player))
    for i in prob_player:
        print(i)