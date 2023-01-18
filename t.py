from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = mc.player.getTilePos()
h = 100
block = 0
print("pos: x:{},y:{},z:{},block:{}".format(x,y,z,block))
mc.setBlocks(pos, x+h,y+h,z+h, block)