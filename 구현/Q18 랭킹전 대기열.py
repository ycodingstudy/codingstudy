n, maxPlayer = map(int, input().split())
room = []
firstLv = []
for _ in range(n):
    player = list(map(str, input().split()))
    isJoin = False
    level = int(player[0])
    for i in range(len(room)):
        if firstLv[i] - 10 <= level <= firstLv[i] + 10 and len(room[i]) < maxPlayer:
            isJoin = True
            room[i].append((player[1], level))
            break
    if not isJoin:
        room.append([(player[1], level)])
        firstLv.append(level)

for players in room:
    if len(players) == maxPlayer:
        print("Started!")
    else:
        print("Waiting!")

    for player in sorted(players):
        print(str(player[1]) + " " + player[0])
