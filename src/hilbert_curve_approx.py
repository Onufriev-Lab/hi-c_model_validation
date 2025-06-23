#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:12:10 2025

@author: samir
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# -------------------- User-defined parameters --------------------
p = 4           # Hilbert curve order (edge length = 2**p, total points = 8**p)
NC = 18         # Number of curves to generate
K = 4           # Number of curves to visualize (first K)
NP = 30         # Number of initial points to plot for each curve
SEED = 2025   # RNG seed for reproducibility

# -------------------- Hilbert decoder (canonical) --------------------
def hilbert_points(order):
    """Generate canonical 3D Hilbert curve points (Gray-code method)."""
    n_bits = order
    N = 8 ** order
    coords = np.zeros((N, 3), dtype=int)
    for h in range(N):
        g = h ^ (h >> 1)  # Gray code
        x = y = z = 0
        for i in range(n_bits):
            bit0 = (g >> (3*i))   & 1
            bit1 = (g >> (3*i+1)) & 1
            bit2 = (g >> (3*i+2)) & 1
            x |= bit0 << i
            y |= bit1 << i
            z |= bit2 << i
        coords[h] = (x, y, z)
    # shift origin to (0,0,0)
    return coords.astype(float) - coords[0]

# -------------------- Approximate Hilbert: random orientation per level --------------------
template = np.array([
    [0,0,0],[0,0,1],[0,1,1],[0,1,0],
    [1,1,0],[1,1,1],[1,0,1],[1,0,0]
])

def apply_orientation(pts, perm, flips):
    return pts[:, perm] * flips

def random_hilbert_per_level(order, rng):
    """Approximate Hilbert with one random orientation (perm+flip) per recursion depth."""
    def rec(o, offset):
        # choose orientation for this depth
        perm = tuple(rng.permutation(3))
        flips = tuple(rng.choice([-1, 1], size=3))
        if o == 1:
            return offset + apply_orientation(template, perm, flips)
        pts_list = []
        size = 2 ** (o - 1)
        for idx in range(8):
            corner = apply_orientation(template[[idx]], perm, flips)[0] * size
            pts_list.append(rec(o - 1, offset + corner))
        return np.vstack(pts_list)
    return rec(order, np.zeros(3))

# -------------------- Generate curves --------------------
rng = np.random.default_rng(SEED)
base_curve = hilbert_points(p)
curves = [base_curve] + [random_hilbert_per_level(p, rng) for _ in range(NC-1)]

# -------------------- Plot first K curves (NP points) --------------------
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
colors = ['black','tab:orange','tab:green','tab:purple'] + ['gray']*(K-4)
labels = [f'Curve {i+1}' for i in range(K)]
for i in range(K):
    seg = curves[i][:NP]
    lw = 3 if i == 0 else 1.8
    ax.plot(seg[:,0], seg[:,1], seg[:,2], color=colors[i], lw=lw, label=labels[i])
ax.scatter(0,0,0, s=100, marker='x', color='red', label='Origin')
ax.set_box_aspect([1,1,1])
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()

# -------------------- Compute R(s) --------------------
N = curves[0].shape[0]
s_vals = np.arange(1, N)
Rs = np.vstack([np.array([norm(c[s:] - c[:-s], axis=1).mean() for s in s_vals]) for c in curves])

# -------------------- Compute relative R and sigma_rel --------------------
mean_R = Rs.mean(axis=0)
rel_R = Rs / mean_R
sigma_rel = rel_R.std(axis=0)

# -------------------- Save data to CSV --------------------
# 1) Raw R(s) curves
df_R = pd.DataFrame(Rs.T, index=s_vals, columns=[f'curve_{i+1}' for i in range(NC)])
df_R.index.name = 's'
df_R.to_csv('R_s_curves.csv')

# 2) Relative R(s)
df_rel = pd.DataFrame(rel_R.T, index=s_vals, columns=[f'curve_{i+1}' for i in range(NC)])
df_rel.index.name = 's'
df_rel.to_csv('relative_R_s_curves.csv')

# 3) sigma_rel(s)
df_sigma = pd.DataFrame({'s': s_vals, 'sigma_rel': sigma_rel})
df_sigma.to_csv('relative_sigma_s_2032.csv', index=False)

print("Data saved to:")
print(" - R_s_curves.csv")
print(" - relative_R_s_curves.csv")
print(" - relative_sigma_s_1058.csv")

print("Files will be saved in:", os.getcwd())
