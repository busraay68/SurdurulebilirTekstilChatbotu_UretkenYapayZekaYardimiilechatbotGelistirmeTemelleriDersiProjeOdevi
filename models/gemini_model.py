# gemini_model.py
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import joblib

class GeminiIntentModel:
    def __init__(self):
        # TF-IDF + Logistic Regression pipeline for intent classification
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=10000)),
            ('clf', LogisticRegression(max_iter=200))
        ])
        self.trained = False
        self.model_path = os.path.join("results", "gemini_trained_model", "gemini_pipeline.pkl")

    def train(self, train_texts, train_labels):
        # Train the pipeline
        self.pipeline.fit(train_texts, train_labels)
        self.trained = True

        # Save the trained pipeline to disk
        save_dir = os.path.dirname(self.model_path)
        os.makedirs(save_dir, exist_ok=True)
        joblib.dump(self.pipeline, self.model_path)
        print(f"Eğitilen model '{self.model_path}' dosyasına kaydedildi.")

    def load(self):
        # Load the trained pipeline from disk
        if os.path.exists(self.model_path):
            self.pipeline = joblib.load(self.model_path)
            self.trained = True
            print(f"Model '{self.model_path}' dosyasından yüklendi.")
        else:
            raise FileNotFoundError(f"Model dosyası bulunamadı: {self.model_path}")

    def predict(self, texts):
        if not self.trained:
            raise ValueError("Model henüz eğitilmedi veya yüklenmedi. Önce train() veya load() metodunu çağırın.")
        return self.pipeline.predict(texts)

    def evaluate(self, texts, true_labels, class_names):
        pred_labels = self.predict(texts)

        precision = precision_score(true_labels, pred_labels, average='weighted', zero_division=0)
        recall = recall_score(true_labels, pred_labels, average='weighted', zero_division=0)
        f1 = f1_score(true_labels, pred_labels, average='weighted', zero_division=0)
        conf_matrix = confusion_matrix(true_labels, pred_labels, labels=class_names)

        os.makedirs("results", exist_ok=True)
        results_path = "results/gemini_results.txt"
        with open(results_path, "w", encoding="utf-8") as f:
            f.write("Performans Sonuçları\n")
            f.write("===================\n")
            f.write(f"Precision: {precision:.4f}\n")
            f.write(f"Recall:    {recall:.4f}\n")
            f.write(f"F1 Score:  {f1:.4f}\n")
            f.write("Karışıklık Matrisi:\n")
            f.write(np.array2string(conf_matrix))
            f.write("\n")
        print(f"Sonuçlar '{results_path}' dosyasına kaydedildi.")

        self.plot_confusion_matrix(conf_matrix, class_names)

        return precision, recall, f1, conf_matrix

    def plot_confusion_matrix(self, cm, class_names):
        plt.figure(figsize=(12,10))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                    xticklabels=class_names, yticklabels=class_names)
        plt.title("Karışıklık Matrisi")
        plt.xlabel("Tahmin Edilen Etiket")
        plt.ylabel("Gerçek Etiket")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    train_df = pd.read_csv("data/train_data.csv")
    test_df = pd.read_csv("data/test_data.csv")

    model = GeminiIntentModel()
    model.train(train_df['text'].tolist(), train_df['labels'].tolist())
    # Eğer eğitimli modeli tekrar kullanmak isterseniz:
    # model.load()

    class_names = sorted(train_df['labels'].unique().tolist())

    precision, recall, f1, conf_matrix = model.evaluate(test_df['text'].tolist(), test_df['labels'].tolist(), class_names)

    print("Gemini Modeli Performans Değerlendirmesi Tamamlandı.")



# python models/gemini_model.py