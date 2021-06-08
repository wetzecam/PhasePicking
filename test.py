#!/usr/bin/env python
import sys
from time import *
import array
import struct
import math

Status = [[True,True,False,True,True,True,True,True,False],
          [True,True,False,True,False,True,True,True,False],
          [False,True,False,True,False,True,True,True,False],
          [False,False,False,False,False,False,False,True,False],
          [False,False,False,False,False,False,False,False,False],
          [True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,False]]

def main():
    for x in range(0,15):
        print(x)

def findBestWindow(statArr):
    BestStart = -1;
    BestEnd   = -1;
    CurrStart = -1;
    CurrEnd   = -1;
    BestWindowSpecs = [-1,-1]

    for phi in range(len(statArr)):
        print('Current Phase = ',phi,' Status = ',statArr[phi])
        if(statArr[phi]):
            #Check if Start of new Window
            if(CurrStart == -1):
                # New Window Set Bounds to Current phase
                CurrStart = phi
                CurrEnd = phi
            else:
                # Continuing Window Set End to Current phase
                CurrEnd = phi
        else:   # Window Has ended
            if((BestStart == -1) & (CurrStart != -1)):    # No Best Window Has been Set yet
                BestStart = CurrStart
                BestEnd   = CurrEnd
            elif((BestEnd-BestStart)<(CurrEnd-CurrStart)): # Better Window has been detected
                BestStart = CurrStart
                BestEnd   = CurrEnd
            CurrStart = -1
            CurrEnd = -1

    # Checks if no "Bad" phases were detected, sets Best window as full range
    if((BestStart == -1) & (CurrStart != -1)):
        BestStart = CurrStart
        BestEnd = CurrEnd

    BestWidth = (BestEnd - BestStart) + 1
    CenterWindow = math.floor((BestStart + BestEnd)/2)
    print('Best Window: Width = ',BestWidth,' Center = ', CenterWindow)

    BestWindowSpecs[0] = BestWidth
    BestWindowSpecs[1] = CenterWindow

    return BestWindowSpecs

if __name__ == '__main__':
    main()
