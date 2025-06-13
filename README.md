Sürdürülebilir Tekstil Alanında Yapay Zekâ Destekli Chatbot Geliştirilmesi

Proje Konusu

Bu proje, sürdürülebilir tekstil konusunda uzmanlaşmış, yapay zekâ destekli bir sohbet botu geliştirme sürecini kapsamaktadır. Temel amacı, kullanıcıların tekstil malzemeleri, üretim süreçleri, çevresel etkiler ve sürdürülebilir alternatifler gibi konulardaki sorularına doğru ve hızlı yanıtlar verebilen bir yapay zekâ asistanı oluşturmaktır. Proje kapsamında, belirli niyet (intent) türlerine dayalı bir veri seti hazırlanmış, farklı Büyük Dil Modelleri (LLM) ile eğitim gerçekleştirilmiş ve bu modellerin performansları karşılaştırmalı olarak değerlendirilmiştir.

Proje Akışı 

Projenin geliştirme süreci, aşağıdaki adımları içeren sistematik bir yaklaşımla ilerlemiştir:

Veri Toplama → Intent Oluşturma → Veri Seti Hazırlama → Model Eğitimi → Performans Değerlendirme → Uygulama Geliştirme → Kullanıcı Arayüzü → Değerlendirme

Bu akış, projenin her aşamasında net hedefler belirleyerek, geliştirme sürecini verimli bir şekilde yönetmeyi sağlamıştır.


Intent'lerin Oluşturulması ve Veri Seti Paylaşımı

Proje kapsamında, chatbot'un anlayabilmesi ve doğru yanıt verebilmesi için 15 farklı niyet (intent) kategorisi belirlenmiştir. Bu intent'ler, sürdürülebilir tekstil ve moda alanındaki yaygın kullanıcı sorularını kapsayacak şekilde özenle seçilmiştir. Niyetlerin oluşturulması sürecinde, ChatGPT gibi yapay zekâ destekli araçlardan faydalanılarak daha kapsamlı ve çeşitli ifade biçimleri elde edilmiştir. Belirlenen intent'ler ve bazı örnekleri aşağıdadır:

Selamlama: Kullanıcıların sohbeti başlatma ifadeleri.

Vedalaşma: Sohbeti sonlandırma ifadeleri.

Malzeme_Türü: Farklı tekstil malzemeleri hakkında bilgi edinme.

Malzeme_Karbon_Ayak_İzi: Belirli malzemelerin karbon ayak izini sorgulama.

Üretim_Süreci: Tekstil üretim süreçleri ve etkileri hakkında sorular.

Sürdürülebilirlik_Tanımı: Sürdürülebilir tekstilin ne anlama geldiği.

Öneri_Alternatif: Sürdürülebilir alternatifler veya ürün önerileri.

Bilinçlendirme: Kullanıcıların sürdürülebilirlik konusunda bilinçlenmesine yönelik sorular.

Etiketleme_Sorusu: Sürdürülebilirlik etiketleri ve sertifikaları hakkında bilgi.

Çevre_Etkisi_Karşılaştırma: Farklı uygulamaların çevresel etkilerini karşılaştırma.

Yönetmelik_Politika: Sektördeki sürdürülebilirlik politikaları ve yönetmelikler.

Geri_Dönüşüm: Tekstilde geri dönüşümün önemi ve süreçleri.

Teknik_Tekstil: Teknik tekstillerin sürdürülebilirliğe katkıları.

Karbon_Ayak_İzi_Hesaplama: Karbon ayak izi hesaplama yöntemleri.

Yanlış_Bilgi_Düzeltme: Kullanıcının yanlış bilgilerini düzeltme.


Veri Seti Paylaşımı

📌 Bu çalışma kapsamında geliştirilen Türkçe dilindeki intent sınıflandırma veri seti, sürdürülebilirlik ve karbon ayak izi temalı bir sohbet botu eğitimi amacıyla oluşturulmuştur. Bilimsel katkı ve yeniden kullanım amacıyla veri seti, Kaggle platformunda herkese açık olarak paylaşılmıştır.

Kaggle Veri Seti Başlığı: Turkish Intent Dataset for Sustainable Textile Chatbot

Kaggle Linki: https://www.kaggle.com/datasets/busraodev/tekstil-srdrlebilirlik-chatbotu-veri-seti

Lisans: CC BY-SA 4.0 (Atıf + Aynı Lisansla Paylaş)

Kaggle, veri bilimcileri için önemli bir platformdur ve Türkçe veri setlerinin paylaşılması, yerel çözümlerin geliştirilmesine katkı sağlamaktadır. 

Kaggle'a Veri Yükleme Adımları:

Kaggle'a veri seti yüklemek oldukça basittir, ancak bazı güvenlik adımları (örneğin telefon doğrulaması) gerekebilir:
Kaggle Hesabı Oluşturma: İlk olarak Kaggle.com adresinden bir hesap oluşturun veya mevcut hesabınızla giriş yapın.
Veri Seti Sayfasına Gitme: Ana sayfada "Datasets" sekmesine tıklayın.
Yeni Veri Seti Oluşturma: Sağ üst köşedeki "New Dataset" butonuna tıklayın.
Dosyaları Yükleme: Veri setinizi oluşturan dosyaları (örn. chatbot_dataset.xlsx) sürükleyip bırakın veya seçerek yükleyin.
Meta Veri Girişi: Veri setinize bir başlık (örneğin "Turkish Intent Dataset for Sustainable Textile Chatbot"), bir açıklama ve etiketler ekleyin. Bu bilgiler, veri setinizin bulunabilirliğini artırır.
Lisans Seçimi: Veri setinizin kullanım koşullarını belirleyen bir lisans seçin (örn. CC BY-SA 4.0).
Yayınlama: Tüm bilgiler doğru olduğunda "Publish" butonuna tıklayarak veri setinizi yayınlayın. 

Veri Seti Yapısı (Train-Test Ayrımı)
Hazırlanan veri seti, modelin gerçek dünya senaryolarında ne kadar iyi genelleme yapabildiğini ölçmek amacıyla eğitim (train) ve test kümelerine ayrılmıştır. Bu ayrım, modelin aşırı öğrenmesini (overfitting) engellemek ve performansının objektif bir şekilde değerlendirilmesini sağlamak için kritik öneme sahiptir. Projemizde, orijinal Excel dosyası (chatbot_dataset.xlsx), traintestayrimi.py adlı özel bir Python betiği kullanılarak %80 eğitim verisi (train_data.csv) ve %20 test verisi (test_data.csv) oranında CSV formatına dönüştürülerek ayrılmıştır. Bu ayrılan dosyalar, sohbet botunun eğitilmesi ve daha sonra bağımsız olarak performansının test edilmesi için kullanılmıştır.

Proje İçin Kullanılan Modeller ve Eğitim Süreçleri

Projede, iki ana işlev için farklı model yaklaşımları benimsenmiştir:

Niyet Sınıflandırma (Intent Classification): Kullanıcının girdisini projenin 15 intent kategorisinden birine atamak için kendi veri setimizle eğitilmiş veya ince ayarlanmış modeller kullanılmıştır.

Yanıt Üretimi (Response Generation): Sınıflandırılan niyete ve kullanıcının sorusuna uygun, doğal dilde cevaplar üretmek için büyük, genel amaçlı dil modellerinin (LLM) API'leri kullanılmıştır.

Bu iki aşamada kullanılan modeller ve eğitim süreçleri aşağıda detaylandırılmıştır.

A. Niyet Sınıflandırma Modelleri ve Eğitimi

Niyet sınıflandırma için iki farklı model türü değerlendirilmiş ve eğitilmiştir: Gemini için geleneksel bir makine öğrenimi yaklaşımı ve Hugging Face için derin öğrenme tabanlı bir Transformer modeli. Bu modeller, projenin özelleşmiş Türkçe intent veri seti üzerinde eğitilmiş ve performansı değerlendirilmiştir.

1. Gemini Niyet Sınıflandırma Modeli (Yerel Eğitim)

Model Tipi: TF-IDF (Term Frequency-Inverse Document Frequency) ve Lojistik Regresyon bileşenlerinden oluşan bir makine öğrenimi pipeline'ı kullanılmıştır. Bu yaklaşım, metin verilerini sayısal özellik vektörlerine dönüştürür (TF-IDF) ve ardından bu vektörleri kullanarak intent'leri sınıflandırmak için Lojistik Regresyon algoritmasını uygular.

Seçim Nedeni: Bu model, hızlı eğitim süresi, nispeten daha az hesaplama kaynağı gerektirmesi ve küçük/orta ölçekli metin sınıflandırma görevlerinde etkili olması nedeniyle tercih edilmiştir. Bu, projenin ilk aşamalarında hızlı prototipleme ve temel performans değerlendirmeleri için ideal bir seçenek sunmuştur.

Eğitim Süreci: Model, data/train_data.csv dosyasındaki eğitim verileri kullanılarak models/gemini_model.py betiği çalıştırılarak eğitilmiştir. Eğitim tamamlandıktan sonra, eğitilmiş pipeline (Pipeline objesi) disk üzerine .pkl uzantılı bir dosya olarak (results/gemini_trained_model/gemini_pipeline.pkl) kaydedilmiştir. Bu sayede, model bir kez eğitildikten sonra tekrar tekrar eğitilmesine gerek kalmadan doğrudan yüklenerek kullanılabilir.

Eğitim Komutu:
python models/gemini_model.py
aynı zamanda modelin test verileri üzerinde performansını değerlendirir ve karışıklık matrisini (results/gemini_results.txt) kaydeder.

2.Hugging Face Niyet Sınıflandırma Modeli (Yerel Fine-tuning)

Model Tipi: DistilBERT tabanlı bir Transformer modeli üzerinde fine-tuning (ince ayar) yapılmıştır. DistilBERT, BERT'in daha hafif ve hızlı bir versiyonu olup, genel dil anlama yeteneklerini korurken çıkarım hızını artırır.

Seçim Nedeni: Hugging Face ekosistemindeki önceden eğitilmiş Transformer modelleri, doğal dil işlemedeki son gelişmeleri temsil eder ve karmaşık dil anlama görevlerinde yüksek doğruluk potansiyeli sunar. Türkçe gibi dillerde bile önceden eğitilmiş modellerin ince ayarlanması, sıfırdan model eğitmeye göre çok daha verimlidir.

Eğitim Süreci: Model, data/train_data.csv dosyasındaki eğitim verileri kullanılarak models/huggingface_model.py betiği çalıştırılarak fine-tune edilmiştir. Fine-tuning, transformers kütüphanesinin Trainer sınıfı aracılığıyla gerçekleştirilmiştir. Eğitimin sonunda, modelin ağırlıkları, konfigürasyonu ve tokenizer'ı (results/hf_trained_model/ dizini altına) kaydedilmiştir. Bu kaydedilen model bileşenleri, Streamlit uygulamasında niyet sınıflandırması için yüklenir.

Eğitim Komutu:
python models/huggingface_model.py
modelin test verileri üzerinde performansını değerlendirir ve sonuçları (results/hf_results.txt) kaydeder.

Eğitim Kayıtları (Hugging Face Modeli)
<img width="1440" alt="Ekran Resmi 2025-06-07 19 15 34" src="https://github.com/user-attachments/assets/49688941-6ed8-4a76-8a64-b9e148e22fe9" />

Yukarıdaki ekran görüntüsü, Hugging Face tabanlı niyet sınıflandırma modelimizin (distilbert-base-uncased üzerinde fine-tune edilmiş) eğitim sürecine ait konsol kayıtlarını göstermektedir. Bu kayıtlar, her bir eğitim adımında (logging step) modelin performansı ve eğitim dinamikleri hakkında bilgi sunmaktadır:

loss: Modelin tahmin hatalarını gösteren eğitim kaybı değerleri. Eğitim ilerledikçe bu değerin azalması beklenir, bu da modelin veriyi daha iyi öğrenmeye başladığını gösterir.

grad_norm: Gradyan normu, modelin ağırlık güncellemelerinin büyüklüğünü temsil eder. Aşırı büyük gradyan normları (exploding gradients) veya çok küçük gradyan normları (vanishing gradients) eğitimde sorunlara işaret edebilir. Buradaki değerlerin makul seviyelerde kalması eğitimin kararlılığını gösterir.

learning_rate: Modelin ağırlıklarının her adımda ne kadar güncellendiğini belirleyen öğrenme oranı. Eğitim süresince ayarlanan öğrenme oranı çizelgesine (scheduler) göre bu değerin değiştiği gözlemlenmektedir.

epoch: Modelin tüm eğitim veri setini kaç kez gördüğünü (geçtiğini) gösterir.

Bu kayıtlar, modelin başarılı bir şekilde eğitildiğini ve kayıp değerlerinin istikrarlı bir şekilde düştüğünü teyit etmektedir.

B. Yanıt Üretimi Modelleri (API Kullanımı)

Sohbet botunun kullanıcıya doğal dilde yanıt vermesi için, büyük ve genel amaçlı dil modellerinin (Large Language Models - LLM) API'leri kullanılmıştır. Bu LLM'ler, bizim kendi veri setimizle eğitilmiş niyet sınıflandırma modellerinden bağımsızdır ve geniş bir bilgi tabanına sahiptir.

1. Google Gemini 

Model Tipi: Google tarafından sunulan gemini-1.5-pro modeli, yanıt üretimi için kullanılmıştır. Bu model, Google'ın en yeni ve yetenekli genel amaçlı LLM'lerinden biridir.

Seçim Nedeni: Gemini 1.5 Pro, yüksek kaliteli ve bağlama uygun yanıtlar üretebilme yeteneği, geniş bilgi tabanı ve Google'ın sağladığı güçlü altyapı nedeniyle tercih edilmiştir.

API Anahtarı ve Entegrasyon: Gemini modeline erişim, Google Cloud Console üzerinden alınan bir API anahtarı ile sağlanmıştır. Bu anahtar, GOOGLE_API_KEY olarak .env dosyasında saklanır ve Streamlit uygulamasında langchain_google_genai kütüphanesi aracılığıyla kullanılır.

API Anahtarı Nasıl Alınır: Google Cloud Console'a (console.cloud.google.com) giriş yaparak yeni bir proje oluşturulur veya mevcut bir proje seçilir. Sol menüden "APIs & Services" → "Credentials" yolunu izlenerek "Create Credentials" butonuna tıklanır ve "API Key" seçeneğiyle yeni bir anahtar oluşturulur. Bu anahtar güvenli bir şekilde saklanmalı ve .env dosyası gibi çevresel değişkenler aracılığıyla uygulamaya dahil edilmelidir.

2. Hugging Face Inference API 

Model Tipi: Hugging Face'in sağladığı Inference API üzerinden erişilen HuggingFaceH4/zephyr-7b-beta modeli, yanıt üretimi için kullanılmıştır. Zephyr 7B Beta, sohbet uygulamaları için optimize edilmiş güçlü bir küçük dil modelidir.

Seçim Nedeni: Hugging Face ekosistemindeki zengin model seçenekleri ve Zephyr'ın sohbet odaklı performansı, bu modelin tercih edilmesinde etkili olmuştur.

API Anahtarı ve Entegrasyon: Hugging Face Inference API'ye erişim, bir Hugging Face API token'ı ile sağlanmıştır. Bu token, HUGGINGFACEHUB_API_TOKEN olarak .env dosyasında saklanır ve requests kütüphanesi aracılığıyla Hugging Face API uç noktasına HTTP POST isteği gönderilerek kullanılır.

API Anahtarı Nasıl Alınır: Hugging Face web sitesine (huggingface.co) giriş yapıldıktan sonra profil ayarlarına (Settings) gidilir. Sol menüde "Access Tokens" veya "API Tokens" bölümünden yeni bir token oluşturulur. Bu token da güvenli bir şekilde saklanmalı ve .env dosyası aracılığıyla uygulamaya entegre edilmelidir.

Streamlit Uygulamasında Model Kullanımı

streamlit_app.py dosyası, kullanıcının seçtiği modele göre hem niyet sınıflandırmasını hem de yanıt üretimini yönetir:

Niyet Tahmini: Kullanıcının girdisi alındığında, ilk olarak daha önce eğitilmiş ve kaydedilmiş olan yerel Gemini niyet sınıflandırma modeli (gemini_pipeline.pkl) veya yerel Hugging Face niyet sınıflandırma modeli (hf_trained_model/ klasöründeki bileşenler) yüklenerek, kullanıcının niyetini (intent) tahmin etmek için kullanılır.

Prompt Oluşturma: Tahmin edilen niyet (predicted_intent) ve kullanıcının orijinal sorusu (user_input), build_prompt fonksiyonu aracılığıyla, yanıt üretecek LLM için optimize edilmiş bir "prompt" (komut) oluşturmak üzere birleştirilir. Bu prompt, LLM'nin doğru bağlamda ve istenen formatta yanıt vermesini sağlar.

Yanıt Üretimi: Oluşturulan prompt, seçilen LLM API'sine (gemini-1.5-pro veya HuggingFaceH4/zephyr-7b-beta) gönderilir. API'den gelen yanıt, temizleme (clean_response) işleminden geçirilerek kullanıcıya sunulur.

Bu ayrım, projenin hem özelleşmiş bir niyet sınıflandırma yeteneğine sahip olmasını hem de güncel ve kapsamlı bilgilere sahip büyük dil modellerinden faydalanmasını sağlamaktadır.


Performans Karşılaştırması ve Karışıklık Matrisi

Her iki modelin (Gemini ve Hugging Face) performansını objektif bir şekilde değerlendirmek için test veri seti kullanılmış ve Precision, Recall, F1-Score gibi metriklerle birlikte Karışıklık Matrisi (Confusion Matrix) oluşturulmuştur.

Performans Karşılaştırması ve Karışıklık Matrisi

Her iki modelin (Gemini ve Hugging Face) performansını objektif bir şekilde değerlendirmek için test veri seti kullanılmış ve Precision, Recall, F1-Score gibi metriklerle birlikte Karışıklık Matrisi (Confusion Matrix) oluşturulmuştur.

Performans Metrikleri ve Karışıklık Matrisi Açıklaması:

Precision (Kesinlik): Modelin pozitif olarak tahmin ettiği durumların ne kadarının gerçekten pozitif olduğunu gösterir. (Doğru pozitifler / (Doğru pozitifler + Yanlış pozitifler))

Recall (Duyarlılık): Gerçek pozitif durumların ne kadarının model tarafından doğru bir şekilde yakalandığını gösterir. (Doğru pozitifler / (Doğru pozitifler + Yanlış negatifler))

F1-Score: Precision ve Recall'un harmonik ortalamasıdır ve modelin dengeli performansını yansıtır. Özellikle sınıf dengesizliklerinin olduğu durumlarda daha bilgilendirici bir metrik olabilir.

Karışıklık Matrisi: Bir sınıflandırma modelinin performansını görselleştiren bir tablodur. Satırlar gerçek sınıfları, sütunlar ise modelin tahmin ettiği sınıfları temsil eder. Köşegen üzerindeki değerler doğru tahminleri, köşegen dışındaki değerler ise yanlış sınıflandırmaları gösterir.

Hesaplama ve Görselleştirme Yöntemleri:

Performans metrikleri ve karışıklık matrislerinin hesaplanması için Python'daki popüler makine öğrenimi kütüphaneleri (örneğin scikit-learn) kullanılmıştır. Her iki modelin sonuçları, results klasörüne kaydedilmiştir. Karışıklık matrisinin görselleştirilmesi için matplotlib veya seaborn gibi kütüphanelerden faydalanılmıştır. MATLAB, özellikle istatistiksel analiz ve veri görselleştirme için güçlü bir araç olsa da, Python'daki bu kütüphaneler, makine öğrenimi projeleri için daha yaygın ve entegre çözümler sunmaktadır.



Sonuçlar:



           Gemini      Hugging Face

Precision  0.6475      0.6136

Recall     0.6398      0.6137

F1 Score   0.6353      0.5972


Bu tablo, modellerin kesinlik (Precision), duyarlılık (Recall) ve F1-skoru (F1-Score) değerlerini karşılaştırarak hangi modelin daha iyi performans gösterdiğini özetlemektedir.



Karışıklık Matrisi:

Hugging Face

<img width="641" alt="Ekran Resmi 2025-06-13 22 13 05" src="https://github.com/user-attachments/assets/3e267359-1b07-4f43-856e-100b77dda419" />


Gemini
<img width="1440" alt="gemini" src="https://github.com/user-attachments/assets/e593c810-e2fa-4e5a-bb64-c2e82fffa548" />


Sonuçlara göre, Gemini modeli Hugging Face modeline kıyasla biraz daha yüksek Precision, Recall ve F1-Score değerleri göstermiştir. Bu, Gemini modelinin, projenin mevcut veri seti ve görev tanımı bağlamında biraz daha iyi performans sergilediğini düşündürmektedir. Her iki model için de karışıklık matrisleri, hangi niyetlerin birbirine karıştırıldığını detaylı olarak göstermektedir, bu da gelecekteki geliştirmeler için yol göstericidir.



Chatbot Akış Diyagramı



Başlangıç

   │

   ▼

Model Seçimi (Gemini / Hugging Face)

   │

   ▼

Kullanıcı Girişi (Soru veya ifade girer)

   │

   ▼

Niyet Sınıflandırması (Örn: Malzeme_Turu, Sürdürülebilirlik_Tanimi)

   │

   ▼

Yanıt Oluşturma (Seçilen modele göre yanıt üretilir)

   │

   ▼

Yanıt Gösterme (Yanıt kullanıcıya sunulur, giriş silinmez)

   │

   ▼

Sohbet Devam Ediyor mu?

   ├──► **Evet** → Kullanıcı yeni bir soru girer → **Adım 3'e dön**

   └──► **Hayır** → Sohbet sona erer

   │

   ▼

Bitiş (Sohbet tamamlanır)



Proje Kurulum ve Çalıştırma Aşamaları

Proje, bağımlılıkların yönetimi ve kolay çalıştırılabilirlik için bir sanal ortam kullanılarak yapılandırılmıştır. Uygulamanın kullanıcı arayüzü Streamlit ile geliştirilmiştir.
Python 3.9 kullanılmıştır.


Başlangıç  

   │  

   ▼  

Proje Yapılandırma (Bağımlılık yönetimi ve sanal ortam kullanımı)  

   │  

   ▼  

Streamlit Kullanıcı Arayüzü Hazır  

   │  

   ▼  

Kurulum Adımları  

   │  

   ▼  

Sanal Ortam Oluşturma  

   │  

   ├──► **macOS/Linux:** `python3 -m venv .venv`  

   └──► **Windows:** `python -m venv .venv`  

   │  

   ▼  

Sanal Ortamı Aktifleştirme  

   │  

   ├──► **macOS/Linux:** `source .venv/bin/activate`  

   └──► **Windows:** `.venv\Scripts\activate`  

   │  

   ▼  

Gerekli Paketleri Yükleme (`requirements.txt` içindeki bağımlılıkları yükle)  

   │  

   ▼  

API Anahtarlarını Ayarlama  

   │  

   ├──► `.env` dosyası oluştur  

   ├──► **GOOGLE_API_KEY** ve **HUGGINGFACEHUB_API_TOKEN** değişkenlerini ekle  

   └──► Dosyayı proje ana dizinine yerleştir  

   │  

   ▼  

Uygulamayı Çalıştırma  

   │  

   ├──► `streamlit run app/streamlit_app.py` komutunu çalıştır  

   └──► **Tarayıcıda chatbot arayüzü açılır**  

   │  

   ▼  

Proje Çalıştırmaya Hazır!  


Geliştirilen sohbet botu uygulaması, kullanıcı dostu bir arayüz sunmak üzere tasarlanmıştır.



Ana Özellikler:

Model Seçimi: Uygulama açılışında, kullanıcıya Gemini ve Hugging Face modelleri arasında seçim yapma imkanı sunulur. Bu seçim, sohbet botunun hangi yapay zekâ modeli tarafından destekleneceğini belirler. Modeller arasındaki temel farklar; hız, kullanılan teknoloji (TF-IDF + Lojistik Regresyon vs. Transformer tabanlı fine-tuning) ve yanıt kalitesindeki nüanslardır.

Örnek Sorular: Kullanıcı arayüzünde, sohbeti başlatmaya yardımcı olmak ve kullanıcılara ilham vermek amacıyla çeşitli örnek sorular listelenmiştir. Bu örnek sorulara tıklanıldığında, soru otomatik olarak giriş alanına yerleşir ve ekstra "Gönder" tuşuna basmaya gerek kalmadan doğrudan bot'a iletilir. Bu, kullanıcı deneyimini kolaylaştırır.

Kullanıcı Girişi ve Yanıt Bekleme: Kullanıcı, kendi sorularını metin kutusuna yazabilir. Mesajlar, "Gönder" butonuna tıklanarak veya metin alanında Enter tuşuna basılarak (birden fazla satır yazabilmek için Shift+Enter kullanılabilir) gönderilir. Bot, seçili modele göre yanıt oluşturur ve sohbet geçmişinde gösterir.

Sohbet Geçmişini Temizleme: Sohbetin uzaması ve kafa karışıklığını önlemek amacıyla, kullanıcıya sohbet geçmişini tek bir tuşla temizleme imkanı sunan bir buton bulunmaktadır. Bu, yeni bir sohbet başlatmak için kullanışlı bir özelliktir.

Kullanıcı Dostu Tasarım: Uygulama, basit ve anlaşılır bir kullanıcı arayüzü ile tasarlanmıştır. Renkler ve düzen, rahat bir sohbet deneyimi sağlamayı hedefler.


Projede Geliştirilebilecek Yönler ve Eksiklikler

Her proje gibi, bu chatbot uygulamasının da geliştirilmeye açık yönleri ve bazı eksiklikleri bulunmaktadır:

Yanıt Hızı: Özellikle Hugging Face modelinin API kısıtlamaları ve model büyüklüğü nedeniyle yanıt süreleri, Gemini modeline kıyasla daha yavaş olabilmektedir. Bu durum, anlık geri bildirim bekleyen kullanıcılar için bir dezavantaj oluşturabilir. Gelecekte daha optimize edilmiş modeller veya daha yüksek API limitleri ile bu sorun giderilebilir.

Giriş Alanı Temizliği: Kullanıcı bir mesaj gönderdikten sonra, mesajın yazıldığı metin giriş alanı otomatik olarak temizlenmemektedir. Bu, kullanıcı deneyimini hafifçe olumsuz etkileyebilir. Kullanıcı mesajı gönderdikten sonra giriş alanının otomatik olarak sıfırlanması, akıcı bir sohbet deneyimi için önemli bir iyileştirme olacaktır.

Hugging Face Yanıt Kalitesi: Hugging Face API kısıtlamaları nedeniyle (deneme sürümünde API kredilerinin hızla tükenmesi gibi), model üzerinde istenildiği kadar derinlemesine fine-tuning veya test yapılamamıştır. Bu durum, Hugging Face modelinin yanıt kalitesinin Gemini kadar optimize edilememesine yol açmıştır. Tam sürüm API erişimi ile daha kapsamlı bir eğitim ve optimizasyon, performansını önemli ölçüde artırabilir.

Proje Yapısı
├── .env                  # API anahtarları gibi hassas bilgileri içeren ortam değişkenleri dosyası
├── app/                  # Streamlit uygulamasını içeren dizin
│   └── streamlit_app.py  # Ana Streamlit uygulama dosyası
├── data/                 # Veri setlerinin bulunduğu dizin
│   ├── chatbot_dataset.xlsx # Orijinal veri seti
│   ├── train_data.csv    # Eğitim için ayrılmış veri
│   └── test_data.csv     # Test için ayrılmış veri
├── models/               # Model eğitim ve fine-tuning kodlarının bulunduğu dizin
│   ├── gemini_model.py   # Gemini (TF-IDF + Lojistik Regresyon) modelinin eğitim kodu
│   └── huggingface_model.py # Hugging Face (DistilBERT) modelinin fine-tuning kodu
├── results/              # Model eğitim sonuçları, kaydedilmiş modeller ve görselleştirmeler
│   ├── gemini_trained_model/ # Eğitilmiş Gemini modeli objelerinin saklandığı dizin
│   │   └── gemini_pipeline.pkl # Kaydedilmiş Gemini model pipeline'ı
│   ├── hf_trained_model/     # Eğitilmiş Hugging Face modelinin ağırlık ve konfigürasyon dosyaları
│   │   ├── config.json
│   │   ├── pytorch_model.bin
│   │   └── tokenizer.json
│   ├── gemini_results.txt    # Gemini modelinin performans sonuçları (karışıklık matrisi vb.)
│   └── hf_results.txt        # Hugging Face modelinin performans sonuçları (karışıklık matrisi vb.)
├── utils/               
│   └── traintestayrimi.py # Veri setini train ve test olarak ayıran Python betiği
├── .gitignore            # Git versiyon kontrol sistemi için ignore edilecek dosyalar
├── README.md             # Proje hakkında genel bilgi, kurulum ve çalıştırma talimatları (bu belge)
└── requirements.txt      # Projenin tüm bağımlılıklarını içeren dosya


Proje için ekran görüntüleri aşağıda verilmiştir.

<img width="1440" alt="Ekran Resmi 2025-06-12 22 20 26" src="https://github.com/user-attachments/assets/640bb3dd-b9b7-4850-a0b8-26835578f880" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 05 00" src="https://github.com/user-attachments/assets/70f9f55d-99e3-4569-8374-eb087106b59a" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 09 57" src="https://github.com/user-attachments/assets/e03905a6-15b2-4706-b9c8-dfce6fd44ade" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 02 02" src="https://github.com/user-attachments/assets/d282a982-bbbc-4eaa-97f2-f0f21abcf1c1" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 18 29" src="https://github.com/user-attachments/assets/034e08c2-d116-49d6-a2d4-ccd4f8d96ba2" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 11 26" src="https://github.com/user-attachments/assets/698ac3e8-ba20-4ba1-abc8-659296d926f8" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 10 47" src="https://github.com/user-attachments/assets/90440b32-e147-4b0e-b16f-4956316165a3" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 15 25" src="https://github.com/user-attachments/assets/962c7bab-ab32-45cb-ad2e-209a883c1a2e" />


<img width="1440" alt="Ekran Resmi 2025-06-13 20 17 27" src="https://github.com/user-attachments/assets/fc1da86f-20b8-44e8-a0f9-80bde31a9413" />


Herhangi hata durumunda ise aşağıdaki mesaj gönderiliyor

<img width="1331" alt="Ekran Resmi 2025-06-13 22 22 08" src="https://github.com/user-attachments/assets/23fc3fab-0caf-410c-9ef1-076c6c124e35" />



