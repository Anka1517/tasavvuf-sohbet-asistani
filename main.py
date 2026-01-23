import streamlit as st

# Sayfa ayarları
st.set_page_config(
    page_title="Tasavvuf Sohbet Asistanı",
    page_icon="🌿",
    layout="centered"
)

# Başlık
st.title("Tasavvuf Sohbet Asistanı")

# Karşılama metni
st.markdown("""
🌿 **Hoş geldiniz.**

Burada, tasavvuf alanında sadece **Ehl-i Sünnet** çizgisinde hazırlanmış,  
sözüne ve ilmine itibar edilen **İslam büyüklerinin**  
nadide eserlerinden izler ve cevaplar bulacaksınız.

Sorularınla gel; acele etme.  
Cevaplar bazen bir cümlede,  
bazen bir susuşta gizlidir.

Niyetini temiz tut,  
sözünü sade söyle.
""")

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
