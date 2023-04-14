# Tugas Kecil 3: Implementasi Program Tanda-tangan Digital dengan Menggunakan Algoritma RSA dan Fungsi hash SHA-3
## II4031 Kriptografi dan Koding
- 18220012 Fikri Muhammad Fahreza
- 18220086 Aldi Fadlian Sunan

# 🔍 Introduction 
- Tanda-tangan digital dapat digunakan untuk otentikasi data digital, seperti pesan yang dikirim melalui saluran komunikasi dan dokumen elektronis yang disimpan dalam komputer.
- Pada program ini ini, berupa aplikasi yang mengimplementasikan algoritma RSA + SHA-3 (Keccak) untuk memberi tanda-tangan digital pada dokumen (file) elektronis.
- Dalam hal ini, anda sebagai pemilik dokumen mempunyai sepasang kunci, yaitu kunci publik dan kunci privat.
Untuk aplikasi desktop, tanda tangan dapat disimpan di dalam dokumen terpisah atau digabung di dalam file yang ditandatangani (tanda tangan digitak diletakkan pada akhir dokumen).
- Pengguna dapat memilih apakah tanda-tangan disimpan di dalam dokumen terpisah (separate) atau disatukan di dalam file pesan.
- Tanda tangan digital bergantung pada isi file dan kunci.
- Tanda-tangan digital direpresentasikan sebagai karakter-karakter heksadesimal. Untuk membedakan tandatangan digital dengan isi dokumen, maka tanda-tangan digital diawali dan diakhiri dengan
*** Begin of digital signature **** dan *** End of digital signature ****
- Karena algoritma RSA menggunakan parameter bilangan bulat yang panjang (besar), maka program anda harus mampu menggunakan bilangan yang besar.

# 👨‍💻Specifications
1. Program berupa aplikasi desktop yang terdiri dari menu:
a) Menu pembangkitan kunci publik dan kunci privat RSA.
b) Menu pembangkitan tanda-tangan digital (signing)
c) Menu verifikasi tanda-tangan digital (verifying)
2. Program RSA dibuat sendiri, tidak menggunakan libary bahasa pemrograman. Panjang kunci sebaiknya di atas 512 bit (gunakan pustaka big number)
3. File dokumen yang ditanda-tangani default-nya adalah file teks, tanda-tangan digital disisipkan pada akhir dokumen.
Untuk file non teks seperti .jpg, .pdf, video, maupun audio, tanda-tangan digital disimpan di dalam file terpisah.
4. Bahasa pemrograman yang digunakan adalah Python

# 💻How to Run This Program?
1. Clone repositori ini
2. Run file app.py
3. Buat kunci terlebih dahulu melalui menu generate key
4. Signing signature ke dokumen melalui menu sign dengan kunci yang telah dibuat sebelumnya
5. Verifying signature dari dokumen yang telah ditandatangani melalui menu Verify
