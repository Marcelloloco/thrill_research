# Reads text files, matches point coordinates, and writes an SVG containing the
# founds points

import sys
import re

if len (sys.argv) != 2:
    print("Usage: points2svg.py <text file>")
    sys.exit(1)

# SVG header
print("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   version="1.1" id="svg2">
  <g id="layer1">
""")

# Function to output SVG objects
def MakeColor(x):
    return ("#%02x%02x%02x") % (
        int((3 * (x + 1) % 11) / 11.0 * 256),
        int((7 * (x + 1) % 11) / 11.0 * 256),
        int((9 * (x + 1) % 11) / 11.0 * 256))

def SVGPoint(x,y,color):
    print('<path style="fill:none;stroke:' + color + ';stroke-width:3.0;stroke-linecap:round;'
          'stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1" '
          'd="m ' + str(x) + ',' + str(y) + ' v 0" />')

def SVGCircle(x,y,r,color):
    print('<circle r="'+ str(r) + '" cx="' + str(x) + '" cy="' + str(y) + '" style=\"stroke:black;stroke-opacity:1;fill:' + color + ';fill-opacity:1\" />')

# read lines from file, match regex, and output SVG objects
with open(sys.argv[1]) as f:
    for line in f:
        # match (x,y) syntax
        match = re.search('\(([0-9.e]+),([0-9.e]+)\)', line)
        if match:
            SVGPoint(match[1], match[2], "black")
        # match (x,y/c) syntax
        match = re.search('\(([0-9.e]+),([0-9.e]+)/([0-9]+)\)', line)
        if match:
            SVGPoint(match[1], match[2], MakeColor(int(match[3])))
            #SVGCircle(match[1], match[2], 6, MakeColor(int(match[3])))

# SVG footer
print("</g></svg>")
