# EcoSync Agent

EcoSync adalah aplikasi Agent AI simpel berbasis **Python (Flask, LangChain, dan LangGraph)** yang menggunakan model **Google Gemini**. Agen ini disimulasikan untuk mengelola tugas dampak sosial/lingkungan seperti mengecek volume sampah di area tertentu maupun menghitung estimasi pengurangan karbon.

## ⚙️ Persiapan & Instalasi

Ikuti langkah-langkah di bawah ini untuk menjalankan EcoSync Agent di perangkat Anda:

### 1. Prasyarat
Pastikan Python telah terinstal di komputer Anda. Disarankan menggunakan **Python 3.10** ke atas.

### 2. Membangun *Virtual Environment* (Opsional namun disarankan)
Sangat direkomendasikan membuat *virtual environment* (`.venv`) agar dependensi tidak bentrok dengan proyek Python lainnya:
```bash
python -m venv .venv

# Untuk Windows:
.\.venv\Scripts\activate

# Untuk Mac/Linux:
source .venv/bin/activate
```

### 3. Mengunduh Dependencies
Instal semua modul yang diperlukan menggunakan file `requirements.txt` yang sudah disediakan:
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key (Environment Variables)
Anda perlu memiliki API Key dari [Google AI Studio](https://aistudio.google.com/).
1. Di dalam folder `EcoSync-Agent`, buat sebuah file baru bernama `.env`.
2. Buka file `.env` dan masukkan API Key Anda dengan format seperti berikut:
```env
GEMINI_API_KEY=KODE_API_KEY_ANDA_DISINI
```
*(Ingat: File `.env` ini akan diabaikan oleh Git, sehingga kunci rahasia Anda tetap aman.)*

## 🚀 Menjalankan Aplikasi

Setelah semua instalasi dan konfigurasi selesai, jalankan server Flask menggunakan file `app.py`:
```bash
python app.py
```

Bila server berhasil berjalan, buka *browser* Anda dan arahkan ke alamat lokal berikut:
```
http://127.0.0.1:5000/
```

## 📝 Format Percakapan yang Dapat Dicoba

Coba gunakan percakapan di kolom chat *website* untuk berdiskusi layaknya berikut:
* "Tolong cek status tumpukan sampah di area Pasar Minggu saat ini. Apakah kondisinya kritis?"
* "Jika kita meminta masyarakat untuk melakukan daur ulang plastik sebanyak 100kg, berapa kompensasi pengurangan karbonnya?"

Selamat Mencoba!
