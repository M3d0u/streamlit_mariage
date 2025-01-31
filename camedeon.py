import streamlit as st
from assets.utils import contact_form

st.set_page_config(
    page_title="Médéric & Camille",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_GOOGLE_MAPS = st.secrets["API_GOOGLE_MAPS"]

@st.experimental_dialog("Répondre à l'invitation")
def show_contact_form():
    contact_form()

col1, col2 = st.columns([2, 3])
with col1:
    st.title("Médéric & Camille")
    st.subheader("Le samedi 6 septembre 2025")
    st.markdown('##')
    st.markdown("Rendez-vous en l'église de Saint-Gervais et Saint-Protais, à Saint-Gervais (95420), à 16h :")


    # pip install folium geopy
    address = "Rue de l'Église, 95420 Saint-Gervais"

    # Generate the Google Maps URL
    map_url = f"https://www.google.com/maps/embed/v1/place?key={API_GOOGLE_MAPS}&q={address}&zoom=15&maptype=roadmap"

    # Create the HTML template for the iframe
    html_code = f"""
    <div style="width: 100%; height: 300px;">
        <iframe 
            width="100%" 
            height="100%" 
            frameborder="0" 
            loading="lazy"
            style="border:0; width: 100%; height: 100%;"
            src="{map_url}"
        >
        </iframe>
    </div>
    """

    # Display the map in Streamlit
    st.components.v1.html(html_code, height=300)

    st.markdown('##')
    col1_bis, col2_bis = st.columns([2, 2])
    with col1_bis:
        st.link_button("🎁 Notre liste de mariage", "https://www.millemercismariage.com/camedeon/liste.html")
    with col2_bis:
        if st.button("✉️ Répondre à l'invitation"):
            show_contact_form()
with col2:
    st.image("assets/image_camedeon.jpeg", width=900)

    hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)







