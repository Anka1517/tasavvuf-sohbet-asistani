import streamlit as st
import time

# --- Sayfa Ayarları ---
st.set_page_config(
    page_title="Tasavvuf Sohbet Asistanı",
    layout="centered"
)

# --- Başlık ve Karşılama ---
st.title("Tasavvuf Sohbet Asistanı")

st.markdown("""
🌿 **Hoş geldiniz.**

Burada, tasavvuf alanında sadece **Ehl-i Sünnet** çizgisinde hazırlanmış,  
sözüne ve ilmine itibar edilen **İslam büyüklerinin**  
nadide eserlerinden izler ve cevaplar bulacaksınız.

Sorularınla gel; acele etme.  
Cevaplar bazen bir cümlede,  
bazen bir susuşta gizlidir.

*Niyetini temiz tut,  
sözünü sade söyle.*
""")

st.divider()

# --- Soru Alanı ---
st.markdown("### 🕊️ Sormak istediğin bir mesele varsa:")

soru = st.text_area(
    label="",
    placeholder="Kalbine düşen soruyu buraya yaz…",
    height=120
)

# --- Sor Butonu ---
if st.button("🌿 Sor"):
    if soru.strip() == "":
        st.warning("Lütfen önce bir soru yaz.")
    else:
        st.markdown("### 📜 Cevap")

        cevap = (
            "Bu sualin cevabı, ilimden önce edepte gizlidir.\n\n"
            "Hak yolunda arayan kimse bilir ki;\n"
            "her soru hemen cevap bulmaz.\n\n"
            "Bazen beklemek, cevabın kendisidir."
        )

        # --- Yavaş ve edepli yazım ---
        cevap_alani = st.empty()
        yazilan = ""

        for harf in cevap:
            yazilan += harf
            cevap_alani.markdown(yazilan)
            time.sleep(0.04)

st.divider()

# --- Alt Not ---
st.markdown(
    "<div style='text-align:center; font-size:0.9em; color:gray;'>"
    "Sırra açılan kapı, edep ile aralanır."
    "</div>",
    unsafe_allow_html=True
)


# Görsel
st.image(
    "https://i.imgur.com/your_image_here.jpg",
    caption="Sırra açılan kapı",
    use_container_width=True
)

# --- OpenAI entegrasyonu ŞİMDİLİK KAPALI ---
# İleride burası adım adım açılacak
#
# import os
# from openai import OpenAI
#
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
# OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "").strip()
#
# client = OpenAI(
#     api_key=OPENAI_API_KEY,
#     base_url=OPENAI_BASE_URL if OPENAI_BASE_URL else None
# )



#import os
#from openai import OpenAI
#import streamlit as st

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
#OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "").strip()

#client = OpenAI(
#    api_key=OPENAI_API_KEY,
#    base_url=OPENAI_BASE_URL if OPENAI_BASE_URL else None
#)
