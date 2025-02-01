import streamlit as st
from assets.utils import contact_form

st.set_page_config(
    page_title="Médéric & Camille",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_GOOGLE_MAPS = st.secrets["API_GOOGLE_MAPS"]

@st.dialog("Répondre à l'invitation")
#@st.experimental_dialog("Répondre à l'invitation")
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
    st.write("Si vous le souhaitez, vous pouvez nous accompagner dans ce début de vie à deux. Nous vous en remercions du fond du coeur.")
    st.link_button("🎁 Notre liste de mariage", "https://www.millemercismariage.com/camedeon/liste.html")
    st.divider()
with col2:
    st.image("assets/image_camedeon.jpeg", use_column_width="auto")

    hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)

st.header("Les lieux")
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("La célébration religieuse aura lieu en l'église de Saint-Gervais et Saint-Protais, à Saint-Gervais (95420):")

    address_eglise = "Rue de l'Église, 95420 Saint-Gervais"
    html_code = f"""
    <div style="width: 100%; height: 300px;">
        <iframe 
            width="100%" 
            height="100%" 
            frameborder="0" 
            loading="lazy"
            style="border:0; width: 100%; height: 100%;"
            src="https://www.google.com/maps/embed/v1/place?key={API_GOOGLE_MAPS}&q={address_eglise}&zoom=15&maptype=roadmap"
        >
        </iframe>
    </div>
    """
    st.components.v1.html(html_code, height=300, width=600)
with col2:
    st.markdown("Réception au Clos Magnitos, à 4 minutes de l'église :")
    address_reception = "Hameau de Magnitot, 1 rue du Prieuré, 95420 Saint-Gervais"
    html_code = f"""
    <div style="width: 100%; height: 300px;">
        <iframe 
            width="100%" 
            height="100%" 
            frameborder="0" 
            loading="lazy"
            style="border:0; width: 100%; height: 100%;"
            src="https://www.google.com/maps/embed/v1/place?key={API_GOOGLE_MAPS}&q={address_reception}&zoom=15&maptype=roadmap"
        >
        </iframe>
    </div>
    """
    st.components.v1.html(html_code, height=300, width=600)

st.divider()
st.header("Le programme")
col1, col_arrow1, col2, col_arrow2, col3, col_arrow3, col4, col_arrow4, col5 = st.columns(
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
)

with col1:
    st.image("assets/eglise.svg", width=100)
    st.subheader("16h")
    st.markdown("Cérémonie religieuse")

with col_arrow1:
    st.markdown("<h1 style='text-align: center;'>→</h1>", unsafe_allow_html=True)

with col2:
    st.image("assets/cocktail.svg", width=100)
    st.subheader("18h")
    st.markdown("Cocktail")

with col_arrow2:
    st.markdown("<h1 style='text-align: center;'>→</h1>", unsafe_allow_html=True)

with col3:
    st.image("assets/diner.svg", width=100)
    st.subheader("20h30")
    st.markdown("Diner")

with col_arrow3:
    st.markdown("<h1 style='text-align: center;'>→</h1>", unsafe_allow_html=True)

with col4:
    st.image("assets/soiree.svg", width=100)
    st.subheader("23h")
    st.markdown("Soirée")

with col_arrow4:
    st.markdown("<h1 style='text-align: center;'>→</h1>", unsafe_allow_html=True)

with col5:
    st.image("assets/brunch.svg", width=100)
    st.subheader("11h")
    st.markdown("Brunch")
