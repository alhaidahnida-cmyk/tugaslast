import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(page_title="Virtual Lab Vektor 3D", layout="wide")

st.title("🧭 Virtual Lab Matematika – Vektor 3D Interaktif")
st.write("Eksplorasi vektor 3D secara visual dan interaktif agar lebih mudah dipahami.")

# ================= Vektor Input =================
st.sidebar.header("Input Vektor 3D")
Ax = st.sidebar.number_input("A_x", value=1.0)
Ay = st.sidebar.number_input("A_y", value=2.0)
Az = st.sidebar.number_input("A_z", value=3.0)

Bx = st.sidebar.number_input("B_x", value=4.0)
By = st.sidebar.number_input("B_y", value=1.0)
Bz = st.sidebar.number_input("B_z", value=0.0)

A = np.array([Ax, Ay, Az])
B = np.array([Bx, By, Bz])

# ================= Perhitungan =================
dot = np.dot(A, B)
magA = np.linalg.norm(A)
magB = np.linalg.norm(B)
cross = np.cross(A, B)
angle = np.degrees(np.arccos(dot / (magA * magB + 1e-10)))

# ================= Hasil =================
st.subheader("📌 Hasil Perhitungan Vektor 3D")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("‖A‖", f"{magA:.3f}")
    st.metric("A · B (Dot Product)", f"{dot:.3f}")

with col2:
    st.metric("‖B‖", f"{magB:.3f}")
    st.metric("Sudut A-B", f"{angle:.3f}°")

with col3:
    st.write("Cross Product (A × B):")
    st.code(f"({cross[0]:.3f}, {cross[1]:.3f}, {cross[2]:.3f})")

# ================= Visualisasi =================
st.subheader("🎨 Visualisasi Vektor 3D")
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

max_range = max(np.linalg.norm(A), np.linalg.norm(B), np.linalg.norm(cross)) + 1
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, max_range])

# Vektor A, B, Cross
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='blue', label='Vektor A')
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='red', label='Vektor B')
ax.quiver(0, 0, 0, cross[0], cross[1], cross[2], color='green', label='A × B')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

st.pyplot(fig)

# ================= Latihan Soal =================
st.subheader("📘 Latihan Soal Vektor 3D")
import random

if st.button("Generate Soal Baru"):
    P = np.random.randint(-5, 6, size=3)
    Q = np.random.randint(-5, 6, size=3)
    st.write("Hitung dot product dan cross product dari vektor berikut:")
    st.latex(f"P = ({P[0]}, {P[1]}, {P[2]})")
    st.latex(f"Q = ({Q[0]}, {Q[1]}, {Q[2]})")
    st.write("Coba hitung sendiri dulu ya!")
