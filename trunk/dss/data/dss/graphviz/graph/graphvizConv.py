import pygraphviz as pgv
import os
import datetime

def toDot(filename):                                                                    fileStr = os.system(os.path.dirname(os.path.abspath(__file__))+"/traverse "+filename+" > "+filename[0:-4]+".dot")

def toPNG(filename):
    g=pgv.AGraph(filename)
    g.layout()
    newFile = filename[0:-4]+".png"
    g.draw(newFile)
