import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Archivo donde se guardan las reservas en tu servidor
ARCHIVO_DATOS = "reservas.csv"

st.set_page_config(page_title="Ingersoll - Sala de Reuniones", layout="centered")

st.title("🏢 Gestión de Sala de Reuniones")
st.subheader("Ingersoll Argentina - Planta Monte Maíz")

# Función para guardar
def guardar_reserva(n, m, f, h):
    nueva_fila = pd.DataFrame([[n, m, f, h]], columns=["Nombre", "Motivo", "Fecha", "Hora"])
    if not os.path.isfile(ARCHIVO_DATOS):
        nueva_fila.to_csv(ARCHIVO_DATOS, index=False)
    else:
        nueva_fila.to_csv(ARCHIVO_DATOS, mode='a', header=False, index=False)

# --- Lógica de la interfaz ---
st.success("### ✅ SALA DISPONIBLE") 
st.divider()

tab1, tab2 = st.tabs(["📅 Reservar Ahora", "📋 Ver Cronograma"])

with tab1:
    with st.form("reserva_form"):
        nombre = st.text_input("Quién solicita:")
        motivo = st.text_input("Motivo de la reunión:")
        fecha = st.date_input("Día:", datetime.now())
        hora = st.time_input("Hora de inicio:")
        
        if st.form_submit_button("Confirmar Reserva"):
            if nombre and motivo:
                guardar_reserva(nombre, motivo, fecha, hora)
                st.balloons() # ¡Un poco de festejo por la reserva!
                st.success(f"¡Listo loquito! Reserva guardada para {nombre}.")
            else:
                st.warning("Por favor, completá todos los campos.")

with tab2:
    if os.path.exists(ARCHIVO_DATOS):
        df = pd.read_csv(ARCHIVO_DATOS)
        st.table(df)
    else:
        st.write("No hay reservas cargadas todavía.")