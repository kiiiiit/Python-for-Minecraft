import time
# from itertools import chain
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mult = 5
# x,y,z = pos = mc.player.getTilePos()
x,y,z = pos = 0,0,mult*2
loot = [0,233,207,165,30,92,(35,14),162,57,56,103,21,22,4,2,46,(5,4),(17,2),(17,3),41,42,133,129,14,127,142,74,152,47,62,59,119,(6,3),83,116,173,86, (6,1),141,250]

i = 0
for j in loot:
# for j in range(1, 255):
    i+=1
    # Очищаем пространство
    # mc.setBlocks(x+i*mult,y,z-3, x+7+i*mult, y+7, z+7, 0)
    # Ставим стены
    mc.setBlocks(x+i*mult,y,z, x+mult+i*mult, y+mult, z+mult, 49)
    mc.setBlocks(x+i*mult+1,y+1,z+1, x+mult-1+i*mult, y+mult-1, z+mult-1, j)
    # Светильник
    mc.setBlocks(x+4+i*mult,y+mult,z+4,x+1+i*mult,y+mult,z+1, 89)
    # Пол
    # mc.setBlocks(x+4+i*mult,y,z+4,x+1+i*mult,y,z+2, 154)
    # mc.setBlocks(x+4+i*mult,y,z+1,x+1+i*mult,y,z+1, 54)
    # # Витрина
    mc.setBlocks(x+i*mult,y,z,x+mult+i*mult, y+mult, z, 20)

    # Road
    mc.setBlocks(x+i*mult,y-1,z-3, x+mult+i*mult, y-1, z, 152)
    mc.setBlocks(x+i*mult,y-1,z-2, x+mult+i*mult, y-1, z-1, 124) # Подстветка дорожки
    mc.setBlocks(x+i*mult,y,z-3, x+mult+i*mult, y, z-3, 27)
    # n=0
    # for j in range(42, 42):
    #     n+=1
    #     mc.spawnEntity(x+i*mult+n,y,z-3, x+i*mult+n, y, z-3, j)
    # # MOB
    # time.sleep(10)
    # mc.spawnEntity(x+3+i*mult,y+1,z+3,120)

# Домик Стива
# i = 0
# while i < mult:
#     i+=1
#     mc.setBlocks(x-i, y-1, z-i, x+i, y-1, z+i, 152)
#     mc.setBlocks(x-i, y, z-i, x+1, y+3, z+1, 0)
#     mc.setBlock (x, y+3, z, 89)

blocks = [162,1,42,57]
j = 0
for n in blocks:
    j+=1
    for i in range(1,mult):
        mc.setBlock (mult+4, y+i, mult*2+j, n)

mc.setBlock (mult+1, y+3, mult*2+mult-1, 64) # Door
# mc.setBlock (mult+1, y+1, mult*2+3, 119) # Ender portal

for i in range(3):
    mc.setBlock (mult+1+i, y+3, mult*2+mult-1, 103) # Melon

for i in range(3):
    mc.setBlock (mult+1+i, y+mult-1, mult*2+mult-1, 35,2) # Wool

mc.setBlock (mult+1, y+1, mult*2+mult-1, 54) # Сундук
mc.setBlock (mult+2, y+1, mult*2+mult-1, 54) # Сундук
mc.setBlock (mult+3, y+1, mult*2+mult-1, 58) # Верстак

# mc.player.setTilePos(pos)
mc.player.setTilePos(mult+2, y+1, mult*2+2)