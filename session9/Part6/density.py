district = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
populations = [150300,247100,333300,266800,420900,318000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
# for y in district:
#     print(y)
# for x in population:
#     print(x)
for i,population in enumerate(populations):
    density.append(populations[i]/area[i])
    print (density)

