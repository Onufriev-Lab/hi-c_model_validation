## The Spread of Euclidean Distances between Chromatin Loci among Individual Cells at Different Genomic Distances Grants a Robust Approach to Compare Single-Cell Chromatin Models
By Samira Mali, Igor S Tolokh, Erik Cross, Igor V Sharakhov, Alexey V Onufriev


## To compute the Rs plots of the chromatin cinfigurations in your model 
1. Compile the C++ code
```
g++ Rs_plots.cpp -std=c++11 -oRs_plots
```
2. Run the C++ code (Your simulation trajectory file needs to be in vtf format)
```
./Rs_plots simulation.vtf LamSites_bID_0.txt 0.2 72 72 >1st_tau_1min
```
The inputs of the C++ code include the trajectory file, the LamSites text file, the tolerance to reflect the fluctuation of a TAD shape (0.2 or 0.1 micron) and the specific time frame obtained from the selection algorithm. The algorithm is based on a defined "tau" as the maximum age of the Drosophila nuclei. We take a trajectory (one by one);
to each trajectory, we randomly choose a time-slice (a piece) within a tau. For example, the command above assume tau= 1min. The trajectory file in Ref[] include 400,000 snapshots.
The outputs are the "Rs" values corresponding to each specific genomic distance.

3. To generate the bash script to run the cpp code for different trajectories and time scales, run
 ```
python3 generation_single_cells_HiC_10min.py
```
## MC-TAD Algorithm to refine the representation of the polymer chain from the lower resolution to a higher one

1.  To generate permissible paths inside one cube using Monte Carlo algorithm, run
```
python3 3D_new_fast.py
```
2. To continue the paths to the second cube with specified conditions, run
```
python3 secondCube_Box1_fast2.py
```
3. To performs statistical operations on results of MC-TAD, run
```
python3 SumArr.py 
```
## Statistics for results of MC-TAD

1. To obtain the density histogram plot of end-to-end distance of TAD chains from MC-TAD algorithm, run
```   
Rscript hist_with_distribution_line.R
```
2. To fit the values to Gaussian distribution using inverse sampling, run
```
Rscript inverse_sampling_estimate_parameters_Gauss.R
```
3. To see the comparison between the inverse sampling method with actual data distribution to fit to the normal distribution, run
```
Rscript combined_plots_inverse_sampling.R
```
## Comparing different models:
1. To draw the Rs plots with resolution effects before incorporate the shifting process, run
```
python3 newDistFig5d_before_shifting_up_down.py
```
2. To draw Rs plots considering end-to-end distance distribution and resolution effects, run
```
python3 newdistfig5d_New.py
```
3. To compute Rs values with trajectories in mol2 format, run
```
python3 Read_pdb_Rs_Ulianov.py
```
4. To draw Rs plots of Reference [1], both normalized to the TAD size and unnormalized ones (sliding window), run
```
python3 new_fig_5d_Ulianov_1.py
```
5. In order to compute both normalized and unnormalized Rs plots for selected genomic structures in reference [2], run
```
python3 ContactProbability_Alber_unnormalized_with_shift.py
```
6. To calculate the end-to-end distance of the chromatin configurations, run
```
python3 End_to_end_distance_pdb_Ulianov.py
```
7. To compare the end-to-end distance of chromatin configurations, run
```
python3 boxplot_Alber_end_to_end_dist_new__difBox.py
```
8. To calculate the Radius of Gyration for every configuration in vtf format, 
```
g++ RadGyr_Tolokh.cpp -std=c++11 -oRadGyr_Tolokh
./RadGyr_Tolokh simulation.vtf LamSites_bID_0.txt 0.2 1 1 >Rad_Gyr

```
9. To calculate the Radius of Gyration for every configuration in mol2 format
```
python3 Read_pdb_Rg_Ulianov.py
```
10. To compare Radius of Gyration between Ref [1] and ref [2], run
```
python3 Radius_gyration.py
```


## References

[1] Ulianov, S.V., Zakharova, V.V., Galitsyna, A.A., ... Gavrilov, A.A., 2021. Order and stochasticity in the folding of individual Drosophila genomes. Nature communications, 12(1), p.41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, ... Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome Biology 18 (2017): 1-22.

[4] Sexton T, et al. Three-dimensional folding and functional organization principles of the Drosophila genome. Cell. 2012;148(3):458–72

[5] Shi, Guang, and Dave Thirumalai. "Conformational heterogeneity in human interphase chromosome organization reconciles the FISH and Hi-C paradox." Nature communications 10, no. 1 (2019): 3894.

[6] Gürsoy, Gamze, Yun Xu, Amy L. Kenter, and Jie Liang. "Spatial confinement is a major determinant of the folding landscape of human chromosomes." Nucleic acids research 42, no. 13 (2014): 8223-8230.


