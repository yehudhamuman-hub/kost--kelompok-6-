from sqlalchemy import (
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    Mapped,
    mapped_column
)


class Base(DeclarativeBase):
    pass


class KamarDB(Base):
    __tablename__ = "kamar"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nomor: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    tipe: Mapped[str] = mapped_column(String(20))
    harga: Mapped[float] = mapped_column(Float)
    terisi: Mapped[bool] = mapped_column(Boolean, default=False)

    kontrak_list = relationship(
        "KontrakDB",
        back_populates="kamar",
        cascade="all, delete-orphan"
    )


class KontrakDB(Base):
    __tablename__ = "kontrak"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    kamar_id: Mapped[int] = mapped_column(
        ForeignKey("kamar.id")
    )

    nama_penghuni: Mapped[str] = mapped_column(String(100))
    no_ktp: Mapped[str] = mapped_column(String(20))
    no_hp: Mapped[str] = mapped_column(String(20))
    tanggal_masuk: Mapped[str] = mapped_column(String(20))

    status_lunas: Mapped[bool] = mapped_column(Boolean, default=False)

    kamar = relationship(
        "KamarDB",
        back_populates="kontrak_list"
    )