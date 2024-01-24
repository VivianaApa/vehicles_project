import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles.csv') 

st.header('C:\Users\vivia\vehicles_project\vehicles_env\notebooks\vehicles.csv')
hist_button = st.button('./Construir histograma')

if hist_button: # al hacer clic en el botón hist
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
        # crear un histograma
        hist = px.histogram(car_data, x="odometer")
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispersión')

if scatter_button: # al hacer clic en el botón scatter
        #escribir un mensaje
        st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de choches')

        # crear un diagrama de dispersión 
        scat = px.scatter(car_data, x="odometer", y="price")

        # mostrar un gráfico Plotly interactivo
        st.plotly_charts(scat)
