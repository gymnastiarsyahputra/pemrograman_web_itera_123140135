from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

Base = declarative_base()

# global engine & session factory
SessionLocal = scoped_session(sessionmaker())
_engine = None


def init_engine(engine):
    """
    Simpan engine global (dipanggil di __init__.py).
    """
    global _engine
    _engine = engine


def configure_session(engine):
    """
    Konfigurasi SessionLocal dengan engine.
    """
    SessionLocal.configure(bind=engine)


def get_db_session():
    """
    Dapatkan session database.
    """
    return SessionLocal()


class Matakuliah(Base):
    __tablename__ = 'matakuliah'

    id = Column(Integer, primary_key=True)
    kode_mk = Column(Text, unique=True, nullable=False)
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester,
        }
