from services.kost import Kost
from models.kamar import KamarStandar


def test_tambah_kamar():
    kost = Kost()

    kamar = KamarStandar("A01", 500000, "WiFi")

    kost.tambah_kamar(kamar)

    assert len(kost.daftar_kamar) == 1