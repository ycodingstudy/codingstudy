def is_valid(buildings):
    for x, y, a in buildings:
        if a == 0:  # 기둥일 때
            if y == 0 or (x, y - 1, 0) in buildings or (x - 1, y, 1) in buildings or (x, y, 1) in buildings:
                continue
            else:
                return False
        elif a == 1:  # 보일 때
            if (x, y - 1, 0) in buildings or (x + 1, y - 1, 0) in buildings or ((x - 1, y, 1) in buildings and (x + 1, y, 1) in buildings):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    buildings = []  # 설치된 기둥과 보 정보를 저장하는 리스트
    
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치 작업일 때
            buildings.append((x, y, a))
            if not is_valid(buildings):
                buildings.remove((x, y, a))
        else:  # 삭제 작업일 때
            buildings.remove((x, y, a))
            if not is_valid(buildings):
                buildings.append((x, y, a))
    
    buildings.sort()  # 규칙에 따라 정렬
    
    return buildings