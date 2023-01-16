from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = [1,2,3,4,8,9,13,41]
x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = 0,0,0
print("Position is: ", pos)

delta = 2
delta_x = x+delta
delta_y = y+delta
delta_z = z+delta
block = 0
m = 0

now = list(mc.getBlocks(pos, delta_x-1, delta_y-1, delta_z-1))
# # print(list(now))
for a in range(x,delta_x):
    for b in range(y,delta_y):
         for c in range(z,delta_z):
            boom = a,b,c
            target = now[m]
            print("Найден: x:{},y:{},z:{}, получен:{}".format(a,b,c, target))
            if target in blocks:
                print("BOOM: x:{},y:{},z:{}, поставлен:{}".format(a,b,c, block))
                mc.setBlock(boom, block)
            m += 1
