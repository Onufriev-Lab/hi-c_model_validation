
## To Compute $\langle R_s \rangle$

To compute $\langle R_s \rangle$ values from trajectories in mol2 format, run
```
python3 Rs_values_mol2.py
```

To compute $\langle R_s \rangle$ values from trajectories in VTF format,

1. Compile the C++ code:
```
g++ Rs_values_vtf.cpp -std=c++11 -oRs_values_vtf
````
2. Run the C++ code:

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

   Thus, the values would be:  118020, 236040, 354060, ..., (N * 118020)

4. **Add an additional column at the end that represents the average values over each row.**
   
5. **After up-conversion to 10 kb resolution**, you must:
   - Insert an **additional first row** indicating Genomic Distance that correspond to the **bin size** (MC-TAD Algorithm)[micron].
     
   - The first row will start with the  (e.g., `13000`) followed by repeated `0.09` values for each column:

   ```
   13000, 0.09, 0.09, ..., 0.09
   ```

---

### 📊 Input Matrix Illustration

Here’s how the matrix should look **before up-conversion**:

| Genomic_Distance | 1st | 2nd | ... | 10th | avee1
|-----------------------|----------|----------|------|-----------|--------
| 118020                | 0.23     | 0.42     | ...  | 0.35      |  <average_row1>
| 236040                | 0.18     | 0.30     | ...  | 0.27      |   ...
| 354060                | 0.20     | 0.22     | ...  | 0.31      |
| ...                   | ...      | ...      | ...  | ...       |   ...

After **up-conversion to 10 kb resolution**, it will look like:

| Genomic_Distance | 1st | 2nd | ... | 10th | avee1
|-----------------------|----------|----------|------|-----------|----------
| 13000                 | 0.09     | 0.09     | ...  | 0.09      |  <average_row1>
| 118020                | 0.23     | 0.42     | ...  | 0.35      |   ...
| 236040                | 0.18     | 0.30     | ...  | 0.27      |
| 354060                | 0.20     | 0.22     | ...  | 0.31      |
| ...                   | ...      | ...      | ...  | ...       |   ...


## To Compute Relative $\langle R_s \rangle$, C.H. and Relative C.H. with the input data already generated

### 🛠 Setup on Linux
These instructions have been tested on CentOS 7.

Note, these scripts require Python 3.7.3 or higher to run and anaconda3 to manage packages.
To install Anaconda3, crate conda environment and install packages in the newer python version:
```
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
```
Install it by running this: 
```
bash Anaconda3-2024.02-1-Linux-x86_64.sh
```
Run this: 
```
source ~/.bashrc
```
Create a Python 3.7 environment:
```
conda create -n py37 python=3.7
conda activate py37
```
To compute C.H. values
across the genome before incorporate the up-conversion, run
```
python3 Rs_CH_before_UpConversion.py
```
To compute Relative $\langle R_s \rangle$ and Relative C.H. values across the genome after up-conversion, run
```
python3 Relative_Rs_CH.py
```


## References

[1] Ulianov, S.V., Zakharova, V.V., Galitsyna, A.A., ... Gavrilov, A.A., 2021. Order and stochasticity in the folding of individual Drosophila genomes. Nature communications, 12(1), p.41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, ... Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome Biology 18 (2017): 1-22.
