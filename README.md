flatpackhouse
=============

flat Pack house software for your 3 axis cnc


This is the code for the floorplan to house generator

The program should consist of 3 main programs and various smaller ones:

The editor:
  A webbased (javascript / canvas / webGL) floorplan editor and viewer.
  This allows the actual design of the floorplan to be edited, houses to be 
  created, designed, modified and parts like windows, doors, electrical elements
  and watter fittings to be placed.
  
The Router:
  This routes cables, conduits, gas lines etc from their respective start points
  to their end points. This would preferably be vissible in the editor.
  
The Slicer:
  Much like how 3d printers attack stl files by slicing them into layers, we 
  will use this program to slice the house into boxes. This program should take 
  into account the maximum size of woodpanels available, and the size of the cnc
  router.
  It should have two output types for walls, one for straight boxes, and one for
  boxes that will become corners, possibly with any angle.
  Floors and ceilings would be two more options, however thats not part of the 
  scope just yet.
  
The Wall engine:
  This code receives the width/height/depth of a box, and generates the 
  apropriate panels in svg. This also takes into account any fixtures and 
  conduits running trough, from and to the wall.
  Windows, and doors, both complete inside, and partially inside the wall should
  also be taken into account.
  Corner pieces would generate the panels that combine into a corner wall, given
  their angle.
  
The Gcode generator:
  This could be pycam or any other tool that can turn svg files into gcode files
  The width of the endmill being used is all thats needed as an input parameter 
  beyond the allready generated parts of every box.
