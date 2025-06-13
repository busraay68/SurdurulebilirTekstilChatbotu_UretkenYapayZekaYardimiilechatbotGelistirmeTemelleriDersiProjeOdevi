import pandas as pd
from sklearn.model_selection import train_test_split

# 📌 Excel dosyasını oku
file_path = "data/chatbot_dataset.xlsx"  # Güncellenmiş dosya yolu
df = pd.read_excel(file_path)

# 📌 Sütun adlarını Hugging Face formatına uygun hale getir
df = df.rename(columns={"KategoriAdi": "labels", "Cumle": "text"})  # Model için uygun sütun isimleri

# 📌 Train ve test verisini ayır
train_data, test_data = train_test_split(df, test_size=0.2, stratify=df["labels"], random_state=42)

# 📌 Dosyaları kaydet (UTF-8 formatında)
train_data.to_csv("data/train_data.csv", index=False, encoding="utf-8")
test_data.to_csv("data/test_data.csv", index=False, encoding="utf-8")

print("✅ Veri başarıyla ayrıldı: train_data.csv ve test_data.csv dosyaları oluşturuldu.")

# python utils/traintestayrimi.py çalıştırmak için