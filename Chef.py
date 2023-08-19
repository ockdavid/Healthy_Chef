import streamlit as st
from PIL import Image
import openai

st.set_page_config(
    page_title="HealthyChef App",
    page_icon="👨‍🍳",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/david-landeo/',
        'Report a bug': "https://www.linkedin.com/in/david-landeo/",
        'About': "Esta app solo es para ver recetas saludables, \
          no reemplaza las labores de un nutricionista"
    }
)

# openai.api_key  = os.getenv('OPENAI_API_KEY')
openai.api_key = st.secrets["api_secret"]

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.4, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

st.title('Healthy Chef 👨‍🍳')

st.subheader('Tu mejor aplicación con Inteligencia Artificial para comer más sano!')

option = st.selectbox(
    '¿Qué deseas ver/hacer?',
    ('Recetas recomendadas', 'Preparar recetas'))

st.write('You selected:', option)

if st.button('Ver recetas recomendadas'):
    response = get_completion(prompt)
    lista = response
    st.write(response)