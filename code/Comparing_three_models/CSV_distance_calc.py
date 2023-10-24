import numpy as np
import math as m
import csv
from sklearn.metrics import euclidean_distances

def average_each_item(lst):
    num_lists = len(lst)
    num_items = len(lst[0])
    averages = []

    for i in range(num_items):
        total = 0
        for j in range(num_lists):
            total += lst[j][i]
        averages.append(total / num_lists)
    return averages

with open('CubesX_2x2.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    Two_Cube_List = list(csv_reader)

num_steps = len(list(eval(Two_Cube_List[0][0])))

'''Calculate 3D Distances and the occurence of them'''
print("made it to distance")
Distances_list = list()
Distances_list_All = list()
All_paths = list()
#print(Two_Square_List)
#normalizing_value = float(input("Enter normalizing value (3.5 for 3x3)"))

for line in Two_Cube_List:
    
    #text_output.write("1\n")
    #list(eval(Two_Cube_List[0][0]))
    #start and end points for distance calculations
    Distance=[]
    l1 =eval(line[0])
    l2 =eval(line[1])
    All_paths.append(l1+l2)
    for i in range(num_steps):
        
        sp = l1[i]
        spx = sp[0]
        spy = sp[1]
        spz = sp[2]
    
        ep = l2[i]
        epx = ep[0]
        epy = ep[1]
        epz = ep[2]
    
        #Distance = m.sqrt(((epx-spx)**2)+((epy-spy)**2)+((epz-spz)**2))
        Distance.append( m.sqrt(((epx-spx)**2)+((epy-spy)**2)+((epz-spz)**2)))
    #Distance = Distance/normalizing_value
    
    Distances_list.append(sum(Distance) / len(Distance))
    Distances_list_All.append(Distance)
    
#Creates list of JUST unique distances once per (X axis)
Distances_x_axis = list(sorted(set(Distances_list)))
Distances_x_axis_split = list()
for value in Distances_x_axis:
    Distances_x_axis_split.append(value)
    
    
#print(Distances_x_axis)

#For how many times each distance comes up (Y axis).
number_num_occurences = list()
for number in Distances_x_axis:
    dist_count = (Distances_list.count(number))
    number_num_occurences.append(dist_count*4)#dist_count needs to multiply by 4 in y axis
                                 
    #Distances_Output[number] = dist_count
#=================================================================#
print("completed distances")

#pdf.close()
Distances_list_All_sorted_by_SD = sorted( [(np.std(l),l) for l in Distances_list_All],   key=lambda x: x[0])
# Distance Map to compare bonded and non-bonded configurations
distances = np.zeros((16, 16), dtype=float)
for i in range(len(All_paths)):
    centerList = np.array(All_paths[i])
    #0.08 scales the size of cube edge in case we do not assume 
    distances = distances + euclidean_distances(centerList)*0.08

distances = distances/len(All_paths)
print(" average distances: " , distances)
print(" average: " , average_each_item(Distances_list_All))

#print(Distances_x_axis_split,number_num_occurences)
#print(Distances_list_All)
with open("DIST_box1.txt", "w") as myfile:
        # myfile.write("num of run"+str(Current_Run))
        myfile.write("\n=========================\n\n")
        for line in Distances_x_axis_split:
            myfile.write(f"{line},")
        myfile.write(" -> ")
        for line in number_num_occurences:
            myfile.write(f"{line},")
        myfile.write("\n=========================\n\n")
        counter=0
        for line in Distances_list_All_sorted_by_SD:
            counter +=1
            myfile.write(str(counter)+': ==>  '+ f"{line},\n\n")
        myfile.write("\n============\n")
        

SumLastOcc = sum(number_num_occurences)
#print(Two_Cube_List)
