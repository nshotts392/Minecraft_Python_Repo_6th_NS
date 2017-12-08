from mcpi.minecraft import Minecrat
mc = Minecraft.create()
import time
s = 0
x, y, z = mc.player.getPos()
BA = mc.getBlock(x, y+2, z)
