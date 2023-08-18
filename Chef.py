import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="HealthyChef App",
    page_icon="👨‍🍳",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/david-landeo/',
        'Report a bug': "https://www.linkedin.com/in/david-landeo/",
        'About': "Esta app es para la postulación a un puesto de trabajo en PepsiCo.\
            El contenido de esta app no le pertenece a dicha empresa."
    }
)


st.title('Healthy Chef 👨‍🍳')

st.subheader('Tu mejor aplicación con Inteligencia Artificial para comer más sano!')

option = st.selectbox(
    '¿Qué deseas hacer?',
    ('Recetas recomendadas', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.subheader('Uno de nuestros pilares es :blue[Positive Choices]')

st.subheader('Parte del propósito de Positive Choices implica aprovechar nuestras marcas para _educar_ a los consumidores\
            e impulsar acciones positivas.✨')

st.subheader('Sabemos que nuestros productos te acompañan siempre, pero también queremos que te alimentes saludablemente. 💙')

st.subheader('¿Estás listo para comer saludable? 🚀')
