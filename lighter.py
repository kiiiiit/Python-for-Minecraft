from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = 0,0,0
# x,y,z = pos = mc.player.getTilePos()
# Zero Zone
zz = 5
mc.setBlocks(x-zz, y, z-zz, x+zz, y+zz*2, z+zz, 0)

# Строим 4 маяка
blocks = [133, 41, 42, 57, 41]
h = 4 # Высота
# x = x+3
y = y+h-1
# z = z+3
j = 0
i = 0
for j in blocks:
    for i in range(h):
        mc.setBlocks(x-i,y-i,z-i, x+i, y-i, z+i, j)
    mc.setBlock(x, y-i+h-1, z, 138)
    x = x+h*2

# # Move Steve
# i = 0
# while i < 3:
#     i+=1
#     mc.setBlocks(x-i, y-1, z-i, x+i, y-1, z+i, 152)
#     mc.setBlocks(x, y, z, x+1, y+3, z+21, 0)
#     mc.setBlock (x, y+3, z+20, 89)
#     mc.player.setTilePos(x,y,z)