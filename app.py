import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles.csv') 

st.header('Anuncios de venta de autos :red_car:', divider='blue')

st.title('Tabla de datos')
tabla = st.dataframe(car_data.sample(20))
new_filter = st.checkbox('new')
if new_filter:
        st.write('Visualizar una muestra solo de los autos nuevos')

        tabla['condition'[tabla['condition']== 'new']]


build_histogram = st.checkbox('Histograma')
if build_histogram: # al hacer clic en el botón hist
        # escribir un mensaje
        st.write('Construir un histograma para la columna odómetro')
            
        # crear un histograma del kilometraje de los autos anunciados
        hist = px.histogram(car_data, x="odometer")
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist, use_container_width=True)

build_scatter = st.checkbox('Diagrama de dispersión')
if build_scatter: # al hacer clic en el botón scatter
        #escribir un mensaje
        st.write('Construir un diagrama de dispersión que relacione la distancia recorrida (odómetro), con el precio del auto')

        # crear un diagrama de dispersión 
        scat = px.scatter(car_data, x="odometer", y="price")

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(scat, use_container_width=True)
