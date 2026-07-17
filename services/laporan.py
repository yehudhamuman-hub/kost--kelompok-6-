"""
services/laporan.py
Layer 2 - Pipeline laporan menggunakan map, filter, dan sorted.
Tidak ada loop 'for' / 'while' eksplisit di dalam fungsi-fungsi ini.
"""

from functools import reduce

from models.kamar import Kamar, KamarDeluxe
from models.kontrak import Kontrak


def tipe_dari(kamar: Kamar) -> str:
    """Fungsi bantu: tentukan tipe kamar ('standard' / 'deluxe') via isinstance()."""
    return "deluxe" if isinstance(kamar, KamarDeluxe) else "standard"


def kamar_tersedia(daftar_kamar: list[Kamar]) -> list[Kamar]:
    """Filter kamar yang terisi == False, urutkan dari harga terendah ke tertinggi."""
    kosong = filter(lambda k: not k.terisi, daftar_kamar)
    return sorted(kosong, key=lambda k: k.harga)


def _akumulasi_tipe(acc: dict, kamar: Kamar) -> dict:
    """Fungsi bantu untuk reduce(): tambahkan harga kamar ke total tipenya."""
    t = tipe_dari(kamar)
    acc[t] = acc.get(t, 0) + kamar.harga
    return acc


def total_pendapatan_per_tipe(daftar_kamar: list[Kamar]) -> dict:
    """
    Filter kamar yang terisi == True, lalu jumlahkan harga per tipe
    menggunakan filter + reduce (tanpa loop eksplisit).
    """
    terisi = filter(lambda k: k.terisi, daftar_kamar)
    return reduce(_akumulasi_tipe, terisi, {})


def kontrak_diurutkan_tanggal(daftar_kontrak: list[Kontrak]) -> list[Kontrak]:
    """Filter kontrak yang belum lunas, urutkan tanggal_masuk dari terlama ke terbaru."""
    belum_lunas = filter(lambda k: not k.status.is_lunas(), daftar_kontrak)
    return sorted(belum_lunas, key=lambda k: k.tanggal_masuk)


def ringkasan_penghuni(daftar_kontrak: list[Kontrak]) -> list[str]:
    """Map setiap kontrak ke string ringkasan."""
    return list(
        map(
            lambda k: f"{k.penghuni.nama} — Kamar {k.kamar._nomor} — {k.status.keterangan()}",
            daftar_kontrak,
        )
    )