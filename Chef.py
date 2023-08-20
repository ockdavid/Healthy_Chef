import streamlit as st
from PIL import Image
import openai
import recetas

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

hide_menu_style = """
                <style>
                footer {visibility: hidden; }
                </style>
                """
st.markdown(hide_menu_style, unsafe_allow_html=True)

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

st.markdown("Esta aplicación te genera una **receta saludable** a partir de los ingredientes que tengas o desees utilizar.")
st.markdown("Si no deseas ingresar ningún ingrediente, puedes ver en la parte inferior 👇 las recetas recomendadas 💯.")
st.markdown("En la siguiente campo de entrada de texto **_enumera_** los **_ingredientes_** que deseas que la inteligencia \
            artificial utilice para tu nueva receta a preparar y presiona Enter.")

text_input = st.text_input('Ingredientes')

prompt = f"{text_input} es una lista de ingredientes con las cuales vas a realizar \
            una receta saludable incluyendo la preparación, utiliza un lenguaje amigable para comunicar la receta"

if text_input:
        response = get_completion(prompt)
        st.write(response)

if "visibility" not in st.session_state:
    st.session_state.visibility = "hidden"

def click_receta():
     if st.session_state.receta_recogida:
          st.session_state.type=st.session_state.receta_recogida

if st.button('Ver recetas recomendadas'):
    st.session_state.visibility = "visible"
    
st.write(st.session_state.visibility)

option = st.selectbox(
'¿Qué receta deseas ver?',
("Ensalada de Quinua y Aguacate con Salmón a la Parrilla", "Batido de Avena, Plátano y Fresas", \
    "Lentejas con Espinacas y Tomates"), on_change=click_receta, label_visibility=st.session_state.visibility,\
        key='receta_escogida')
    
   # if st.session_state.type == "Lentejas con Espinacas y Tomates":
    #    st.write('lentejas con espinacas')
        