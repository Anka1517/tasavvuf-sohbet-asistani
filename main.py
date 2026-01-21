import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Tasavvuf Sohbet Asistanı")

st.title("🌿 Tasavvuf Sohbet Asistanı")

lang = st.selectbox(
    "Dili seç / Select language / Pilih bahasa",
    ["Türkçe", "English", "Bahasa Indonesia"]
)

system_prompts = {
    "Türkçe": "Sen tasavvuf ehli bir mürşidsin. Cevaplarını yumuşak, hikmetli ve öğretici bir üslupla ver.",
    "English": "You are a Sufi spiritual guide. Respond with wisdom, humility, and compassion.",
    "Bahasa Indonesia": "Anda adalah pembimbing sufi. Jawablah dengan kebijaksanaan dan ketenangan."
}

user_input = st.text_area(
    "Sorunuzu yazınız" if lang == "Türkçe" else "Write your question"
)

if st.button("Gönder"):
    if user_input.strip() == "":
        st.warning("Lütfen bir soru yazınız.")
    else:
        with st.spinner("Cevap hazırlanıyor..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompts[lang]},
                    {"role": "user", "content": user_input}
                ]
            )
            st.markdown("### 🌱 Cevap")
            st.write(response.choices[0].message.content)
