import os

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_nilai_akhir(uts, uas, tugas):
    """Menghitung nilai akhir berdasarkan bobot yang ditentukan."""
    return (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)

def tentukan_grade(nilai_akhir):
    """Menentukan grade berdasarkan nilai akhir."""
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def input_nilai(prompt):
    """Helper function untuk validasi input nilai (0-100)."""
    while True:
        try:
            nilai = float(input(prompt))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Error: Nilai harus berada di antara 0 dan 100.")
        except ValueError:
            print("Error: Input harus berupa angka.")

def tampilkan_data(data_list):
    """Menampilkan seluruh data mahasiswa dalam format tabel."""
    if not data_list:
        print("Belum ada data mahasiswa.")
        return

    print("--- Data Nilai Mahasiswa ---")
    # Header Tabel
    print("=" * 88)
    print(f"| {'NIM':<10} | {'Nama':<20} | {'UTS':>5} | {'UAS':>5} | {'Tugas':>7} | {'Akhir':>7} | {'Grade':>7} |")
    print("=" * 88)
    
    # Isi Tabel
    for mhs in data_list:
        print(f"| {mhs['NIM']:<10} | {mhs['nama']:<20} | {mhs['nilai_uts']:>5.1f} | {mhs['nilai_uas']:>5.1f} | {mhs['nilai_tugas']:>7.1f} | {mhs['nilai_akhir']:>7.2f} | {mhs['grade']:>7} |")
    
    print("-" * 88)

def tambah_mahasiswa_baru(data_list):
    """Menambahkan data mahasiswa baru melalui input user."""
    print("--- Tambah Data Mahasiswa Baru ---")
    nama = input("Nama Mahasiswa: ")
    nim = input("NIM: ")
    
    # Validasi input nilai
    uts = input_nilai("Nilai UTS: ")
    uas = input_nilai("Nilai UAS: ")
    tugas = input_nilai("Nilai Tugas: ")
    
    # Hitung nilai akhir dan grade
    nilai_akhir = hitung_nilai_akhir(uts, uas, tugas)
    grade = tentukan_grade(nilai_akhir)
    
    # Buat dictionary baru dan tambahkan ke list
    mahasiswa_baru = {
        'nama': nama,
        'NIM': nim,
        'nilai_uts': uts,
        'nilai_uas': uas,
        'nilai_tugas': tugas,
        'nilai_akhir': nilai_akhir,
        'grade': grade
    }
    
    data_list.append(mahasiswa_baru)
    print(f"\nData untuk {nama} ({nim}) berhasil ditambahkan!")

def cari_nilai_ekstrim(data_list):
    """Mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah."""
    if not data_list:
        print("Belum ada data mahasiswa.")
        return

    # Mencari nilai tertinggi
    tertinggi = max(data_list, key=lambda x: x['nilai_akhir'])
    # Mencari nilai terendah
    terendah = min(data_list, key=lambda x: x['nilai_akhir'])
    
    print("--- Nilai Ekstrim Mahasiswa ---")
    print(f"Nilai Tertinggi:")
    print(f"  Nama  : {tertinggi['nama']} ({tertinggi['NIM']})")
    print(f"  Nilai : {tertinggi['nilai_akhir']:.2f} (Grade: {tertinggi['grade']})")
    
    print(f"\nNilai Terendah:")
    print(f"  Nama  : {terendah['nama']} ({terendah['NIM']})")
    print(f"  Nilai : {terendah['nilai_akhir']:.2f} (Grade: {terendah['grade']})")

def filter_by_grade(data_list):
    """Menampilkan mahasiswa berdasarkan grade yang diinput."""
    if not data_list:
        print("Belum ada data mahasiswa.")
        return

    grade_input = input("Masukkan Grade yang ingin dicari (A/B/C/D/E): ").upper()
    
    # Filter list berdasarkan grade
    filtered_list = [mhs for mhs in data_list if mhs['grade'] == grade_input]
    
    if not filtered_list:
        print(f"Tidak ditemukan mahasiswa dengan grade '{grade_input}'.")
    else:
        print(f"\n--- Mahasiswa dengan Grade '{grade_input}' ---")
        tampilkan_data(filtered_list)

def hitung_rata_rata_kelas(data_list):
    """Menghitung dan menampilkan rata-rata nilai akhir seluruh kelas."""
    if not data_list:
        print("Belum ada data mahasiswa.")
        return

    total_nilai = sum(mhs['nilai_akhir'] for mhs in data_list)
    rata_rata = total_nilai / len(data_list)
    
    print(f"--- Rata-rata Nilai Kelas ---")
    print(f"Total Mahasiswa : {len(data_list)}")
    print(f"Rata-rata Nilai : {rata_rata:.2f}")

def tampilkan_menu():
    """Menampilkan menu utama program."""
    print("\n========= Program Pengelolaan Data Nilai ==========")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Tambah Data Mahasiswa Baru")
    print("3. Cari Nilai Tertinggi & Terendah")
    print("4. Filter Mahasiswa Berdasarkan Grade")
    print("5. Hitung Rata-rata Nilai Kelas")
    print("6. Keluar Program")
    print("===================================================")
    return input("Pilih menu (1-6): ")

def main():
    """Fungsi utama untuk menjalankan program."""
    
    # Data awal mahasiswa
    data_mahasiswa = [
        {'nama': 'Budi Santoso', 'NIM': '211001', 'nilai_uts': 80, 'nilai_uas': 75, 'nilai_tugas': 85},
        {'nama': 'Ani Lestari', 'NIM': '211002', 'nilai_uts': 90, 'nilai_uas': 95, 'nilai_tugas': 92},
        {'nama': 'Candra Wijaya', 'NIM': '211003', 'nilai_uts': 60, 'nilai_uas': 50, 'nilai_tugas': 65},
        {'nama': 'Dewi Sartika', 'NIM': '211004', 'nilai_uts': 75, 'nilai_uas': 80, 'nilai_tugas': 70},
        {'nama': 'Eka Prasetya', 'NIM': '211005', 'nilai_uts': 40, 'nilai_uas': 45, 'nilai_tugas': 50}
    ]
    
    # Proses data awal untuk menambahkan 'nilai_akhir' dan 'grade'
    for mhs in data_mahasiswa:
        mhs['nilai_akhir'] = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        mhs['grade'] = tentukan_grade(mhs['nilai_akhir'])

    # Loop menu utama
    while True:
        pilihan = tampilkan_menu()
        clear_screen()
        
        if pilihan == '1':
            tampilkan_data(data_mahasiswa)
        elif pilihan == '2':
            tambah_mahasiswa_baru(data_mahasiswa)
        elif pilihan == '3':
            cari_nilai_ekstrim(data_mahasiswa)
        elif pilihan == '4':
            filter_by_grade(data_mahasiswa)
        elif pilihan == '5':
            hitung_rata_rata_kelas(data_mahasiswa)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-6.")
        
        input("\nTekan Enter untuk kembali ke menu...")
        clear_screen()

# Menjalankan program utama
if __name__ == "__main__":
    main()