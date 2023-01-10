from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = 0,0,0
# Zero Zone
zz = 20
mc.setBlocks(x, y, z-zz, x+zz, y+zz, z+zz, 0)

# Стеклянный купол
w = 5
h = 3
mc.setBlocks(x-w,y,z-w, x+w, y+h, z+w, 95)
mc.setBlocks(x-w+1,y,z-w+1, x+w-1, y+h-1, z+w-1, 0)
mc.setBlocks(x-w, y-1, z-w, x+w, y-1, z+w, 152)
mc.setBlock (x,y+h*2,z,10)
# mc.player.setTilePos(pos)
