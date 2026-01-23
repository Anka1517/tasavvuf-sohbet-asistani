import os
import time
import streamlit as st
from openai import OpenAI

# ---- Sayfa Ayarları ----
st.set_page_config(page_title="Tasavvuf Sohbet Asistanı", layout="centered")

st.title("Tasavvuf Sohbet Asistanı")

st.markdown("""
🌿 **Hoş geldiniz.**

Burada, tasavvuf alanında sadece **Ehl-i Sünnet** çizgisinde hazırlanmış,  
sözüne ve ilmine itibar edilen **İslam büyüklerinin**  
nadide eserlerinden izler ve cevaplar bulacaksınız.

Sorularınla gel; acele etme.  
Cevaplar bazen bir cümlede,  
bazen bir susuşta gizlidir.

**Niyetini temiz tut,  
sözünü sade söyle.**

🕊️ *Sormak istediğin bir mesele varsa:*  
**Sırra açılan kapı, edep ile aralanır.**
""")

# ---- Gazali Metinlerini Yükle ----
def load_texts():
    base_path = "data/gazali"
    texts = ""
    for file in os.listdir(base_path):
        with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
            texts += f.read() + "\n\n"
    return texts

gazali_texts = load_texts()

# ---- OpenAI ----
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---- Soru Alanı ----
question = st.text_area("Sorunuzu edep ile yazınız:", height=100)

if st.button("Sor"):
    if question.strip() == "":
        st.warning("Soru boş olmaz.")
    else:
        with st.spinner("Cevap hazırlanıyor…"):
            time.sleep(1.5)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Sen İmam-ı Gazâlî çizgisinde, edepli, kısa, "
                            "acele etmeyen bir tasavvuf sohbet asistanısın. "
                            "Modern yorum yapmazsın."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Kaynak metinler:\n{gazali_texts}\n\nSoru: {question}"
                    }
                ],
                temperature=0.4
            )

            st.markdown("### 🌿 Cevap")
            st.write(response.choices[0].message.content)
