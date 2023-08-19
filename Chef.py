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

"""st.markdown('Esta aplicación te genera una receta** saludable** a partir de los ingredientes que tengas o desees utilizar.\n')
st.markdown('Si no deseas ingresar ningún ingrediente, puedes ver en la parte inferior 👇 las recetas recomendadas. 💯\n ')
st.markdown('En la siguiente campo de entrada de texto enumera los ingredientes que deseas que la inteligencia \
            artificial utilice para tu nueva receta a preparar.')"""

st.markdown('Esta aplicación te genera una receta** saludable** a partir de los ingredientes que tengas o desees utilizar.\n \
            Si no deseas ingresar ningún ingrediente, puedes ver en la parte inferior las recetas recomendadas 💯.\n \
            En la siguiente campo de entrada de texto _enumera_ los _ingredientes_ que deseas que la inteligencia \
            artificial utilice para tu nueva receta a preparar.')


st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

title = st.text_input('Ingredientes', 'Escribe aquí...')


if st.button('Ver recetas recomendadas'):
    option = st.selectbox(
    '¿Qué receta deseas ver?',
    ('Ensalada de Quinua y Aguacate con Salmón a la Parrilla', 'Batido de Avena, Plátano y Fresas', \
     'Lentejas con Espinacas y Tomates'))