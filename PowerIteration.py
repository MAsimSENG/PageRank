#!/usr/bin/env python3
import re
from copy import deepcopy
import array

def main():

    matrixM = [[0,1/2,0,0],[1/3,0,0,1/2],[1/3,0,1,1/2],[1/3,1/2,0,0]];
    Rold = [1/4,1/4,1/4,1/4];
    rNew=[0,0,0,0]
    teleportProb = [1/20,1/20,1/20,1/20];

# Get BM
    for x in range (0,len(matrixM)):
        for y in range (0, len(matrixM[0])):
            matrixM[x][y] = 0.8 * matrixM[x][y]

# get BM * Rold
    for z in range(0,1000):
        rNew=[0,0,0,0]
        for x in range(0, len(matrixM)):
            for y in range(0, len(matrixM[0])):
                rNew[x] += matrixM[x][y] * Rold[y];
        for q in range(0,len(teleportProb)):
            rNew[q] +=teleportProb[q];

        Rold = rNew[:];
    print(rNew)


if __name__ == '__main__':
	main()
