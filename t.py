from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from itertools import product
from itertools import permutations

#x,y,z = pos = mc.player.getTilePos()
x,y,z = 0,0,0
delta = 1
x2 = x+delta
z2 = z+delta

list(permutations('XYZ', 3))
print(list(permutations('XYZ', 3)))

# coordinates = [(x,x2), (z,z2)]
# data = list(product(*coordinates))
# for i in data:
#     y = mc.getHeight(i[0],i[1])
#     print([i[0], y+1, i[1]])
#     data_y.append([i[0], y, i[1]])
#     mc.setBlock([i[0], y, i[1]], 152)

# # print("pos: x:{},y:{},z:{},block:{}".format(x,y,z,block))
# # boom = a,b,c
# # target = mc.getBlock(boom)
# # y_hi = mc.getHeight(dx,dz) # Находим максимальную высоту в данной точке