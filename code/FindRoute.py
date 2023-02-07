import Node
import numpy as np
import bisect
import globals
from array import*
final_route = []
class FindRoute:
    def findRoute(self):
        
        start = Node.Node(None,0,globals.startSearch)
        start.setAstarValue()
        globals.openList.append(start)


        
        while globals.targetFound == False:
            globals.openListCheck.sort()
            globals.openList.sort(key=lambda x: x.f)
            start = globals.openList[0] 
            start.addChildren(start)
            globals.openListCheck.sort()
            globals.openList.sort(key=lambda x: x.f)
            globals.openList.pop(0)
            globals.closedList.append(start.let)
            if start.let==globals.targetSearch:      
                globals.targetFound = True
        while start.parent != None:
            final_route.append(start.let)
            start = start.parent
        final_route.append(start.let)
        return final_route
