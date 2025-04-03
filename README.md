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
1. To compute Rs values from trajectories in mol2 format, run
```
python3 Rs_Traj_mol2.py
```
2. To compute Rs values from trajectories in VTF format,

    generate the bash script to run the an executable file for different trajectories and time scales, run
 ```
python3 #1_generation_single_cells_HiC_10min.py
```
The inputs of the C++ code include the trajectory file, the LamSites text file, and the specific time frame obtained from the selection algorithm. The algorithm is based on a defined "tau" as the maximum age of the Drosophila nuclei. We take a trajectory (one by one);
to each trajectory, we randomly choose a time-slice (a piece) within a tau. For example, the command above assume tau= 1min. The trajectory file in Ref[2] include 400,000 snapshots.
The outputs are the "Rs" values corresponding to each specific genomic distance.
```
  ./<topology_name>.script
```
3. To visualize Rs valuse across the genome before incorporate the up-conversion for Tolokh et. al model, run
```
python3 newDistFig5d_before_shifting_up_down.py
```
4. To visualize Rs values across the genome after both up-conversion and normalization for Tolokh et. al model, run
```
python3 newdistfig5d_New.py
```


## References

[1] Ulianov, S.V., Zakharova, V.V., Galitsyna, A.A., ... Gavrilov, A.A., 2021. Order and stochasticity in the folding of individual Drosophila genomes. Nature communications, 12(1), p.41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, ... Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome Biology 18 (2017): 1-22.

[4] Sexton T, et al. Three-dimensional folding and functional organization principles of the Drosophila genome. Cell. 2012;148(3):458–72

[5] Shi, Guang, and Dave Thirumalai. "Conformational heterogeneity in human interphase chromosome organization reconciles the FISH and Hi-C paradox." Nature communications 10, no. 1 (2019): 3894.

[6] Gürsoy, Gamze, Yun Xu, Amy L. Kenter, and Jie Liang. "Spatial confinement is a major determinant of the folding landscape of human chromosomes." Nucleic acids research 42, no. 13 (2014): 8223-8230.


