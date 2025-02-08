import streamlit as st
import requests
import base64
import re

WEBHOOK_URL = os.environ['WEBHOOK_URL']

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Votre nom")
        email = st.text_input("Votre adresse mail")
        
        # Variable pour stocker le statut de participation
        statut_participation = st.radio(
            "Veuillez choisir une option",
            ('Je participe', 'Je ne participe pas')
        )
        
        # Text area pré-rempli selon le statut choisi
        message = st.text_area("Votre message", value='Bien sur que je viens !', key="message")
        
        # Bouton de soumission
        submitted = st.form_submit_button("Confirmer")
        
        if submitted:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon="📧")
                st.stop()

            if not name:
                st.error("Please provide your name.", icon="🧑")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📧")
                st.stop()

            if not message:
                st.error("Please provide a message.", icon="💬")
                st.stop()

            # Prepare the data payload and send it to the specified webhook URL
            data = {"email": email, "name": name, "particpe": statut_participation, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Merci pour votre réponse ! 🎉", icon="🚀")
            else:
                st.error("There was an error sending your message.", icon="😨")
