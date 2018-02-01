from mcpi.minecaft import Minecraft
mc = Minecraft.create()
def growTree(1, 5, 10):
x, y, z = mc.player.getTilePos()
growTree(x + 1, y, z)
