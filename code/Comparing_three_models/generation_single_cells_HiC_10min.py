
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:13:30 2022

@author: samir
"""
import numpy as np
import math
import pandas as pd

#dictionary
Dict = {1: 'CIS_X6S', 2: 'CIS_X6S_2', 3: 'CIS_X7N', 4: 'CIS_X7N_2', 5: 'm06_CIS_X6S', 6: 'm06_CIS_X6S_2', 7: 'm06_CIS_X7N', 8: 'm06_CIS_X7N_2', 9: 'm06_TRANS_X3S', 10: 'm06_TRANS_X4N', 11: 'p06_CIS_X6S', 12: 'p06_CIS_X6S_2', 13: 'p06_CIS_X7N', 14: 'p06_CIS_X7N_2', 15: 'p06_TRANS_X3S', 16: 'p06_TRANS_X4N', 17: 'TRANS_X3S', 18: 'TRANS_X4N'}
Dict2 = {1: '1st', 2: '2nd', 3: '3rd', 4: '4th', 5: '5th', 6: '6th', 7: '7th', 8: '8th', 9: '9th', 10: '10th', 11: '11th', 12: '12th', 13: '13th', 14: '14th', 15: '15th', 16: '16th', 17: '17th', 18: '18th'}
Dict3 = {1:'1h', 2: '2h', 3: '3h', 4: '4h', 5: '5h', 6: '6h', 7: '7h', 8: '8h', 9: '9h', 10: '10h', 11: '11h'}
#http://www.cookbook-r.com/Numbers/Generating_random_numbers/
for dict_num in (8,9,10):
    tempDf = pd.DataFrame(columns=['str'])
    tempDf2 = pd.DataFrame(columns=['str'])
    topo = Dict.get(dict_num)
    for z in range(1, 2, 1):
        print("\n")
        for y in (0.5, 1,2,3,4,5,10,30,60,180,240,300, 360, 420, 480, 540, 600, 660):
            #print(y)
            print("\n",y)
            #According to the single-cell Hi-C experiment, it is likely to having the crosslinking in each single moment during 10 minutes
            for q in range(0, 6060, 1):
                vstart = str(math.floor((606*y))+q)
                vend = str(math.floor((606*y))+q)
                vstr = "./tad_tad_end ../sim_3h41h_1h1hBh_r20_G001_400M_Act/"
                vstr += topo#Dict.get(a[z-1][y-1]) 
                vstr += "/simulation.vtf LamSites_bID_0.txt 0.2" 
                vstr += " " + vstart + " " + vend + " " + ">HiC_" + vstart + "_" + vend + "_" +topo+ ".map"
                #print(vstr)
                if (y<180):
                    tempDf = tempDf.append({'str': vstr}, ignore_index=True)
                else:
                    tempDf2 = tempDf2.append({'str': vstr}, ignore_index=True)

    tempDf.to_csv(topo+"_first.script",header =None,index=False)   
    tempDf2.to_csv(topo+"_second.script",header =None,index=False)   


# C = np.zeros((18, 18))
# for x in range(2020, 38380, 2020):
#     print("\n")
#     for j in range(1,11):
#         a= x*j
#         print((x*(j-1)+1)," ",a)
