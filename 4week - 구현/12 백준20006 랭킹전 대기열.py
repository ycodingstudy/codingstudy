# 매칭가능한 방 X -> 새로운 방 생성 및 입장
# 새 방 기준 첫 입장 플레이어 레빌이 -10에서 10까지 입장
# 매칭가능한 방 O -> 입장시킨 방의 정원이 탈 때까지 대기
# 방의 정원이 모두 차면 게임 시작

p, m = map(int, input().split())  # 플레이어의 수와 방의 정원
rooms = []
for _ in range(p):
    l, name = input().split()
    level = int(l)
    item = {'level': level, 'name': name}

    can_add = True  # 들어갈 방이 있는지 확인
    for room in rooms:
        if len(room) < m and room[0]['level'] - 10 <= level <= room[0]['level'] + 10:
            room.append(item)
            can_add = False
            break
    # rooms를 다 돌았음에도 들어갈 방이 없음
    if can_add:
        rooms.append([item])  # 새로 방 만들어서 넣음

for room in rooms:
    sorted_room = sorted(room, key=lambda x: x['name'])
    print("Started!") if len(room) == m else print("Waiting!")
    for item in sorted_room:
        print(item['level'], item['name'])

# 소요시간 : 55분 40.34초 // sorted_room에서 출력해야함...