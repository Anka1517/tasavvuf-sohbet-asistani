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
