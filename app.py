import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
from io import BytesIO

st.title("Concordia Celes Hotel Anket")

# --- Anket Formu ---
isim = st.text_input("Adınız")
memnuniyet = st.radio("Otel hizmetlerinden memnun musunuz?", ["Evet", "Hayır"])
yorum = st.text_area("Yorumunuz")

if st.button("Gönder"):
    st.success("Teşekkürler! Yanıtınız kaydedildi.")
    df = pd.DataFrame([[isim, memnuniyet, yorum]], columns=["İsim","Memnuniyet","Yorum"])
    df.to_csv("anket_sonuclari.csv", mode='a', index=False, header=False)

# --- QR Kod Oluşturma ---
app_url = "https://share.streamlit.io/arminkochac-cloud/Concordia-Celes-Hotel-Anket/main/app.py"
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(app_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Streamlit Cloud uyumu için BytesIO kullanıyoruz
buf = BytesIO()
img.save(buf, format="PNG")
buf.seek(0)

st.image(buf, caption="QR Kod ile Anketi Aç", use_column_width=True)