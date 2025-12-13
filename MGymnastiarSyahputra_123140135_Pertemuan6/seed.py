from sqlalchemy import create_engine
from app.models import Base, Matakuliah, configure_session, get_db_session

# ⚠️ GANTI sesuai dengan yang kamu pakai di development.ini / alembic.ini
DB_URL = "postgresql+psycopg2://postgres:stev123@localhost:5432/matakuliah_db"


def main():
    # Buat engine Postgre
    engine = create_engine(DB_URL)

    # Pastikan tabel ada (harusnya sudah dibuat Alembic, tapi ini aman kalau belum)
    Base.metadata.create_all(engine)

    # Konfigurasi session dengan engine
    configure_session(engine)
    session = get_db_session()

    # (Opsional) kosongkan dulu tabel matakuliah
    session.query(Matakuliah).delete()

    # Tambah 3 data awal
    mk1 = Matakuliah(kode_mk="IF101", nama_mk="Pengantar Informatika", sks=3, semester=1)
    mk2 = Matakuliah(kode_mk="IF202", nama_mk="Struktur Data", sks=3, semester=3)
    mk3 = Matakuliah(kode_mk="IF303", nama_mk="Pengembangan Aplikasi Web", sks=3, semester=5)

    session.add_all([mk1, mk2, mk3])
    session.commit()

    print("Data awal berhasil ditambahkan ke PostgreSQL!")


if __name__ == "__main__":
    main()
