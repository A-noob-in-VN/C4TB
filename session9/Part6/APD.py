district = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
populations = [150300,247100,333300,266800,420900,318000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
total_populations = 0
# for y in district:
#     print(y)
# for x in population:
#     print(x)
# for i,population in enumerate(populations):
#     density.append(populations[i]/area[i])
#     print (density)
for i in populations:
    total_populations = total_populations + i
    print (total_populations)
all_district = len(district)
print (len(district)) 
# print (total_populations)
average_populations = total_populations/all_district
print (average_populations)
