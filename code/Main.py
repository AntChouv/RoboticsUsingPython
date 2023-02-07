import FindRoute
import numpy as np
import globals
arr=np.array([['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P'],['Q','R','S','T']])# πίνακας για την ευρεση συντεταγμένων
globals.initialize()
globals.startSearch = 'A'
if __name__ == "__main__":
    
    while  globals.targetSearch != 'A':

        globals.targetSearch = input("Give target")

        fn = FindRoute.FindRoute()
        final = fn.findRoute()
        final.reverse() # λίστα στάσεων
        print(final)
        directions = [] # λίστα οδηγιών

        if globals.previous == ' ':#ελεγχος για το αν είναι η αρχή της διαδρομής
            cur = final[0]
            final.pop(0)
            nex = final[0]
            final.pop(0)
            if nex == 'E':
                directions.append("deksia")
            elif nex == 'B':
                directions.append("eutheia")
            prev = cur
            cur = nex
        else:
            final.pop(0)
        while len(final) != 0:
            nex = final[0]
            final.pop(0)
            result = np.where(arr == prev)
            ip= int(result[0]) # συντεταγμένες προηγούμενου
            jp= int(result[1])
        
            result = np.where(arr == cur)
            iC= int(result[0]) # συντεταγμένες τωρινού
            jC= int(result[1])

            result = np.where(arr == nex)
            iN= int(result[0]) # συντεταγμένες επόμενου
            jN= int(result[1])
            if ip == iN and jp == jN:
                directions.append("anastrofi")
    
            if ip + 1 == iC and iN == iC and jC==jp and jN - 1 == jC:
                directions.append("aristera")
            
            elif ip == iC and iC == iN-1 and jp == iC - 1 and jC == jN:
                directions.append("deksia")
            elif ip + 1 == iC and iC == iN-1 and jp == jC and jC == jN:
                directions.append("eutheia")
            elif jp + 1 == jC and jC == jN-1 and ip == iC and iC == iN:
                directions.append("eutheia")
                
            elif ip == iC and iN == iC-1 and jC-1==jp and jN == jC:
                directions.append("aristera")
                
            elif ip-1 == iC and iN == iC and jC==jp and jN == jC-1:
                directions.append("aristera")
            elif ip == iC and iN == iC-1 and jC == jp-1 and jN == jC:
                directions.append("deksia")
            elif ip == iC +1 and iN+1 == iC and jC==jp and jN == jC:
                directions.append("eutheia")
            elif ip == iC and iC == iN:
                directions.append("eutheia")
            
            else:
                directions.append("deksia")
    
            prev = cur
            cur = nex
            if globals.targetSearch == nex:
                directions.append("stop")
                break
            


        globals.previous = prev
        globals.startSearch = cur
        print(directions)
        globals.openList = []
        globals.openListCheck = []
        globals.closedList = []
        globals.targetFound = False
  
        
        
            
                
