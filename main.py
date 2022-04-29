import streamlit as st
import pandas as pd 
import numpy as np 


st.image('data//Logos.png')




#Titulo
st.write("""
# Herramienta para medir el porcentaje de materia seca de yuca 

Esta herramienta permite calcular el porcentaje de materia seca de la yuca. Para esto, es necesario registrar el peso exacto de una muestra de yuca (aproximadamente 5 kg), y el peso de esta misma muestra sumergida en el agua. En el siguiente video se puede observar un ejemplo del procedimiento
""")


#insert video


st.video('data//materiaseca2.mp4')


#insert variables


st.subheader('A continuación ingresar los pesos:')

PS = st.number_input('Peso de la yuca sin sumergir en agua (gr)', 4500,6000)
PA = st.number_input('Peso de yuca sumergida en agua (gr)', 200,800)

#Inicio de ecuación

#Gravedad específica (parte de abajo de la ecuacuación)

GEd = int(PS) - int(PA)

#resultado de gravedad específica

RG = int(PS) / int(GEd)


# Ecuaciación de materia seca 

MS1 = 158.26 * float(RG) - 142.05

st.write('* **Utilizando la ecuación de CIAT et al., (1976), el porcentaje de materia seca para esta muestra es:**')
st.subheader(round(MS1,2))

if float(MS1)<30:
	st.error('**El Porcentaje de materia seca es muy bajo**')

elif 34 > float(MS1) >= 30:
	st.warning('**El Porcentaje de materia seca es aceptable**')

elif float(MS1)>= 34:
	st.success('**El Porcentaje de materia seca es alto**')


#Porcentaje de almidón
Alm= float(MS1)*0.875

st.write('* *En promedio el almidón de la yuca representa el 87,5% de la materia seca, por lo tanto se puede concluir que el % de almidón de esta muestra es igual a:*')
st.subheader(round(Alm,2))






st.markdown('*Copyright (C) 2022 CIRAD & CIAT*')
st.markdown('**Authors: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Thierry Tran (thierry.tran@cirad.fr)**')

