import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st


# Importación de plotly.graph_=objects como go

# Leer los datos del archivo CSV
car_data = pd.read_csv("vehicles_us.csv")
# creacion de encabezado
st.header("Datos de Anuncios de Coches")
# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion')

if disp_button:

    st.write("Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches")

    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

# Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

# Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)
