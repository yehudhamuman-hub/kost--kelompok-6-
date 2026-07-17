from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.models import Base, KamarDB, KontrakDB

engine = create_engine("sqlite:///kost.db")


def init_db():
    Base.metadata.create_all(engine)


def simpan_kamar(nomor, tipe, harga):
    with Session(engine) as session:
        # Cek apakah nomor kamar sudah ada
        kamar = session.query(KamarDB).filter_by(nomor=nomor).first()

        if kamar:
            return kamar

        kamar = KamarDB(
            nomor=nomor,
            tipe=tipe,
            harga=harga,
            terisi=False
        )

        session.add(kamar)
        session.commit()
        session.refresh(kamar)

        return kamar


def ambil_semua_kamar():
    with Session(engine) as session:
        return session.query(KamarDB).all()


def update_status_kamar(nomor, terisi):
    with Session(engine) as session:
        kamar = (
            session.query(KamarDB)
            .filter_by(nomor=nomor)
            .first()
        )

        if kamar:
            kamar.terisi = terisi
            session.commit()


def simpan_kontrak(kamar_id, nama, ktp, hp, tgl_masuk):
    with Session(engine) as session:

        kontrak = KontrakDB(
            kamar_id=kamar_id,
            nama_penghuni=nama,
            no_ktp=ktp,
            no_hp=hp,
            tanggal_masuk=tgl_masuk,
            status_lunas=False
        )

        session.add(kontrak)
        session.commit()
        session.refresh(kontrak)

        return kontrak


def update_status_lunas(kontrak_id):
    with Session(engine) as session:

        kontrak = (
            session.query(KontrakDB)
            .filter_by(id=kontrak_id)
            .first()
        )

        if kontrak:
            kontrak.status_lunas = True
            session.commit()


def ambil_kontrak_aktif():
    with Session(engine) as session:
        return (
            session.query(KontrakDB)
            .filter_by(status_lunas=False)
            .all()
        )