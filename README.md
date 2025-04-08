## Quantifying Conformational Heterogeneity of 3D Genome Organization in Fruit Fly
![Slinkies](figures/slinkies.png)

## To Compute $\langle R_s \rangle$

To compute $\langle R_s \rangle$ values from trajectories in VTF format,

Compile the C++ code:
```
g++ Rs_values_vtf.cpp -std=c++11 -oRs_values_vtf
````
Run the C++ code:

```
./Rs_values_vtf <simulation_name>.vtf LamSites_bID_0.txt 0.2 <snapshot_number> <snapshot_number> > <output_file>
```
 Conformation files from Ref [2] is [here] (http://people.cs.vt.edu/%7Eonufriev/CODES/DROSOPHILA_NUCLEUS.zip)  
 
The inputs of the C++ code include the trajectory file, the LamSites txt file, and the specific time frame obtained from the selection algorithm. We take a trajectory (one by one);
to each trajectory, we randomly choose a time-slice (a piece). The trajectory file in Ref[2] include 400,000 snapshots.
The outputs are the $\langle R_s \rangle$ values corresponding to all genomic distance.

### 🧪 Input Data Preparation

To generate the input matrix for the code, follow these steps:

1. **Run the provided C++ code** using the following command **10 times**, including the snapshot number and the trajectory file name in the names of the snapshots saved in the Conformations_Tolokh_2023 folder:

```
./Rs_values_vtf <simulation_name>.vtf LamSites_bID_0.txt 0.2 <snapshot_number> <snapshot_number> > <output_file>
```

 Repeat this for each run, modifying the output file name accordingly (`column_2.txt`, ..., `column_10.txt`).

2. **Construct the input matrix** by placing all 10 generated columns **side by side** (horizontally). This will result in a matrix with each column representing one run of the code.

3. **Add a genomic distance column** at the **beginning** of the matrix.  
   This column should contain values that are **multiples of the genomic bin size**, calculated as:

   ```
   bin_size = <chromosome_length> / <number_of_TADs> = 118,020 bp
   ```

   So the values would be:

   ```
   118020, 236040, 354060, ..., (N * 118020)
   ```
4. **Add an additional column at the end represent the average values over each row.**
   
5. **After up-conversion to 10 kb resolution**, you must:
   - Insert an **additional first row** indicating the **bin size** (MC-TAD Algorithm)[micron] for each column.
   - The first row will start with the  (e.g., `13000`) followed by repeated `0.09` values for each column:

   ```
   13000, 0.09, 0.09, ..., 0.09
   ```

---

### 📊 Input Matrix Illustration

Here’s how the matrix should look **before up-conversion**:

| Genomic_Distance | Column 1 | Column 2 | ... | Column 10 | avee1
|-----------------------|----------|----------|------|-----------|--------
| 118020                | 0.23     | 0.42     | ...  | 0.35      |  <average_row1>
| 236040                | 0.18     | 0.30     | ...  | 0.27      |   ...
| 354060                | 0.20     | 0.22     | ...  | 0.31      |
| ...                   | ...      | ...      | ...  | ...       |   ...

After **up-conversion to 10 kb resolution**, it will look like:

| Genomic_Distance | Column 1 | Column 2 | ... | Column 10 | avee1
|-----------------------|----------|----------|------|-----------|----------
| 13000                 | 0.09     | 0.09     | ...  | 0.09      |  <average_row1>
| 118020                | 0.23     | 0.42     | ...  | 0.35      |   ...
| 236040                | 0.18     | 0.30     | ...  | 0.27      |
| 354060                | 0.20     | 0.22     | ...  | 0.31      |
| ...                   | ...      | ...      | ...  | ...       |   ...


## To Compute Relative $\langle R_s \rangle$, CV and Relative CV with the input data already generated
To compute CV valuse across the genome before incorporate the up-conversion, run
```
python3 Rs_CV_before_UpConversion.py
```
To compute Relative $\langle R_s \rangle$ and Relative CV values across the genome after up-conversion, run
```
python3 Relative_Rs_CV.py
```


## References

[1] Ulianov, S.V., Zakharova, V.V., Galitsyna, A.A., ... Gavrilov, A.A., 2021. Order and stochasticity in the folding of individual Drosophila genomes. Nature communications, 12(1), p.41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, ... Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome Biology 18 (2017): 1-22.

[4] Sexton T, et al. Three-dimensional folding and functional organization principles of the Drosophila genome. Cell. 2012;148(3):458–72

[5] Shi, Guang, and Dave Thirumalai. "Conformational heterogeneity in human interphase chromosome organization reconciles the FISH and Hi-C paradox." Nature communications 10, no. 1 (2019): 3894.

[6] Gürsoy, Gamze, Yun Xu, Amy L. Kenter, and Jie Liang. "Spatial confinement is a major determinant of the folding landscape of human chromosomes." Nucleic acids research 42, no. 13 (2014): 8223-8230.
