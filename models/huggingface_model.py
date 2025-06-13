import os
import numpy as np
import pandas as pd
import torch
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import matplotlib.pyplot as plt
import seaborn as sns


class HFIntentClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, model_name="distilbert-base-uncased", epochs=5, batch_size=16, learning_rate=3e-5,
                 output_dir="./results/hf_trained_model"):
        self.model_name = model_name
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.output_dir = output_dir

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = None
        self.trainer = None
        self.label2id = None
        self.id2label = None
        self.num_labels = None

    class Dataset(torch.utils.data.Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = torch.tensor(self.labels[idx])
            return item

        def __len__(self):
            return len(self.labels)

    def encode_dataset(self, texts, labels):
        encodings = self.tokenizer(texts, truncation=True, padding=True)
        return self.Dataset(encodings, labels)

    def fit(self, X, y):
        unique_labels = sorted(list(set(y)))
        self.label2id = {label: idx for idx, label in enumerate(unique_labels)}
        self.id2label = {idx: label for label, idx in self.label2id.items()}
        self.num_labels = len(unique_labels)

        y_ids = [self.label2id[label] for label in y]

        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name,
            num_labels=self.num_labels,
            id2label=self.id2label,
            label2id=self.label2id
        )

        train_dataset = self.encode_dataset(X, y_ids)

        training_args = TrainingArguments(
            output_dir=self.output_dir,
            num_train_epochs=self.epochs,
            per_device_train_batch_size=self.batch_size,
            per_device_eval_batch_size=self.batch_size,
            learning_rate=self.learning_rate,
            logging_dir=os.path.join(self.output_dir, "logs"),
            logging_steps=20,
            save_total_limit=2,
            seed=42,
            disable_tqdm=False,
            load_best_model_at_end=False
        )

        def compute_metrics(eval_pred):
            logits, labels = eval_pred
            preds = np.argmax(logits, axis=-1)
            precision = precision_score(labels, preds, average='weighted', zero_division=0)
            recall = recall_score(labels, preds, average='weighted', zero_division=0)
            f1 = f1_score(labels, preds, average='weighted', zero_division=0)
            return {'precision': precision, 'recall': recall, 'f1': f1}

        self.trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            compute_metrics=compute_metrics,
        )

        self.trainer.train()

        # Model ve tokenizer'ı kaydet
        os.makedirs(self.output_dir, exist_ok=True)
        self.trainer.save_model(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)

        return self

    def predict(self, X):
        if self.model is None:
            self.load_model()

        self.model.eval()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)

        encodings = self.tokenizer(X, truncation=True, padding=True, return_tensors="pt").to(device)
        with torch.no_grad():
            outputs = self.model(**encodings)
        logits = outputs.logits.cpu().numpy()
        preds = np.argmax(logits, axis=1)
        return [self.id2label[p] for p in preds]

    def load_model(self):
        if os.path.exists(self.output_dir):
            self.tokenizer = AutoTokenizer.from_pretrained(self.output_dir)
            self.model = AutoModelForSequenceClassification.from_pretrained(self.output_dir)
            config = self.model.config
            self.id2label = {int(k): v for k, v in config.id2label.items()}
            self.label2id = {v: int(k) for k, v in self.id2label.items()}
            self.num_labels = len(self.id2label)
        else:
            raise ValueError(f"Model dizini '{self.output_dir}' bulunamadı!")

    def evaluate(self, X, y_true):
        y_pred = self.predict(X)
        precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
        cm = confusion_matrix(y_true, y_pred, labels=sorted(list(set(y_true))))

        os.makedirs("results", exist_ok=True)
        with open("results/hf_results.txt", "w", encoding="utf-8") as f:
            f.write("Performans Sonuçları\n===================\n")
            f.write(f"Precision: {precision:.4f}\nRecall: {recall:.4f}\nF1: {f1:.4f}\n")
            f.write("Karışıklık Matrisi:\n")
            f.write(np.array2string(cm))

        self.plot_confusion_matrix(cm, sorted(list(set(y_true))))

        return precision, recall, f1, cm

    def plot_confusion_matrix(self, cm, class_names):
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
        plt.title('Karışıklık Matrisi')
        plt.xlabel('Tahmin Edilen Etiket')
        plt.ylabel('Gerçek Etiket')
        plt.tight_layout()
        plt.savefig("results/confusion_matrix.png")
        plt.close()


if __name__ == "__main__":
    train_df = pd.read_csv("data/train_data.csv")
    test_df = pd.read_csv("data/test_data.csv")

    print("Train veri örnekleri:")
    print(train_df.head())
    print(f"Train set boyutu: {len(train_df)}, Test set boyutu: {len(test_df)}")

    model = HFIntentClassifier()
    model.fit(train_df['text'].tolist(), train_df['labels'].tolist())

    # Değerlendir
    precision, recall, f1, cm = model.evaluate(test_df['text'].tolist(), test_df['labels'].tolist())

    print(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")


# python models/huggingface_model.py