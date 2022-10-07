from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)


marble = Material(spec = 64, texture = Texture("whiteMarble.bmp"))

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))


rtx.scene.append( Torus2D(position = (1,-1,-7), radius = 1, radius2 =0.3, normal = (0,0,1), material = glass ))
rtx.scene.append( Torus2D(position = (1,2,-7), radius = 1.5, radius2 =0.8, normal = (0,0,1), material = marble ))
rtx.scene.append( Torus2D(position = (-2,1.5,-7), radius = 2, radius2 =0.9, normal = (0,0,1), material = brick ))
rtx.glRender()

rtx.glFinish("output1.bmp")