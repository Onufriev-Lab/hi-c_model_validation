## Quantifying Conformational Variability of 3D Genome Organization in Fruit Fly
![Slinkies](figures/slinkies.png)

## MC-TAD Algorithm to refine the representation of the polymer chain from the lower resolution to a higher one

1.  To generate permissible paths inside two cubes in Y+- and Z+- direction using Monte Carlo algorithm, run
```
python3 #1_Distance_4Y_direction.py
```
2. To generate permissible paths inside two cubes in X+ directions, run
```
python3 #2_Distance_X_direction.py
```
3. To extract the unique paths inside two cubes, run
```
python3 #3_Sum4Y_X_unique_4_4_4.py 
```

## To Compute Relative Conformational Diversity

# Conformations in mol2 format:
1. To compute Rs values from trajectories, run
```
python3 Rs_values_mol2.py
```
Conformation files from Ref [1] is [here] https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-020-20292-z/MediaObjects/41467_2020_20292_MOESM4_ESM.zip)

# Conformations in VTF format:
2. To compute Rs values from trajectories, 

Compile the C++ code:
```
g++ Rs_values_vtf.cpp -std=c++11 -oRs_plots
````
Run the C++ code:

```
./Rs_values_vtf <simulation_name>.vtf LamSites_bID_0.txt 0.2 <snapshot_number> <snapshot_number> > <output_file>
```
    
The inputs of the C++ code include the trajectory file, the LamSites text file, and the specific time frame obtained from the selection algorithm. We take a trajectory (one by one);
to each trajectory, we randomly choose a time-slice (a piece) within a tau. For example, the command above assume tau= 1min. The trajectory file in Ref[2] include 400,000 snapshots.
The outputs are the "Rs" values corresponding to each specific genomic distance.

3. To compute and visualize Rs and CV valuse across the genome before incorporate the up-conversion, run
```
python3 Relative_Rs_before_UpConversion.py
```
4. To compute and visualize Relative Rs and relative CV values across the genome after both up-conversion, run
```
python3 Relative_Rs.py
```


## References

[1] Ulianov, S.V., Zakharova, V.V., Galitsyna, A.A., ... Gavrilov, A.A., 2021. Order and stochasticity in the folding of individual Drosophila genomes. Nature communications, 12(1), p.41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, ... Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome Biology 18 (2017): 1-22.

[4] Sexton T, et al. Three-dimensional folding and functional organization principles of the Drosophila genome. Cell. 2012;148(3):458–72

[5] Shi, Guang, and Dave Thirumalai. "Conformational heterogeneity in human interphase chromosome organization reconciles the FISH and Hi-C paradox." Nature communications 10, no. 1 (2019): 3894.

[6] Gürsoy, Gamze, Yun Xu, Amy L. Kenter, and Jie Liang. "Spatial confinement is a major determinant of the folding landscape of human chromosomes." Nucleic acids research 42, no. 13 (2014): 8223-8230.


