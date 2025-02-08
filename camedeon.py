import streamlit as st
from assets.utils import contact_form, image_to_base64

st.set_page_config(
    page_title="Médéric & Camille",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_GOOGLE_MAPS = os.environ['API_GOOGLE_MAPS']

@st.dialog("Répondre à l'invitation")
def show_contact_form():
    contact_form()

#st.balloons()
col1, col2 = st.columns([2, 3])
with col1:
    title = '<p style="font-family:Source Sans Pro, sans-serif;    font-weight: 600; font-size: 80px;">Médéric & Camille</p>'
    
    st.markdown(title, unsafe_allow_html=True)
    st.subheader("Le samedi 6 septembre 2025")
    st.markdown('##')
    st.write("N'oubliez pas de nous répondre, avant le **5 juillet 2025** !")
    if st.button("✉️ Répondre à l'invitation"):
        show_contact_form()

    st.divider()
    st.header("Notre liste de mariage")
    st.write("Si vous le souhaitez, vous pouvez nous accompagner dans ce début de vie à deux !")
    st.link_button("🎁 Notre liste de mariage", "https://www.millemercismariage.com/camedeon/liste.html")
    st.divider()
with col2:
    st.image("assets/image_camedeon.jpeg", use_container_width="auto")

    hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)

st.header("Les lieux")
col1, col2 = st.columns([1, 1])

# Define a function to generate dynamic HTML for embedding Google Maps
def generate_html(address):
    return f"""
    <div style="width: 100%; height: 300px;">
        <iframe 
            width="100%" 
            height="100%" 
            frameborder="0" 
            loading="lazy"
            style="border:0; width: 100%; height: 100%;"
            src="https://www.google.com/maps/embed/v1/place?key={API_GOOGLE_MAPS}&q={address}&zoom=15&maptype=roadmap"
        >
        </iframe>
    </div>
    """

with col1:
    st.markdown("### Célébration religieuse")
    st.markdown("La célébration religieuse aura lieu en l'église de Saint-Gervais et Saint-Protais, à Saint-Gervais (95420):")

    address_eglise = "Rue de l'Église, 95420 Saint-Gervais"
    st.components.v1.html(generate_html(address_eglise), height=300)

with col2:
    st.markdown("### Réception")
    st.markdown("Réception au Clos Magnitos, à 4 minutes (en voiture) de l'église :")

    address_reception = "Hameau de Magnitot, 1 rue du Prieuré, 95420 Saint-Gervais"
    st.components.v1.html(generate_html(address_reception), height=300)


st.divider()

st.header("Le programme")

# Define columns with proportionally smaller arrow columns
col1, col2, col3, col4, col5 = st.columns(
    [1, 1, 1, 1, 1]
)

with col1:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/svg+xml;base64,{image_to_base64("assets/eglise.svg")}" width="150">
        </div>
        <p style='text-align: center;'>16h - Cérémonie religieuse</p>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/svg+xml;base64,{image_to_base64("assets/cocktail.svg")}" width="150">
        </div>
        <p style='text-align: center;'>18h - Cocktail</p>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/svg+xml;base64,{image_to_base64("assets/diner.svg")}" width="150">
        </div>
        <p style='text-align: center;'>20h30 - Dîner</p>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/svg+xml;base64,{image_to_base64("assets/soiree.svg")}" width="150">
        </div>
        <p style='text-align: center;'>23h - Soirée</p>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/svg+xml;base64,{image_to_base64("assets/brunch.svg")}" width="150">
        </div>
        <p style='text-align: center;'>11h - Brunch</p>
    """, unsafe_allow_html=True)
