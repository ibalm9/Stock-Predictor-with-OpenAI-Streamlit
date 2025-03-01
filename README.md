# AI Stock Predictor

Aplikasi prediksi saham berbasis AI menggunakan Streamlit dan OpenAI API.

## Fitur
- Visualisasi data saham dengan grafik candlestick
- Analisis prediksi menggunakan AI (OpenAI GPT-3.5)
- Antarmuka web yang interaktif dengan Streamlit

## Persyaratan Sistem
- Python 3.11 atau yang lebih baru
- pip (Python package manager)

## Instalasi

1. Clone repository ini ke komputer lokal Anda

2. Buat virtual environment Python
```bash
python -m venv venv
```

3. Aktifkan virtual environment
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies yang diperlukan
```bash
pip install streamlit openai pandas yfinance plotly
```

5. Buat file `.env` dan tambahkan OpenAI API key Anda
```
OPENAI_API_KEY=your_api_key_here
```

## Cara Menjalankan Aplikasi

1. Pastikan virtual environment sudah aktif

2. Jalankan aplikasi dengan perintah:
```bash
streamlit run main.py
```

3. Buka browser dan akses `http://localhost:8501`

## Penggunaan
1. Masukkan simbol saham (contoh: AAPL untuk Apple Inc.)
2. Klik tombol "Analyze Stock"
3. Tunggu hingga analisis selesai
4. Lihat hasil prediksi dan analisis AI

## Struktur Proyek
```
.
├── main.py              # File utama aplikasi
├── stock_analyzer.py    # Modul analisis menggunakan OpenAI
├── utils.py            # Fungsi-fungsi utilitas
└── style.css           # Stylesheet kustom
```

## Catatan Penting
- Aplikasi ini menggunakan OpenAI API yang memerlukan API key valid
- Prediksi yang dihasilkan hanya untuk tujuan pembelajaran, bukan rekomendasi investasi
- Pastikan Anda memiliki koneksi internet yang stabil untuk mengakses data saham dan API OpenAI

## Troubleshooting

### API Key Error
Jika Anda mendapatkan error terkait API key:
1. Pastikan file `.env` sudah dibuat
2. Periksa API key yang dimasukkan sudah benar
3. Restart aplikasi setelah mengubah API key

### Data Tidak Muncul
Jika data saham tidak muncul:
1. Periksa koneksi internet Anda
2. Pastikan simbol saham yang dimasukkan valid
3. Coba refresh halaman

## Disclaimer
Aplikasi ini dibuat untuk tujuan pembelajaran dan demonstrasi. Jangan gunakan prediksi yang dihasilkan sebagai satu-satunya dasar untuk keputusan investasi Anda.
