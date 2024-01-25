import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles.csv') 

st.header('Anuncios de venta de autos :red_car:', divider='blue')

st.subheader('Tabla de muestra')

#Casilla de verificación para mostrar solo autos nuevos en la tabla de muestra
new_filter = st.checkbox('Mostrarme solo autos nuevos') 

if new_filter: # al marcar la casilla new_filter
        # mostrar el mensaje
        st.write('Muestra ejemplo de 20 autos nuevos')

        # y filtrar la muestra del dataframe para visualizar solo autos nuevos
        st.dataframe(car_data[car_data['condition'] == 'new'].sample(20))
else: 
        st.dataframe(car_data.sample(20))

st.subheader('Marcas de autos en venta')

#Crear una columna que muestre solo la marca del auto, extraida de la columna model
car_data['company'] = car_data['model'].str.split().str[0] 

#Gráfico de barras que muestra la cantidad de autos por marca
company_bar = px.bar(car_data['company'].value_counts(), title= 'Cantidad de autos en venta por Marca')
st.plotly_chart(company_bar, use_container_width=True)

st.subheader('Millas recorridas de los autos en venta')
#Crear una caja desplegable
chart_type = st.selectbox("Selecciona el tipo de gráfico", ["None", "Histograma", "Diagrama de Dispersión"])

if chart_type == "Histograma": # al seleccionar Histograma en el selectbox
        # mostrar el mensaje
        st.write('Histograma para la columna odómetro')
            
        # crear un histograma del kilometraje de los autos anunciados
        hist = px.histogram(car_data, x="odometer", title='Cantidad de millas recorridas por los autos en venta')
        
        # mostrar el gráfico Plotly interactivo
        st.plotly_chart(hist, use_container_width=True)

elif chart_type == "Diagrama de Dispersión": # al hacer clic en el botón scatter
        #mostrar el mensaje
        st.write('Diagrama de dispersión Precio vs Odómetro')

        # crear un diagrama de dispersión 
        odom_price = px.scatter(car_data, x="odometer", y="price", title='Relacion entre las millas recorridas y el precio de los autos en venta')

        # mostrar el gráfico Plotly interactivo
        st.plotly_chart(odom_price, use_container_width=True)
else:
        st.write('Aún no has seleccionado')

st.subheader('Precio de los autos en venta')

#Crear un boton 
price_cond_button = st.button('Comparar Precio vs Condicion')

if price_cond_button: # al hacer clic en price_cond_button
        # mostrar el mensaje
        st.write('Histograma que relaciona los precios de los autos en venta de acuerdo a su condición. Selecciona la condicion de tu interés')

        # crear un histograma de los precios segun la condición del auto
        price_cond = px.histogram(car_data, x= "price", color= "condition", title= 'Frecuencia de precios segun la condición del auto en venta')
        st.plotly_chart(price_cond, use_container_width=True)

#Crear un boton 
price_comp_button = st.button('Comparar Precios entre Marcas')

if price_comp_button: #Al hacer clic en el boton price_comp_button
        # mostrar el mensaje
        st.write('Histograma que relaciona los precios de los autos en venta de acuerdo a la marca. Selecciona la marca de tu interés')
        # crear un histograma de los precios segun la marca del auto
        price_comp = px.histogram(car_data, x= "price", color= "company", title= 'Frecuencia de precios segun la marca de los autos en venta')
        # mostrar el plotly interactivo
        st.plotly_chart(price_comp, use_container_width=True)
