from abc import ABC, abstractmethod

# ------------------------------------------------------------------
# BAGIAN 1: DEFINISI CLASS (Sama seperti sebelumnya)
# ------------------------------------------------------------------

# 1. ABSTRACT CLASS dan ENCAPSULATION
class LibraryItem(ABC):
    """
    Sebuah abstract base class yang mewakili item di perpustakaan.
    Menggunakan __ (double underscore) untuk enkapsulasi private.
    """
    def __init__(self, id, title):
        self.__id = id      # Atribut private (Encapsulation)
        self.__title = title  # Atribut private (Encapsulation)

    # 6. PROPERTY DECORATOR (untuk 'id', read-only)
    @property
    def id(self):
        """Property untuk mengakses __id (read-only)."""
        return self.__id

    # 6. PROPERTY DECORATOR (untuk 'title', read-write)
    @property
    def title(self):
        """Property untuk mengakses __title."""
        return self.__title

    @title.setter
    def title(self, value):
        """Property setter untuk mengubah __title."""
        if value:
            self.__title = value
        else:
            print("Judul tidak boleh kosong.")

    # 3. ABSTRACT METHOD
    @abstractmethod
    def display_details(self):
        """
        Metode abstract yang harus diimplementasikan oleh subclass
        untuk menampilkan detail spesifik item.
        """
        pass

# 2. INHERITANCE (Pewarisan)
class Book(LibraryItem):
    """Subclass untuk item 'Buku', mewarisi dari LibraryItem."""
    def __init__(self, id, title, author):
        super().__init__(id, title)
        self.__author = author  # Atribut private khusus Book

    # 3. Implementasi Abstract Method (POLYMORPHISM)
    def display_details(self):
        print(f"[BUKU]   ID: {self.id}, Judul: '{self.title}', Penulis: {self.__author}")

# 2. INHERITANCE (Pewarisan)
class Magazine(LibraryItem):
    """Subclass untuk item 'Majalah', mewarisi dari LibraryItem."""
    def __init__(self, id, title, issue):
        super().__init__(id, title)
        self.__issue = issue  # Atribut private khusus Magazine

    # 3. Implementasi Abstract Method (POLYMORPHISM)
    def display_details(self):
        print(f"[MAJALAH] ID: {self.id}, Judul: '{self.title}', Edisi: {self.__issue}")

# 4. CLASS PENGELOLA (Library)
class Library:
    """Class untuk mengelola koleksi LibraryItem."""
    def __init__(self):
        # 5. ENCAPSULATION: List item dibuat private
        self.__items = []

    def add_item(self, item):
        """Menambahkan LibraryItem ke dalam koleksi perpustakaan."""
        if isinstance(item, LibraryItem):
            # Cek duplikat ID
            for existing_item in self.__items:
                if existing_item.id == item.id:
                    print(f"-> Gagal: Item dengan ID '{item.id}' sudah ada.")
                    return
            
            self.__items.append(item)
            print(f"-> Berhasil menambahkan: '{item.title}'")
        else:
            print(f"-> Gagal: Objek yang ditambahkan bukan turunan dari LibraryItem.")

    def display_available_items(self):
        """Menampilkan semua item yang ada di perpustakaan."""
        print("\n--- Daftar Item di Perpustakaan ---")
        if not self.__items:
            print("Perpustakaan masih kosong.")
            return
        
        # 4. POLYMORPHISM
        for item in self.__items:
            item.display_details()
        print("-------------------------------------")

    def search_item(self, query):
        """Mencari item berdasarkan ID atau Judul (case-insensitive)."""
        print(f"\n--- Hasil Pencarian untuk '{query}' ---")
        found_items = []
        
        for item in self.__items:
            if query.lower() in item.title.lower() or query.lower() == item.id.lower():
                found_items.append(item)
        
        if not found_items:
            print("Item tidak ditemukan.")
        else:
            for item in found_items:
                item.display_details()
        print("-------------------------------------")

# ------------------------------------------------------------------
# BAGIAN 2: MENU INTERAKTIF (Modifikasi)
# ------------------------------------------------------------------

if __name__ == "__main__":
    
    # Buat instance perpustakaan
    my_library = Library()
    
    # Tambahkan beberapa data awal agar tidak kosong
    print("--- Inisialisasi Data Awal ---")
    my_library.add_item(Book("B001", "Laskar Pelangi", "Andrea Hirata"))
    my_library.add_item(Magazine("M001", "National Geographic", "Oktober 2025"))
    print("------------------------------\n")

    # Loop menu utama
    while True:
        print("\n===== Sistem Manajemen Perpustakaan =====")
        print("1. Tambah Item Baru")
        print("2. Tampilkan Semua Item")
        print("3. Cari Item (berdasarkan ID atau Judul)")
        print("0. Keluar")
        print("=========================================")
        
        pilihan = input("Masukkan pilihan Anda (0-3): ")

        if pilihan == '1':
            # Opsi 1: Tambah Item
            print("\n--- Tambah Item Baru ---")
            tipe_item = input("Pilih Tipe Item (1: Buku, 2: Majalah, lainnya untuk batal): ")
            
            if tipe_item == '1':
                # Tambah Buku
                id = input("Masukkan ID Buku (e.g., B002): ")
                title = input("Masukkan Judul Buku: ")
                author = input("Masukkan Penulis: ")
                if not id or not title or not author:
                    print("-> Gagal: ID, Judul, dan Penulis tidak boleh kosong.")
                else:
                    new_item = Book(id, title, author)
                    my_library.add_item(new_item)
                    
            elif tipe_item == '2':
                # Tambah Majalah
                id = input("Masukkan ID Majalah (e.g., M002): ")
                title = input("Masukkan Judul Majalah: ")
                issue = input("Masukkan Edisi: ")
                if not id or not title or not issue:
                    print("-> Gagal: ID, Judul, dan Edisi tidak boleh kosong.")
                else:
                    new_item = Magazine(id, title, issue)
                    my_library.add_item(new_item)
            else:
                print("-> Penambahan item dibatalkan.")

        elif pilihan == '2':
            # Opsi 2: Tampilkan Semua Item
            # Ini sesuai permintaan Anda: "nampilin item"
            my_library.display_available_items()

        elif pilihan == '3':
            # Opsi 3: Cari Item
            query = input("\nMasukkan ID atau Judul yang ingin dicari: ")
            if not query:
                print("Query pencarian tidak boleh kosong.")
            else:
                my_library.search_item(query)

        elif pilihan == '0':
            # Opsi 0: Keluar
            print("\nTerima kasih telah menggunakan sistem. Sampai jumpa!")
            break # Keluar dari loop while True

        else:
            # Pilihan tidak valid
            print("\nPilihan tidak valid. Silakan coba lagi.")