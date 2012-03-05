import pygraphviz as pgv
import os
import datetime
from subprocess import check_output, call

def toDot(filename):
    fileStr = check_output([os.path.dirname(os.path.abspath(__file__))+"/traverse",filename])
    filename = filename[0:-4]+".dot"
    f = open(filename,"w")
    f.write(fileStr)
    f.close()

def toPNG(filename):
    g=pgv.AGraph(filename)
    g.layout()
    newFile = filename[0:-4]+".png"
    g.draw(newFile)
