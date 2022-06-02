import streamlit as st
import pandas as pd 
import numpy as np 


st.image('data//Logos2.png')




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

st.write('* **Utilizando la ecuación de CIAT 1976, el porcentaje de materia seca para esta muestra es:**')
st.subheader(round(MS1,1))

if float(MS1)<27:
	st.error('**El Porcentaje de materia seca es bajo**')

elif 27.01 <= float(MS1) <= 31.99:
	st.warning('**El Porcentaje de materia seca es promedio**')

elif float(MS1)>= 32:
	st.success('**El Porcentaje de materia seca es alto**')


#Porcentaje de almidón
Alm= float(MS1)*0.8

st.write('* *El almidon de la yuca representa habitualmente entre 80 y 90% de la materia seca, con promedio 87.5%. Por lo tanto el porcentaje aproximado de almidón de esta muestra deberia esta por encima de:*')
st.subheader(round(Alm,2))




st.write('**NOTA**: Los valores calculados en esta página con la ecuación de CIAT 1976 (Kawano et al. 1987; Keating et al. 1981) son indicativos. Para valores más precisos se recomiendan otros métodos tal como secado al horno (105°C por 24 horas) para la materia seca, y determinacion enzimatica de almidon (Holm et al. 1986) para el almidon. Esta herramienta esta a disposicion sin garantía de ningún tipo, ya sea expresa o implícita, incluyendo, pero sin limitarse a, las garantías implícitas de comerciabilidad o pertinencia para un propósito en particular; tanpoco sin garantía alguna en lo que respecta, entre otros, a cualquier daño, pérdida de información, pérdida de beneficios, responsabilidades y/o lesiones causadas por el uso de esta herramienta.')
st.write('-Holm J., Björck I., Drews A., Asp N.G. (1986). A rapid method for the analysis of starch. Starch‐Stärke, 38(7), 224-226.') 
st.markdowm('*Referencias:*')
st.write('-Kawano K., Goncalves Fukuda W.M., Cenpukdee U. (1987). Genetic and environmental effects on dry matter content of cassava root. Crop Science 27, 69-74.') 
st.write('-Keating B.A., Breen A.R., Evenson J.P. (1981). Estimation of Starch and Total Fermentables Content in Storage Roots of Cassava (Manihot esculenta Crantz. Journal of the Science of Food and Agriculture 32, 997-1004.')
	 
st.markdown('*Copyright (C) 2022 CIRAD & CIAT*')
st.markdown('**Authores: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Katia Contreras (kcontreras@agrosavia.co), Thierry Tran (thierry.tran@cirad.fr)**')

