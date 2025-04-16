
## To Compute $\langle R_s \rangle$

To compute $\langle R_s \rangle$ values from snapshots in "mol2" format, run
```
python3 Rs_values_mol2.py
```
The input file name with the data and the output file name are specified inside the script.

To compute $\langle R_s \rangle$ values from trajectories in "vtf" format,

![Built with C++](https://img.shields.io/badge/Built%20with-C%2B%2B11-blue?style=flat-square&logo=c%2B%2B&logoColor=white)

## 🧩 Dependencies

- A **C++11 compatible compiler**, such as `g++`
- POSIX-compliant environment (Linux/macOS)
- No external libraries required

> Note: A "C++11 compatible compiler" means any compiler that supports the C++11 standard or newer (e.g., C++14, C++17, C++20) will also work.

---

## ⚙️ Compiling

To compile the code, run:

```
g++ Rs_values_vtf.cpp -std=c++11 -o Rs_values_vtf
````

## 🚀 Usage

Run the executable with the following command:

```
./Rs_values_vtf <simulation_file.vtf> <LamSites_bID_0.txt> <tolerance> <start_snapshot> <end_snapshot> > <output_file>
````
### Arguments

- `<simulation_file.vtf>`: Trajectory file in VTF format
- `<LamSites_bID_0.txt>`: file contains the radius size information of each TAD.
- `<tolerance>`: According to Ref [2], **bead-bead contact** is defined as the configuration where the distance between the centers of the two beads, *d<sub>ij</sub>*, is less than *r<sub>i</sub> + r<sub>j</sub> + 0.2 µm*.
- `<start_snapshot>`: First snapshot index to include
- `<end_snapshot>`: Last snapshot index to include
- `<output_file>`: Output file to store results (use redirection `>`)

---

### Example

```
./Rs_values_vtf example_sim.vtf LamSites_bID_0.txt 0.2 500 500 > Rs_output.csv
````
This analyzes snapshot 500 from example_sim.vtf and writes the results to Rs_output.csv


Conformation files from Ref [2] is [here] (http://people.cs.vt.edu/%7Eonufriev/CODES/DROSOPHILA_NUCLEUS.zip)  

The outputs are the $\langle R_s \rangle$ values corresponding to all genomic distance.

### 🧪 Input Data Preparation

To generate the input matrix for the code, follow these steps:

1. **Run the provided C++ code** using the following command **10 times**, including the snapshot number and the trajectory file name in the names of the snapshots saved in the Conformations_Tolokh_2023 folder:

```
./Rs_values_vtf <simulation_file>.vtf LamSites_bID_0.txt 0.2 <snapshot_number> <snapshot_number> > <output_file>
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
| 118020                | 0.23     | 0.23     | ...  | 0.23      |  <average_row1>
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
To install Anaconda3, create conda environment and install packages in the newer python version:
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
Create a Python 3.7.3 environment:
```
conda create -n py373 python=3.7.3
conda activate py373
```
Now you can install required packages using conda install or pip. In case your base python version is 3.11.7, you will not need to install the required packages (e.g. numpy, pandas, etc.)

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

[1] Ulianov, Sergey V., Vlada V. Zakharova, Aleksandra A. Galitsyna, Pavel I. Kos, Kirill E. Polovnikov, Ilya M. Flyamer, Elena A. Mikhaleva et al. "Order and stochasticity in the folding of individual Drosophila genomes." Nature communications 12, no. 1 (2021): 41.

[2] Tolokh, Igor S., Nicholas Allen Kinney, Igor V. Sharakhov, and Alexey V. Onufriev. "Strong interactions between highly dynamic lamina-associated domains and the nuclear envelope stabilize the 3D architecture of Drosophila interphase chromatin." Epigenetics & Chromatin 16, no. 1 (2023): 1-25.

[3] Li, Qingjiao, Harianto Tjong, Xiao Li, Ke Gong, Xianghong Jasmine Zhou, Irene Chiolo, and Frank Alber. "The three-dimensional genome organization of Drosophila melanogaster through data integration." Genome biology 18 (2017): 1-22.

