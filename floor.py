#!/usr/bin/python2.7
"""This program takes a floorplan and divides it into wall sections that can be
processed by the wall.py program"""
__author__ = 'Jan KLopper (janklopper@innerheight.com)'
__version__ = 0.1

import xml.etree.ElementTree as etree

def createwalls(inputfile):
  """This function takes the inputfile, parses it and decides on what wall
  sections are needed."""
  xmltree = etree.parse('examples/feed.xml')
  xmlroot = tree.getroot()

  for child in xmlroot:
    print child

if __name__ == '__main__':
  createwalls('floor.xml')
