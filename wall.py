#!/usr/bin/python
"""This program takes a wall and divides it into panels that can be routed"""
__author__ = 'Jan KLopper (jan@eth0.nl)'
__version__ = 0.1

import svgwrite

def wall(width, height, depth):
  wall = {
    "top": face(depth, width, [True, False, True, False]),
    }
  d = { "bottom": face(depth, width, [True, False, True, False]),
    "left": face(height, depth, [True, False, True, False]),
    "right": face(height, depth, [True, False, True, False]),
    "front": face(height, width, [True, False, True, False]),
    "back": face(height, width, [True, False, True, False])
    }
  return wall

def face(width, height, fingers):
  """Returns the lines for a face
  width
  height
  fingers as a interable 4 items long
    true for a positive start,
    false for a negative start
  """
  return {'top': fingerline((0,0), #top left
                            (0,width),#top right
                            fingers[0]),

          'right': fingerline((0,width), #top right
                              (height,width), # bottom right
                              fingers[1]),

          'bottom': fingerline((height,width), # bottom right
                               (height,0), # bottom left,
                               fingers[2]),
          'left':   fingerline((height,0),
                               (0,0),#top left
                               fingers[3])
          }

def fingerline(start, end, fingertype, fingercount=4, materialdepth=18):
  diff = {'x': start[0] - end[0],
          'y': start[1] - end[1]}
  lines = []
  fingertype = True
  if abs(diff['x']):
    section = abs(diff['x']) / fingercount
    for finger in xrange(0, fingercount):
      if fingertype:
        lines.append(((start[0] + (finger * section), start[0]),
                      (start[0] + ((finger + 1) * section), start[0])))
      else:
        # notch in
        lines.append(((start[0] + (finger * section), start[0]),
                      (start[0] + (finger * section), start[0] + materialdepth)))

        # actual line
        lines.append(((start[0] + (finger * section), start[0] + materialdepth),
                      (start[0] + ((finger + 1) * section), start[0] + materialdepth)))
        # notch out
        lines.append(((start[0] + ((finger + 1) * section), start[0] + materialdepth),
                      (start[0] + ((finger + 1) * section), start[0])))
      fingertype = not fingertype

  elif abs(diff['y']):
    section = abs(diff['y']) / fingercount
    lines.append((start, end))
  return lines


def svgwall(width, height, depth):
  faces = wall(width, height, depth);
  offset = (5, 5) # place things away from the wall
  for face in faces:
    prev = None
    dwg = svgwrite.Drawing('output/%s.svg' %  face,
                           size=('%dmm' % (width+offset[0]*2),
                                 '%dmm' % (height+offset[0]*2)),
                           viewBox=('0 0 %d %d' % (width+offset[0]*2,
                                                   height+offset[0]*2)))
    print faces
    for side in faces[face]:
      print '%s %r' % (side, faces[face][side])
      side = faces[face][side]
      for line in side:
        dwg.add(dwg.line(
              start=(line[0][0] + offset[0], line[0][1] + offset[1]),
              end=(line[1][0] + offset[0], line[1][1] + offset[1]),
              stroke='green'))
    dwg.save()

if __name__ == '__main__':
  svgwall(1200, 2200, 150)
