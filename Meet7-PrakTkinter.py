# Mengimpor library Tkinter untuk membuat GUI.
# Messagebox digunakan untuk menampilkan pesan kesalahan.
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries: #Mengambil nilai dari tiap input/entry yang sudah diisi.
            nilai = int(entry.get())
            if not (0 <= nilai <= 100): #Memastikan semua nilai dgn tipe data integer antara 0-100.
                raise ValueError("Nilai harus antara 0 dan 100.")#Jika ada nilai yg di luar natas ini, fungsi akan memunculkan ValueError.

        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")#Jika semua nilai benar, label hasil_label akan diupdate untuk menampilkan "Prediksi Prodi : Teknologi Informasi."
    except ValueError as ve: #Jika ada error(misalnya input bukan angka/diluar batas), pesan kesalahan akan muncul.
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat inisialisasi Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") #Memberi judul dalam aplikasi.
root.geometry("500x600") #Menentukan ukuran frame aplikasi
root.configure(bg="#800000")  # Mengubah background menjadi warna maroon

# Label Judul
# Membuat label judul di bagian atas dgn teks "Aplikasi Prediksi Prodi Pilihan" dan menggunakan font "Bookman Old Style", warna background diubah ke warna maroon.
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Bookman Old Style", 18, "bold"), bg="#800000")
judul_label.pack(pady=20) #Pack digunakan untuk menempatkan elemen(judul_label) secara vertikal/horizontal.Pady=20 adalah jarak vertikal dgn elemen lain diatas/bawahnya.

# Frame sebagai wadah untuk semua input nilai mata pelajaran.
frame_input = tk.Frame(root, bg="#800000")  # Mengubah background menjadi warna maroon
frame_input.pack(pady=10) #Menempatkan frame_input dgn memberikan jarak sebesar 10piksel  dgn elemen lain diatas/bawahnya.

# List untuk menyimpan entry nilai
entries = []
for i in range(10): #Membuat label dan entry/kolom input untuk 10 mata pelajaran. Semua kolom input disimpan dalam list entries untuk digunakan di fungsi hasil_prediksi.
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Bookman Old Style", 12), bg="#800000")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    #fungsi grid untuk menempatkan elemen berdasarkan baris dan kolom.
    #row=i menempatkan label pada baris ke-i sesuai nomor iterasi dalam loop.
    #column=0 menempatkan label di kolom pertama.
    #padx=10 dan pady=5 memberi jarak horizontal 10piksel dan vertikal 5piksel.
    
    entry = tk.Entry(frame_input, width=10, font=("Bookman Old Style", 12))#Membuat kolom input teks dalam frame_input dgn lebar kolom 10karakter dan font Bookman Old Style.
    entry.grid(row=i, column=1, padx=10, pady=5)#Menempatkan kolom input dlm frame_input dgn grid.Menempatkan kolom input di baris i dan kolom ke-1.
    #memberikan jarang horizontal dan vertikal masing" 10 dan 5 piksel.
    entries.append(entry)#menambahkan kolom input entry ke list entries.

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Bookman Old Style", 12, "bold"))
prediksi_button.pack(pady=30)
#Memanggil fungsi hasil_prediksi untuk memvalidasi dan menampilkan hasil prediksi.

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Bookman Old Style", 14, "italic"), fg="blue", bg="#800000")
hasil_label.pack(pady=20)
#Label digunakan untuk menampilkan teks hasil prediksi (misalnya "Prediksi Prodi : Teknologi Informasi") setelah semua nilai divalidasi.
#Awalnya, teks pada label ini kosong (Teks="")

# Menjalankan aplikasi
root.mainloop()
