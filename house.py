# import time
from mcpi.minecraft import Minecraft
import mcpi.block as block
import mcpi.entity as entity
mc = Minecraft.create()
from itertools import product

block, state = 0 , 1

# x, y, z = 100, 0 ,0
x,y,z = pos = mc.player.getTilePos()
lenght_x = 10
height_y = 5
lenght_z = 3

end_x = [lenght_x, +x]#, lenght_x, 0]
# end_x = [lenght_x, +lenght_x, lenght_x, +lenght_x]
end_y = [height_y, 0, height_y, 0]
end_z = [0, lenght_z, 0, lenght_z]

# mc.setBlock(x, y-2, z, 152)
# mc.player.setPos(x, y, z)

pos = mc.player.getPos()
mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))

for i in range(len(end_x)):
    print("Start: ")
    print(x,y,z)
    print("Finish: ")
    print(end_x[i], end_y[i], end_z[i])
    print("Block: ")
    print(block, state)
    print("==============================")

    mc.setBlocks(x,y,z, end_x[i], end_y[i], end_z[i], block, state)
    x = end_x[i]
    y = end_y[i]
    z = end_z[i]
    # block+=1
# for a, b, c in product(end_x, end_y, end_z):
#     print(a, b, c)
# mc.setBlocks(x,y,z, end_x, end_y, end_z, block, state)

stairBlock = 114
step = 0
x, y, z = pos.x, pos.y, pos.z
for i in range(100):
    mc.setBlock(x + step, y + 1 + step, z, stairBlock)
    for j in range(5):
        mc.setBlock(x + step, y + j + step, z, 0)
    step += -1
    mc.setBlock(x + step, y + j + 1 + step, z, 89)