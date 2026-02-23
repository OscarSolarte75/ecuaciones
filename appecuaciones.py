import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Solucionador de Ecuaciones Lineales y Cuadráticas")

tipo = st.selectbox(
    "Seleccione el tipo de ecuación:",
    ["Lineal (ax + b = 0)", "Cuadrática (ax² + bx + c = 0)"]
)

# ECUACIÓN LINEAL

if tipo == "Lineal (ax + b = 0)":
    st.subheader("Ecuación de la forma ax + b = 0")

    a = st.number_input("Ingrese el valor de a:", value=0.0)
    b = st.number_input("Ingrese el valor de b:", value=0.0)

    if st.button("Resolver Lineal"):
        if a == 0:
            st.error("No es una ecuación válida (a no puede ser 0).")
        else:
            x = -b / a
            st.success(f"La solución es: x = {x}")

            # Gráfica
            x_vals = np.linspace(x - 1, x + 1, 400)
            y_vals = a * x_vals + b

            fig, ax_plot = plt.subplots()
            ax_plot.axhline(0)
            ax_plot.axvline(0)
            ax_plot.plot(x_vals, y_vals)
            ax_plot.scatter(x, 0)
            ax_plot.set_title("Gráfica de la ecuación lineal")
            st.pyplot(fig)

# ECUACIÓN CUADRÁTICA

if tipo == "Cuadrática (ax² + bx + c = 0)":
    st.subheader("Ecuación de la forma ax² + bx + c = 0")

    a = st.number_input("Ingrese el valor de a:", value=0.0, key="a2")
    b = st.number_input("Ingrese el valor de b:", value=0.0, key="b2")
    c = st.number_input("Ingrese el valor de c:", value=0.0, key="c2")

    if st.button("Resolver Cuadrática"):
        if a == 0:
            st.error("No es cuadrática (a no puede ser 0).")
        else:
            discriminante = b**2 - 4*a*c
            st.write(f"Discriminante = {discriminante}")

            if discriminante > 0:
                x1 = (-b + np.sqrt(discriminante)) / (2*a)
                x2 = (-b - np.sqrt(discriminante)) / (2*a)
                st.success("Tiene 2 soluciones reales:")
                st.write(f"x1 = {x1}")
                st.write(f"x2 = {x2}")

            elif discriminante == 0:
                x = -b / (2*a)
                st.success("Tiene 1 solución real (raíz doble):")
                st.write(f"x = {x}")

            else:
                st.warning("No tiene soluciones reales (discriminante negativo).")

            # Gráfica
            x_vals = np.linspace(-1, 1, 400)
            y_vals = a*x_vals**2 + b*x_vals + c

            fig, ax_plot = plt.subplots()
            ax_plot.axhline(0)
            ax_plot.axvline(0)
            ax_plot.plot(x_vals, y_vals)
            ax_plot.set_title("Gráfica de la ecuación cuadrática")
            st.pyplot(fig)
