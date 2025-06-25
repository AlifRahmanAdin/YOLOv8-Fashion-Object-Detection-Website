# 👗 YOLOv8 Fashion Detector Web App

## 📌 Project Description

Proyek ini bertujuan untuk membangun aplikasi web yang mampu mendeteksi objek fashion pada gambar streetstyle menggunakan model deep learning YOLOv8. Model dilatih dengan **Colorful Fashion Dataset** dari Kaggle, yang mencakup **10 kelas** objek fashion: `sunglass`, `hat`, `jacket`, `shirt`, `pants`, `shorts`, `skirt`, `dress`, `bag`, dan `shoe`.

Pelatihan dilakukan selama **20 epoch** dengan batch size tetap, menghasilkan performa yang baik dengan skor **mAP@0.5 sebesar 0.799**. Aplikasi web dikembangkan menggunakan framework **Flask** untuk backend, yang memungkinkan pengguna mengunggah gambar, memprosesnya melalui model, dan menampilkan hasil deteksi lengkap dengan **bounding box dan label klasifikasi**.

---

## 🚀 Cara Menjalankan

Pastikan Python sudah terinstal. Jalankan perintah berikut di terminal:

```bash
python app.py
