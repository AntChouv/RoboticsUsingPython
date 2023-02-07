from array import*
import bisect
import globals
import numpy as np
arr=np.array([['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P'],['Q','R','S','T']])

 
class Node:
    def __init__(self,parent,sumPath,let):
        self.let = let
        self.s = sumPath
        self.children = []
        self.parent = parent
        self.h = 0
        self.f = 0
    def setAstarValue(self):
            

            srt= self.let
            result = np.where(arr == globals.targetSearch)
            iT= int(result[0])
            jT= int(result[1])


            result = np.where(arr == srt)
            
            iS= int(result[0])
            jS= int(result[1])


            euklidian_dist=((((iS-iT)*3)**2)+(((jS-jT)*5)**2))**0.5
            self.f = self.s + euklidian_dist
    def getAstar(self):
        return self.f
    def addChildren(self,node2Exp):
        
        start = np.where(arr == self.let)
        iS= int(start[0])
        jS= int(start[1])
        if iS>= 0 and iS<4:
            ic1=iS+1
            jc1=jS
            s=self.s+3
            if arr[ic1][jc1] not in globals.closedList and arr[ic1][jc1] not in globals.openListCheck:
                chld1 = Node(node2Exp,s,arr[ic1][jc1])
                self.children.append(chld1)
                chld1.setAstarValue()
                globals.openList.append(chld1)
                globals.openListCheck.append(arr[ic1][jc1])
        if iS<=4 and iS>0:
            ic1=iS-1
            jc1=jS
            s=self.s+3
            if arr[ic1][jc1] not in globals.closedList and arr[ic1][jc1] not in globals.openListCheck:
                chld1 = Node(node2Exp,s,arr[ic1][jc1])
                self.children.append(chld1)
                chld1.setAstarValue()

                globals.openList.append(chld1)
                globals.openListCheck.append(arr[ic1][jc1])
        if jS>=0 and jS<3:
            
            ic2=iS
            jc2=jS+1
            s=self.s+5
            if arr[ic2][jc2] not in globals.closedList and arr[ic2][jc2] not in globals.openListCheck:
                chld2 = Node(node2Exp,s,arr[ic2][jc2])
                self.children.append(chld2)
                chld2.setAstarValue()
                globals.openList.append(chld2)
                globals.openListCheck.append(arr[ic2][jc2])
        if jS<=3 and jS>0:
            
            ic2=iS
            jc2=jS-1
            s=self.s+5
            if arr[ic2][jc2] not in globals.closedList and arr[ic2][jc2] not in globals.openListCheck:
                chld2 = Node(node2Exp,s,arr[ic2][jc2])
                self.children.append(chld2)
                chld2.setAstarValue()
                globals.openList.append(chld2)
                globals.openListCheck.append(arr[ic2][jc2])
