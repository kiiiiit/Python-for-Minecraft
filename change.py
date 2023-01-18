# Расчистка территории от ненужных блоков
# Больше вариантов здесь
# https://github.com/kiiiiit/Python-for-Minecraft
#
import time
from itertools import product
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sand_to_new_block(x):
    ''' Функция для заменя блоков из перечня '''
    if x in blocks: # Выборка из перечня блоков
        x = 0 # На что меняем
    return x

blocks = [1,2,3,4,7,8,9,12,13,24,60,208] # Что меняем

x,y,z = pos = mc.player.getTilePos() # Точка начала
print("Position is: ", pos)
# y=0 # Если хотим менять от отметки 0

# Задаем размеры кубоида
lenght = int(input("Длина: "))
width  = int(input("Ширина: "))
depth  = int(input("Высота: "))

# Указываем вторые координаты для кубоида
delta_x = x+lenght
delta_y = y+depth
delta_z = z+width

# Новые массивы по осям
new_x = (x,delta_x)
new_y = (y,delta_y)
new_z = (z,delta_z)

block_i = 0

now_blocks = list(mc.getBlocks(pos, delta_x-1, delta_y-1, delta_z-1))
new_blocks = list(map(sand_to_new_block, now_blocks))
time.sleep(5)

for dy, dx, dz in product(new_y, new_x, new_z):
    boom = dx,dy,dz # Координаты для заменяемого блока
    target = new_blocks[block_i]
    if target == 0:
        mc.setBlock(boom, target)
    block_i += 1