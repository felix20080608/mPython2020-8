from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBLock(x,y,z+1,15)
mc.setBLock(x+1,y,z,15)
mc.setBLock(x-1,y,z,15)
mc.setBLock(x,y,z-1,15)