import sys
import pygraphviz as pgv
import os
import datetime
from subprocess import check_output, call

filepath = sys.argv[1]

if ".pml" in filepath:
    print "pml file!"
    fileStr = check_output(["./traverse",filepath])
    filepath = "file.dot"
    f = open(filepath,"w")
    f.write(fileStr)
    f.close()

g=pgv.AGraph(filepath)
g.layout()

date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")+".png"
g.draw(date)
call(["rm","file.dot"])
call(["gnome-open",date])
