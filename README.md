Sistem Absensi Siswa Berbasis Face Recognition dengan Notifikasi WhatsApp

Project ini merupakan sistem absensi otomatis berbasis pengenalan wajah (face recognition) yang digunakan untuk mencatat kehadiran siswa secara real-time. Sistem akan mendeteksi wajah melalui kamera, mencocokkannya dengan database, kemudian secara otomatis mengirimkan notifikasi ke WhatsApp orang tua siswa sebagai laporan kehadiran.

Tujuan Project:
1.Mengotomatisasi proses absensi siswa
2.Mengurangi kecurangan dalam absensi manual
3.Memberikan notifikasi real-time kepada orang tua
4.Mempercepat proses rekap kehadiran

Fitur Utama:
1.Deteksi wajah menggunakan kamera
2.Pengenalan wajah (face recognition)
3.Pencatatan absensi otomatis (check-in)
4.Penyimpanan data kehadiran
5.Notifikasi WhatsApp ke orang tua
6.Sistem berjalan real-time

Arsitektur Sistem:
1.Kamera menangkap wajah siswa
2.Sistem melakukan deteksi & identifikasi wajah
3.Jika cocok → data absensi dicatat
4.Sistem memanggil script WhatsApp sender
5.WhatsApp Web mengirim pesan ke orang tua

Struktur Project
project-absensi-face-recognition/
│
├── attendance.py        # Script utama deteksi wajah & absensi
├── send_wa.py           # Script pengiriman WhatsApp
├── dataset/             # Dataset wajah siswa
├── encodings/           # Data hasil encoding wajah
├── attendance_log.csv   # Hasil pencatatan absensi
├── requirements.txt     # Library yang digunakan
└── README.md            # Dokumentasi project

Teknologi yang Digunakan
1.Python
2.OpenCV
3.Face Recognition / YOLO (sesuai implementasi kamu)
4.NumPy
5.Pandas
6.PyWhatKit (WhatsApp automation)
7.WhatsApp Web

Cara Menjalankan Project
1. Install dependency
pip install -r requirements.txt
2. Jalankan sistem absensi
python attendance.py
3. Sistem WhatsApp akan otomatis berjalan
python send_wa.py

Cara Kerja Notifikasi WhatsApp
1.Sistem mendeteksi siswa hadir
2.Mengambil data nomor orang tua dari database
3.Mengirim pesan otomatis melalui WhatsApp Web

Pesan berisi:
Nama siswa
Waktu kehadiran
Status hadir

Catatan Penting
1.WhatsApp Web harus login terlebih dahulu
2.Koneksi internet harus stabil
3.Kamera harus dalam kondisi baik
4.Delay pengiriman WA perlu dioptimalkan jika jumlah siswa banyak

Masalah yang Dihadapi
1.Delay saat membuka WhatsApp Web terlalu lama
2.Antrian pengiriman jika jumlah siswa banyak
3.Akurasi face recognition tergantung pencahayaan

Rencana Pengembangan
1.Migrasi dari WhatsApp Web ke WhatsApp API resmi
2.Optimasi real-time recognition (multi-threading)
3.Dashboard admin berbasis web
4.Cloud database (MySQL/Firebase)
5.Sistem anti-duplikasi absensi

Author
Nama: Aep Supriadi
Project: Sistem Absensi Face Recognition + WhatsApp Notification
Teknologi: Python, OpenCV, Automation
