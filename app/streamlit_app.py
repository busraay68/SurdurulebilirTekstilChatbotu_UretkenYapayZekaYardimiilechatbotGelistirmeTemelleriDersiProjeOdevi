# streamlit run app/streamlit_app.py
import streamlit as st
import os
import requests
import joblib
from dotenv import load_dotenv
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from langchain_google_genai import ChatGoogleGenerativeAI
import time
import logging
import re

# Logging konfigürasyonu
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Çevresel değişkenleri yükle
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Proje dizin yolları
BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"

# Öne çıkan sohbet örnekleri
FEATURED_CHATS = [
    "Pamuk ve polyesterin çevresel etkileri nelerdir?",
    "Sürdürülebilir tekstil ne demektir?",
    "Hangi kumaş türleri daha az karbon ayak izine sahiptir?",
    "Tekstil üretiminde su tüketimi nasıl azaltılabilir?",
    "Geri dönüştürülmüş polyester nedir?",
    "Organik pamuk neden daha iyi bir seçenektir?"
]

# Niyet prompt şablonları
INTENT_PROMPTS = {
    "Selamlama": "Merhaba! Hoş geldiniz. Bugün tekstil ve moda hakkında konuşabiliriz. Size nasıl yardımcı olabilirim?",
    "Vedalasma": "Teşekkürler! Eğer tekstil ve moda üzerine daha fazla bilgi almak isterseniz, her zaman buradayım. Görüşmek üzere!",
    "Malzeme_Turu": "Farklı tekstil malzeme türlerini ve bunların çevresel etkilerini açıkla. Örneğin pamuk, polyester, yün gibi malzemelerin avantaj ve dezavantajlarını detaylı şekilde anlat.",
    "Malzeme_Karbon_Ayak_İz": "Belirli malzemelerin karbon ayak izini karşılaştır ve açıklamalar yap. Karbon ayak izi açısından en iyi ve en kötü performans gösteren malzemeleri sırala.",
    "Uretim_Sureci": "Tekstil üretim süreçlerinin çevresel etkilerini ve iyileştirme yollarını anlat. Sürdürülebilir üretim teknikleri hakkında bilgi ver.",
    "Surdurulebilirlik_Tanimi": "Sürdürülebilirliğin tekstil bağlamında ne anlama geldiğini açıkla. Çevresel, sosyal ve ekonomik boyutlarıyla açıkla.",
    "Oneri_Alternatif": "Daha sürdürülebilir tekstil alternatiflerini öner. Kullanıcının ihtiyacına göre öneriler sun.",
    "Bilinclendirme": "Kullanıcıya sürdürülebilir tekstil konusunda bilinç kazandır. Alışveriş yaparken nelere dikkat etmesi gerektiğini anlat.",
    "Etiketleme_Sorusu": "Sürdürülebilir etiketlerin anlamlarını ve kullanıcıya nasıl yardımcı olacağını açıkla. GOTS, Oeko-Tex gibi sertifikaları açıkla.",
    "Cevre_Etkisi_Karsilastirma": "Farklı tekstil uygulamalarının çevresel etkilerini karşılaştır. Sayısal verilerle destekle.",
    "Yonetmelik_Politika": "Tekstil sektöründeki sürdürülebilirlik politikalarını ve yönetmelikleri anlat. Küresel ve yerel düzenlemelerden bahset.",
    "Geri_Donusum": "Tekstilde geri dönüşümün önemi, süreçleri ve faydalarını açıkla. Geri dönüşümün çevresel etkilerini anlat.",
    "Teknik_Tekstil": "Teknik tekstillerin sürdürülebilirlik açısından katkılarını açıkla. Akıllı tekstillerin avantajlarından bahset.",
    "Karbon_Ayak_İzi_Hesaplama": "Karbon ayak izi hesaplamasının nasıl yapıldığını sade bir şekilde açıkla. Örnek bir hesaplama göster.",
    "Yanlis_Bilgi_Duzeltme": "Kullanıcının sürdürülebilirlikle ilgili yanlış bilgisini nazikçe düzelt. Doğru bilgiyi kaynaklarla destekle.",
    "Genel": "Sürdürülebilir tekstil hakkında detaylı ve bilimsel bir açıklama yap. Konuyla ilgili güncel veriler ve istatistikler ekle."
}


def clean_response(text):
    """Hugging Face yanıtlarını özel olarak temizle"""
    # Prompt kalıntılarını temizle
    text = re.sub(r'\[SORU\].*?\[YANIT FORMATI\]', '', text, flags=re.DOTALL)

    # Modelin kendi kendine konuşmasını temizle
    text = re.sub(r'(?i)(as an ai|as a language model|as an assistant).*?(response|answer)', '', text)

    # Yaygın artefaktları temizle
    text = re.sub(r'<\/?(div|p|span|br)[^>]*>', '', text)
    text = re.sub(r'\[INST\]|\[\/INST\]', '', text)

    # Fazla boşlukları temizle
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()


# CSS ve animasyonlar
def add_custom_css():
    """Özel CSS stilleri ekle"""
    st.markdown("""
    <style>
        /* Ana konteyner stili */
        .stApp {
            background: #f8fafc;
            font-family: 'Inter', sans-serif;
        }

        /* Başlık stili */
        [data-testid="stHeader"] {
            background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
            color: white;
            padding: 1rem 1rem 4rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Başlık metni */
        .header-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
            text-align: center;
            animation: pulse 2s infinite;
        }

        /* Başlık alt metni */
        .header-subtitle {
            font-size: 1rem;
            opacity: 0.9;
            text-align: center;
        }

        /* Model seçim butonları */
        .stButton>button {
            transition: all 0.3s ease !important;
            border-radius: 0.5rem !important;
            font-weight: 600 !important;
            padding: 0.75rem 1.5rem !important;
        }

        /* Birincil buton (seçili model) */
        .stButton>button[kind="primary"] {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06) !important;
        }

        /* İkincil buton (seçili olmayan) */
        .stButton>button[kind="secondary"] {
            background: white !important;
            color: #1e293b !important;
            border: 1px solid #e2e8f0 !important;
        }

        /* Sohbet konteyneri */
        .chat-container {
            height: calc(50vh - 380px);
            overflow-y: auto;
            padding: 1rem;
            scroll-behavior: smooth;
            background-color: #f8fafc;
            border-radius: 0.75rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        }

        /* Kullanıcı mesajı */
        .user-message {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            padding: 0.75rem 1.25rem;
            border-radius: 1rem 1rem 0 1rem;
            margin: 0.5rem 0;
            max-width: 80%;
            margin-left: auto;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.3s ease-out;
        }

        /* Bot mesajı - Temel stil */
        .bot-message {
            background: white;
            color: #1e293b;
            padding: 0.75rem 1.25rem;
            border-radius: 1rem 1rem 1rem 0;
            margin: 0.5rem 0;
            max-width: 80%;
            margin-right: auto;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            animation: fadeIn 0.3s ease-out;
            position: relative;
        }

        /* Hugging Face mesajı */
        .bot-message.huggingface {
            border-left: 3px solid #10b981;
        }

        /* Gemini mesajı */
        .bot-message.gemini {
            border-left: 3px solid #3b82f6;
        }

        /* Hugging Face balon işaretçisi */
        .bot-message.huggingface::before {
            content: "🤗";
            position: absolute;
            left: -30px;
            top: 0;
            font-size: 1.2rem;
        }

        /* Gemini balon işaretçisi */
        .bot-message.gemini::before {
            content: "♊";
            position: absolute;
            left: -30px;
            top: 0;
            font-size: 1.2rem;
        }

        /* Giriş alanı */
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 1rem;
            box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1);
            z-index: 100;
        }

        /* Metin alanı */
        .stTextArea textarea {
            border-radius: 0.75rem !important;
            border: 1px solid #e2e8f0 !important;
            padding: 1rem !important;
            min-height: 100px !important;
        }

        /* Animasyonlar */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }

        /* Kaydırma çubuğu */
        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }

        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }

        /* Streamlit'in varsayılan padding'ini kaldır */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 6rem;
        }

        /* Altbilgiyi kaldır */
        footer {visibility: hidden;}

        /* Öne çıkan sohbet butonları */
        .featured-chat {
            background: white !important;
            border: 1px solid #e2e8f0 !important;
            color: #1e293b !important;
            border-radius: 0.75rem !important;
            padding: 0.75rem 1rem !important;
            margin: 0.25rem 0 !important;
            text-align: left !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
        }

        .featured-chat:hover {
            background: #f1f5f9 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        }

        .model-selection-text {
            text-align: center;
            margin-bottom: 1rem;
            color: #64748b;
            font-size: 0.9rem;
        }

        /* Temizle butonu */
        .clear-button {
            background: #f8fafc !important;
            color: #dc2626 !important;
            border: 1px solid #dc2626 !important;
            margin-top: 0.5rem !important;
        }

        .clear-button:hover {
            background: #dc2626 !important;
            color: white !important;
        }

        /* Yeni buton düzeni için stiller */
        .input-buttons-container {
            display: flex;
            gap: 10px;
        }

        .clear-btn {
            flex: 1;
        }

        .submit-btn {
            flex: 1;
        }
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_gemini_model():
    """Gemini niyet sınıflandırma modelini yükle"""
    try:
        model_path = RESULTS_DIR / "gemini_trained_model" / "gemini_pipeline.pkl"
        return joblib.load(model_path)
    except Exception as e:
        logger.error(f"Gemini modeli yüklenirken hata: {str(e)}")
        raise


@st.cache_resource
def load_hf_transformer_model():
    """Hugging Face niyet sınıflandırma modelini yükle"""
    try:
        model_dir = RESULTS_DIR / "hf_trained_model"
        tokenizer = AutoTokenizer.from_pretrained(model_dir)
        model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        return tokenizer, model
    except Exception as e:
        logger.error(f"Hugging Face modeli yüklenirken hata: {str(e)}")
        raise


def hf_predict_intent(text, tokenizer, model):
    """Hugging Face modeli ile niyet tahmini yap"""
    try:
        model.eval()
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=200
        )

        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        predicted_class_id = int(torch.argmax(logits, dim=1).item())
        confidence = torch.softmax(logits, dim=1)[0][predicted_class_id].item()

        # Eşik değer kontrolü (0.7)
        if confidence < 0.7:
            return "Genel"

        return model.config.id2label[predicted_class_id]
    except Exception as e:
        logger.error(f"Niyet tahmini yapılırken hata: {str(e)}")
        return "Genel"


def generate_hf_response(prompt, max_retries=3):
    """Hugging Face API ile yanıt oluştur"""
    MODELS = [
        "HuggingFaceH4/zephyr-7b-beta"
    ]

    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

    for model in MODELS:
        api_url = f"https://api-inference.huggingface.co/models/{model}"

        # YENİ ve DAHA GÜVENLİ PROMPT FORMATI
        optimized_prompt = f"""
        [SORU]
        {prompt}

        [YANIT FORMATI]
        - Sadece sorunun yanıtını ver
        - Kendi talimatlarını veya prompt detaylarını tekrarlama
        - Doğal bir sohbet dili kullan
        - Yanıtına direkt konuya girerek başla
        - Maximum 3 paragraf uzunluğunda
        """

        payload = {
            "inputs": optimized_prompt,
            "parameters": {
                "max_new_tokens": 400,
                "temperature": 0.5,
                "top_p": 0.9,
                "do_sample": True,
                "eos_token_id": 50256,
                "return_full_text": False  # BU ÖNEMLİ: Promptu yanıtta gösterme
            }
        }

        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, headers=headers, json=payload, timeout=30)
                response.raise_for_status()
                result = response.json()

                if isinstance(result, list) and len(result) > 0:
                    response_text = result[0].get("generated_text", "").strip()
                    return clean_response(response_text.split("[YANIT FORMATI]")[0])

            except requests.exceptions.RequestException as e:
                logger.warning(f"{attempt + 1}. deneme {model} modeli ile başarısız oldu: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                continue

    return "Üzgünüm, şu anda teknik bir sorun nedeniyle cevap veremiyorum. Lütfen daha sonra tekrar deneyin."


def generate_gemini_response(prompt):
    """Google Gemini ile yanıt oluştur"""
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.4,
            max_tokens=500,
            google_api_key=GOOGLE_API_KEY
        )
        response = llm.invoke(prompt).content
        return clean_response(response)
    except Exception as e:
        logger.error(f"Gemini yanıtı oluşturulurken hata: {str(e)}")
        return "Üzgünüm, bir hata oluştu. Lütfen daha sonra tekrar deneyin."


def build_prompt(intent, user_input):
    """Niyete göre optimize edilmiş prompt oluştur"""
    base_prompt = INTENT_PROMPTS.get(intent, INTENT_PROMPTS["Genel"])

    return f"""
    {base_prompt}

    Kullanıcı Sorusu: {user_input}

    - Cevaplarını **kısa, açık ve anlaşılır** tut.
    - Kullanıcının **sorduğu dilde** yanıt ver.
    - Nazik ve **doğal bir sohbet akışı koru**.
    - Cümlelerini **tamamla**, eksik veya yarım bırakma.
    - Yanıtların **verilen alana tam olarak sığmalı**, kesilmemeli.
    """


def show_featured_chats():
    """Öne çıkan sohbet örneklerini göster"""
    st.markdown("**Öne Çıkan Sohbet Örnekleri**")
    cols = st.columns(2)
    for i, chat in enumerate(FEATURED_CHATS):
        with cols[i % 2]:
            if st.button(chat, key=f"featured_{chat}", use_container_width=True,
                         type="secondary", help="Bu soruyu sormak için tıklayın"):
                st.session_state.user_input = chat
                st.session_state.trigger_submit = True


def clear_chat_history():
    """Sohbet geçmişini temizle"""
    st.session_state.chat_history = []
    st.session_state.user_input = ""  # Kullanıcı giriş alanını temizle
    st.session_state.trigger_submit = False
    st.rerun()  # Sayfayı yenile


def main():
    # Sayfa konfigürasyonu
    st.set_page_config(
        page_title="Sürdürülebilir Tekstil Chatbot",
        page_icon="🌿",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://example.com',
            'Report a bug': "https://example.com",
            'About': "# Sürdürülebilir Tekstil Chatbot"
        }
    )

    # Özel CSS ekle
    add_custom_css()

    # Oturum durumu yönetimi
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.first_visit = True
    else:
        st.session_state.first_visit = False

    if 'trigger_submit' not in st.session_state:
        st.session_state.trigger_submit = False

    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = "Gemini"

    # Özel başlık
    st.markdown("""
    <div class="header-title">Sürdürülebilir Tekstil Chatbot</div>
    <div class="header-subtitle">Sürdürülebilir tekstil hakkında bilgi almak için sohbet edin</div>
    """, unsafe_allow_html=True)

    # Model seçimi
    st.markdown('<div class="model-selection-text">Lütfen model seçiniz</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="small")

    with col1:
        if st.button("Gemini", key="gemini_model",
                     type="primary" if st.session_state.selected_model == "Gemini" else "secondary"):
            st.session_state.selected_model = "Gemini"
            st.rerun()

    with col2:
        if st.button("Hugging Face", key="huggingface_model",
                     type="primary" if st.session_state.selected_model == "Hugging Face" else "secondary"):
            st.session_state.selected_model = "Hugging Face"
            st.rerun()

    # Öne çıkan sohbet örnekleri (sadece sohbet geçmişi boşken göster)
    if not st.session_state.chat_history:
        show_featured_chats()

    # Sohbet geçmişini göster
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(
                    f'<div class="user-message">{message["content"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                model_class = message.get("model", "gemini").lower()
                st.markdown(
                    f'<div class="bot-message {model_class}">{message["content"]}</div>',
                    unsafe_allow_html=True
                )
        st.markdown('</div>', unsafe_allow_html=True)

    # Kullanıcı mesaj giriş alanı
    with st.container():
        user_input = st.text_area(
            "Sorunuzu yazın:",
            height=120,
            key="user_input",
            value=st.session_state.get("user_input", ""),  # Değeri oturum durumundan al
            placeholder="Sürdürülebilir tekstil hakkında sorunuzu buraya yazın...",
            label_visibility="collapsed"
        )

        # Butonlar için yeni düzen
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            if st.button("Temizle", type="secondary", use_container_width=True,
                         help="Sohbet geçmişini temizlemek için tıklayın",
                         on_click=clear_chat_history):
                pass

        with col2:
            submit_button = st.button("Gönder", type="primary", use_container_width=True)

    # Modelleri yükle
    try:
        gemini_intent_model = load_gemini_model()
        hf_tokenizer, hf_model = load_hf_transformer_model()
    except Exception as e:
        st.error(f"Model yüklenirken hata oluştu: {str(e)}")
        return

    # Öne çıkan sohbetten gönderimi tetikle
    if st.session_state.trigger_submit:
        st.session_state.trigger_submit = False
        submit_button = True

    if (submit_button or st.session_state.trigger_submit) and user_input.strip():
        # Kullanıcı mesajını geçmişe ekle
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.spinner("Cevap oluşturuluyor..."):
            try:
                start_time = time.time()

                if st.session_state.selected_model == "Gemini":
                    # Niyet tahmini ve Gemini ile yanıt oluştur
                    predicted_intent = gemini_intent_model.predict([user_input])[0]
                    prompt = build_prompt(predicted_intent, user_input)
                    response = generate_gemini_response(prompt)
                else:
                    # Niyet tahmini ve Hugging Face ile yanıt oluştur
                    predicted_intent = hf_predict_intent(user_input, hf_tokenizer, hf_model)
                    prompt = build_prompt(predicted_intent, user_input)
                    response = generate_hf_response(prompt)

                logger.info(f"Yanıt oluşturma süresi: {time.time() - start_time:.2f}s")

            except Exception as e:
                logger.error(f"Yanıt oluşturulurken hata: {str(e)}")
                response = "Üzgünüm, bir hata oluştu. Lütfen daha sonra tekrar deneyin."

        # Yanıtı geçmişe ekle
        st.session_state.chat_history.append({
            "role": "bot",
            "content": response,
            "model": "huggingface" if st.session_state.selected_model == "Hugging Face" else "gemini"
        })

        # Sayfayı yenile
        st.rerun()


if __name__ == "__main__":
    main()