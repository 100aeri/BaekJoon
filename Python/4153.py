tri_list = []
tri = [0,0,0]
while True:
    tri = list(map(int, input().split(" ")))
    if (tri[0] == tri[1] == tri[2] == 0): break
    tri_list.append(tri)
for i in tri_list:
    i.sort()
    if (i[2]**2 == i[0]**2 + i[1]**2): print("right")
    else: print("wrong")