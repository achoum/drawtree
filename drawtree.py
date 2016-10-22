# -*- coding: utf-8 -*-

##
## By Mathieu Guillame-bert
## 21 Oct. 2016
## 

import sys
import codecs

def numTab(s):
    r = 0
    while r<len(s):
        if s[r] != '\t':
            break
        r+=1
    return r

def main():

    END_BRANCH = "  +--"
    INTERM_BRANCH = "  +--"
    CONTINUITY = "  |  "
    NOTHING = "     "
    ADD_SPACE = True
    
    line = 0
    try:
        r = []
        lvl = 0
        cur = r
        p = []
        for l in sys.stdin:
            line+=1
            l = l.rstrip()
            n = numTab(l)
            if n>lvl+1:
                raise NameError('Cannot go down more than one level at the time')
            elif n==lvl+1:
                p.append(cur)
                cur = cur[-1][1]
                lvl = n
            elif n<lvl:
                for i in range(lvl-n):
                    cur = p.pop()
            lvl = n
            cur.append( (l.strip(),[]) )

        def rec(r,u):
            if ADD_SPACE and len(u)>0:
                nl = ""
                for j,x in enumerate(u[1:]):
                    if x:
                        nl += NOTHING
                    else:
                        nl += CONTINUITY
                nl += CONTINUITY
                print(nl)
                
            for i,e in enumerate(r):
                nl = ""
                last = i==len(r)-1
                for j,x in enumerate(u[1:]):
                    if x:
                        nl += NOTHING
                    else:
                        nl += CONTINUITY

                if len(u)>0:
                    if last:
                        nl += END_BRANCH
                    else:
                        nl += INTERM_BRANCH
                        
                nl += e[0]
                print(nl)
                if len(e[1])>0:
                    u.append(last)
                    rec(e[1],u)
                    u.pop()

        rec(r,[])
        
    except NameError as e:
        print("Error: "+str(e)+" (at line "+str(line)+")")

if __name__ == "__main__":
    main()
