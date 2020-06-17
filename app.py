
####librerias para usar funciones
import pandas as pd ###--tablas
import streamlit as st ##--convertir codigo python en htlm(web)
from PIL import Image ##--muestra imágenes
from streamlit import caching ###--guarda en memoria cache.

##llamar al banner
image = Image.open('banner.jpg')
st.image(image, caption='',use_column_width=True)

##llamar al logo
image = Image.open('logo.jpg')
st.sidebar.image(image, caption='',use_column_width=True)


html_temp = """
				<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
				<h1 style="color:white;text-align:center;">Inputs de base</h2>
				</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

##tipo de calculo
#st.sidebar.title('¿Qué buscas?')
#tipo=st.sidebar.selectbox("¿Qué buscas?",("Calcular agentes", "Calcular base"))

st.sidebar.title('¿Cantidad de base?')
Qbase=st.sidebar.number_input("Qbase", min_value=1000, max_value=2000000, step=1000, format=None, key=None)

st.sidebar.title('¿Cuantos intentos?')
vueltas=st.sidebar.slider('intentos', min_value=0.0, max_value=20.0, value=3.0, step=0.1, format=None, key=None)

st.sidebar.title('¿Contactabilidad sobre base?')
C=st.sidebar.slider('contactabilidad', min_value=0, max_value=100, value=50, step=1, format=None, key=None)

st.sidebar.title('¿Efectividad sobre base?')
E=st.sidebar.slider('efectividad', min_value=0.0, max_value=50.0, value=5.0, step=0.1, format=None, key=None)

html_temp = """
				<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
				<h1 style="color:white;text-align:center;">Inputs de eficiencia</h2>
				</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

st.sidebar.title('¿TMO Venta?')
TMOV=st.sidebar.number_input("Minutos ", min_value=1, max_value=60, step=1, format=None, key=None)

st.sidebar.title('¿TMO Contacto?')
TMOC=st.sidebar.number_input("Minutos", min_value=1, max_value=60, step=1, format=None, key=None)

st.sidebar.title('¿TMO No Contacto?')
TMONOC=st.sidebar.number_input("segundos", min_value=1, max_value=100, step=1, format=None, key=None)


st.sidebar.title('Ocupación')
OCUPACION=st.sidebar.slider('En porcentaje', min_value=1, max_value=100, value=80, step=1, format=None, key=None)

st.sidebar.title('Adherencia')
ADHERENCIA=st.sidebar.slider('En porcentaje ', min_value=1, max_value=100, value=80, step=1, format=None, key=None)

html_temp = """
				<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
				<h1 style="color:white;text-align:center;">Dias</h2>
				</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)


st.sidebar.title('Dias laborables')
DIAS=st.sidebar.number_input("dias", min_value=1, max_value=31, step=1, format=None, key=None)

st.sidebar.title('jornada laboral')
JORNADA=st.sidebar.number_input("horas", min_value=1, max_value=8, step=1, format=None, key=None)


#st.write('**Dias laborables**')
#DIAS=st.multiselect(label="seleccionar uno",options=['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SETIEMBRE'])

#@st.cache(persist=False,allow_output_mutation=True)
def datos():
	C1= (Qbase*(C/100)*(E/100)* TMOV)
	C2= Qbase*(C/100)*(1-(E/100))* TMOC
	C3= (Qbase*(1-C/100)*vueltas*TMONOC)/60	
	TOTALHORAS=(C1+C2+C3)/60
	HORASASESOR=DIAS*JORNADA
	QASESORES=TOTALHORAS/HORASASESOR
	return(QASESORES)


def main():
	if st.button("**CALCULAR**"):
		inferior=round(datos()*0.95)
		central=round(datos())
		superior=round(datos()*1.05)
		st.write('**result inferior**: %s' % inferior)
		st.write('**result central**: %s' % central)
		st.write('**result superior**: %s' % superior)


if __name__ == '__main__':
	main()

st.button('Rerun')
