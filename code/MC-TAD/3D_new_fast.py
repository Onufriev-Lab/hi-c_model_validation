# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:02:11 2022

@author: samir
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Script by Erik Cross
"""
#=================================================================#
'''Implementation of matplotlib function & required modules'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import random as r
import math as m
import time as t
import gc
import YSideCalc
import csv
from functions3D_better_figures import next_step_3D

#=================================================================#

'''Setting starting values'''

#start_time = t.process_time()
SumLastOcc = 0
num_dimensions = 2 #int(input("Input dimensions of square: "))
#Sets dimensions of cubes ^
#print("The TADs have dimensions of",num_dimensions,"by",num_dimensions)
num_steps = 9 #int(input("Input number of steps to be taken: "))
print("========================")
#^Sets number of segments for simulation
direction_dict = {}
#^ direction_dict is to keep track of directions taken point by point
#(refreshes for each run)

Current_Run = 0
#Current_Run is a variable used for making sure all possible
#Current_Paths are found per starting point
Current_Path = list()
#List of all coords taken per given Current_Path used to map out Current_Pathing
All_Current_Paths = list()

#For plotting (directions)
graph_directionsx = list()
graph_directionsy = list()
graph_directionsz = list()

#Generates PDF for output:
#outputname = input("Enter Filename: ")
#outputname = outputname+".pdf"
#pdf = PdfPages(outputname)
avgdistance = list()

#Generates text document for "2-cube" distance calculations
text_output = open("squares.txt")

#Only successfully generated 1-cube paths
All_Paths = list()

Two_Cube_List = list()
num_path_found =0
#=================================================================#

'''Autogenerates list of starting points based on dimensions'''
#Autogenerates list of starting points based on dimensions
#Only allows those on z = 1
all_coordinates = list()

for y in range(0,num_dimensions):
    for z in range(0,num_dimensions):
        temp_start_coord = (1,y+1,z+1)
        all_coordinates.append(temp_start_coord)
print(all_coordinates)

#=================================================================#

'''Calculates number of times the program should run based on dimensions:'''
   
    #Example: 3x3 squares (2x3x2)  Based on number of directions
    #                     (3x4x3)  a Current_Path can go per point:
    #                     (2x3x2)  total = 5,184 runs upper limit; not all permisible

#Corners, then length of walls - corners, then middle area (area-perimeter)


Lengths = ((num_dimensions-2)*4)
Inner_Area = (num_dimensions**2)-Lengths-4
# Total_Runs = (2**4)*(3**Lengths)*(4**Inner_Area)

#If wanting to run only 10% of the trial runs
#Total_Runs = Total_Runs/10

#print(Total_Runs)
# if num_dimensions > 3:
#     Total_Runs = Total_Runs/2
   
Total_Runs = 10000 #200000 #((3**8)*6*(4**12))/10
max_found = 5
max_range =  1000

#=================================================================#

'''Function for actually running the program using for/while loops'''
run_num_display = 1
for coord in all_coordinates:
    print("run number",run_num_display,"using coordinate",coord,"\n")
    #print("========================")    
   
    #All_Current_Paths.append(("NEW COORD",coord))
    current_coordinate = coord
    #start_coordinate = current_coordinate

#=====================================================================#  
    #Makes sure the whole loop runs until Total_Runs is reached
    range_counter = 0
    found_counter = 0
    Current_Run = 0
    while (Current_Run < Total_Runs ):
        if (range_counter == max_range):
            print("Found path in current_run: " +str(found_counter) + " / " + str(Current_Run))
            if( found_counter< max_found):
                break
            else:
                range_counter = 0
                found_counter = 0
        range_counter +=1
        #Resets for below program
        current_step = 0
        current_coordinate = coord
        direction_dict = {}
       
        #Resets Path list
        Current_Path = list()
        Current_Path.append(current_coordinate)
        #graph_directions.append(Path.MOVETO)
       
        #Resets fail check
       
#=====================================================================#  
    #Runs to determine next step
        while current_step < num_steps:
            (current_coordinate,current_step,direction_dict) = next_step_3D(current_coordinate,direction_dict,num_dimensions,num_steps,
                           current_step, Current_Path)
                           
        #stop_time = t.process_time()
        #print("Elapsed time is",stop_time-start_time,"\n")

        #print(len(All_Current_Paths))
           
        #Starting Coord for current pathway
        start_coordinate = Current_Path[0]
        start_coordinate_x = start_coordinate[0]
        start_coordinate_y = start_coordinate[1]
        start_coordinate_z = start_coordinate[2]
       
        #Ending Coord for current pathway
        end_coordinate = Current_Path[-1]
        end_coordinate_x = end_coordinate[0]
        end_coordinate_y = end_coordinate[1]
        end_coordinate_z = end_coordinate[2]
       
        #print("Current_Path check",len(Current_Path),Current_Path)
        if len(Current_Path) == num_steps+1:
            #print("Ending list",Current_Path_Mapping)
            #Add ending point rules
           
            if end_coordinate_z == 1 or end_coordinate_z == num_dimensions:
               
                if end_coordinate_x == num_dimensions or end_coordinate_x == 1 and (end_coordinate_y == num_dimensions or end_coordinate_y == 1) or (end_coordinate_z == num_dimensions or end_coordinate_z == 1):
                   
                    if end_coordinate_y == 1 or end_coordinate_y == num_dimensions:
                       
                        if Current_Path not in All_Current_Paths:
                           
                            All_Current_Paths.append(Current_Path)
                           
                            outputline = ((Current_Path),(start_coordinate),(end_coordinate))
                            All_Paths.append(outputline)
                            found_counter += 1

                            # fig = plt.figure()
                            # ax = plt.axes(projection = '3d')
                            # #plt.grid(True, color='r')
                            # #patch = patches.PathPatch(Path, lw=2)
                            # #ax.add_patch(patch)
                            # #ax.set_xlim(0.5, 4.5)
                            # #ax.set_ylim(0.5, 4.5)
                           
                           
                            # for x,y,z in Current_Path:
                            #     graph_directionsx.append(x)
                            #     graph_directionsy.append(y)
                            #     graph_directionsz.append(z)
                            # ax.plot3D(graph_directionsx,graph_directionsy,graph_directionsz, "ro")
                            # ax.plot3D(graph_directionsx,graph_directionsy,graph_directionsz)
                            # plt.xlabel(Current_Path)
                           
                            # #Calculates Distance for Output (NOT DONE YET)
                            # #start_coord = Current_Path[0]
                            # #x1,y1,z1 = start_coord
                            # #end_coord = Current_Path[len(Current_Path)-1]
                            # #x2,y2,z2 = end_coord
                            # #print("start:",start_coord,"end:",end_coord)
                           
                           
                            # #Distance = m.sqrt(((x2-x1)**2)+((y2-y1)**2))
                            # #avgdistance.append(Distance)
                           
                            # #plt.ylabel(Distance)
                           
                            # #pdf.savefig()
                           
                            # plt.show()
                           
                            # #Clear plot
                            # graph_directionsx = list()
                            # graph_directionsy = list()
                            # graph_directionsz = list()
                           





        Current_Run+=1
    run_num_display+=1
   
    #Calculates average of all past coord spots
    #avgdistance = (sum(avgdistance))/len(avgdistance)
    avgdistance = "placeholder"
    #print("Average distance for",coord,"is",avgdistance)
    avgdistance = list()
#=====================================================================#  

    #print(Current_Run,": Number of Attempts Used")
    #print("=============================")
    #print(All_Current_Paths)
   
   
    All_Current_Paths = list()
   
    #print("========================")
num_path_found = len(All_Paths)
#=================================================================#
#=================================================================#
#=================================================================#
'''CLEANING UP MEMORY FOR REST OF SCRIPT'''
del run_num_display
#del Current_Run
del current_step
del Current_Path
#del num_steps
del end_coordinate_x
del end_coordinate_y
del All_Current_Paths
del current_coordinate
del all_coordinates

gc.collect()


All_Paths_Y = YSideCalc.Get_all_paths_start_from_Y(num_dimensions,num_steps,Total_Runs,max_found,max_range)
#=================================================================#
#=================================================================#
#=================================================================#
#=================================================================#
#=================================================================#

'''TEMPORARILY ADDING ANOTHER SCRIPT TO THE END OF THIS ONE.
This means paths will be regenerated (textfile, pdf) every time this script
is run.'''
#print(All_Paths)

i = 1
print("made it to rotating/calc")
for selected_path in All_Paths:  
    #print("Completed selpathway number:",i)

    #Selected_path ending point, and associated x,y values.
    sel_path_end = selected_path[2]
    SPE_x = sel_path_end[0]
    SPE_y = sel_path_end[1]
    SPE_z = sel_path_end[2]
   
    #Value that will be used to determine which "comparison_path" paths are selected.
    i+=1
    if i % 200 == 0:
        with open("CubesY.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(Two_Cube_List[100:101])
        print("\nround: "+ str(i) + "/" + str(len(All_Paths)) )
        Two_Cube_List = list()
    for comparison_path in All_Paths_Y:
        Two_Cube_Line = list()

        #Comparison_path starting point, and associated x,y values.
        comp_path_start = comparison_path[1]
        comp_path_end = comparison_path[2]
        CPS_x = comp_path_start[0]
        CPS_y = comp_path_start[1]
        CPS_z = comp_path_start[2]
     

        #The selected path needs to be ended on the X=num_dimen and comparison path
        #needs to be started in X=1 and match with the selected path's end (both y, z)
        if SPE_y == num_dimensions:
            if (SPE_x == CPS_x and SPE_y+1-num_dimensions == CPS_y and SPE_z == CPS_z):
                new_path = tuple((x,y+num_dimensions,z) for (x,y,z) in comparison_path[0])
                #new_path is the comparison path  which is shifted by the num_dim
                #and its end matches with the start of the selected path
                Two_Cube_Line = selected_path[0],list(new_path)
                #print(selected_path[1], new_start_point)
                Two_Cube_List.append(Two_Cube_Line)
 
        # if SPE_y == num_dimensions:
        #     new_start_point2 = SPE_x,SPE_y+1,SPE_z
        # if SPE_z == num_dimensions:
        #     new_start_point3 = SPE_x,SPE_y,SPE_z+1
        # if SPE_z == 1:
        #     new_start_point3 = SPE_x,SPE_y,SPE_z-1
        # if SPE_y == 1:
        #     new_start_point2 = SPE_x,SPE_y-1,SPE_z  
       

        #if(matching_comp_path_find == True):
           
with open("CubesY.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(Two_Cube_List[0:1])
print("\nround: "+ str(i) + "/" + str(len(All_Paths)) )           
#=================================================================#
'''More Garbage Collection (Memory)'''

# #del rotate_coordinate_list
# del All_Paths
# del Two_Cube_Line
# del comparison_path
# del comp_path_end
# del comp_path_start
# del selected_path
# # del merge_check
# del SPE_x
# del SPE_y
# del SPE_z
# del CPS_x
# del CPS_y
# del CPS_z


# gc.collect()

# #=================================================================#
# #=================================================================#
# #=================================================================#
# '''Calculate 3D Distances and the occurence of them'''
# print("made it to distance")
# Distances_list = list()
# Distances_list_All = list()
# #print(Two_Square_List)
# #normalizing_value = float(input("Enter normalizing value (3.5 for 3x3)"))

# for line in Two_Cube_List:
   
#     #text_output.write("1\n")
   
#     #start and end points for distance calculations
#     Distance=[]
#     for i in range(num_steps+1):
#         sp = line[0][i]
#         spx = sp[0]
#         spy = sp[1]
#         spz = sp[2]
   
#         ep = line[1][i]
#         epx = ep[0]
#         epy = ep[1]
#         epz = ep[2]
   
#         #Distance = m.sqrt(((epx-spx)**2)+((epy-spy)**2)+((epz-spz)**2))
#         Distance.append( m.sqrt(((epx-spx)**2)+((epy-spy)**2)+((epz-spz)**2)))
#     #Distance = Distance/normalizing_value
   
#     Distances_list.append(sum(Distance) / len(Distance))
#     Distances_list_All.append(Distance)
   
# #Creates list of JUST unique distances once per (X axis)
# Distances_x_axis = list(sorted(set(Distances_list)))
# Distances_x_axis_split = list()
# for value in Distances_x_axis:
#     Distances_x_axis_split.append(value)
   
   
# #print(Distances_x_axis)

# #For how many times each distance comes up (Y axis).
# number_num_occurences = list()
# for number in Distances_x_axis:
#     dist_count = (Distances_list.count(number))
#     #num_occurance is multiplying by 4 because of 4 sides which we calclated
#     #onle one of them for simplicity (front, back, up and down)
#     number_num_occurences.append(dist_count*4)
                                 
#     #Distances_Output[number] = dist_count
# #=================================================================#
# print("completed distances")

# #pdf.close()

# Distances_list_All_sorted_by_SD = sorted( [(np.std(l),l) for l in Distances_list_All],   key=lambda x: x[0])

# #print(Distances_x_axis_split,number_num_occurences)
# #print(Distances_list_All)
# with open("DIST_box2.txt", "w") as myfile:
#         #myfile.write("num of run "+str(Current_Run))
#         myfile.write("\nnum path generated"+str(num_path_found))
#         myfile.write("\n=========================\n\n")
#         for line in Distances_x_axis_split:
#             myfile.write(f"{line},")
#         myfile.write(" -> ")
#         for line in number_num_occurences:
#             myfile.write(f"{line},")
#         myfile.write("\n=========================\n\n")
#         counter=0
#         for line in Distances_list_All_sorted_by_SD:
#             counter +=1
#             myfile.write(str(counter)+': ==>  '+ f"{line},\n\n")
#         myfile.write("\n============\n")
       

# SumLastOcc = sum(number_num_occurences)
# text_output.close()
# #print(Two_Cube_List)