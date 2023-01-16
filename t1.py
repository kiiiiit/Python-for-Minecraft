# from itertools import product
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = [1,2,3,4,8,9,13]
# x,y,z = pos = mc.player.getTilePos()
x,y,z = pos = 0,0,0
print("Position is: ", pos)

delta_x = 2
delta_y = 2
delta_z = 2
block = 41
now = mc.getBlocks(pos, delta_x-1, delta_y-1, delta_z-1)
# print(list(now))
for m in now:
    print("block in NOW:",m)
    for a in range(x, delta_x):
        for b in range(y, delta_y):
            for c in range(z, delta_z):
                boom = a,b,c
                target = mc.getBlock(boom)
                print("Найден: x:{},y:{},z:{}, получен:{}".format(a,b,c, target))
                if target not in blocks:
                    print("BOOM: x:{},y:{},z:{}, поставлен:{}".format(a,b,c, block))
                    mc.setBlock(boom, block)
