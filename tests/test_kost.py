import unittest

from services.kost import Kost
from models.kamar import KamarStandard
from models.penghuni import Penghuni


class TestKost(unittest.TestCase):

    def setUp(self):
        self.kost = Kost()

        self.kamar = KamarStandard(
            "101",
            750000,
            ["Kasur", "Lemari", "Kipas"]
        )

        self.penghuni = Penghuni(
            "Dian",
            "3578123456789001",
            "08123456789"
        )

    def test_tambah_kamar(self):
        self.kost.tambah_kamar(self.kamar)
        self.assertEqual(len(self.kost._daftar_kamar), 1)

    def test_sewa_kamar(self):
        self.kost.tambah_kamar(self.kamar)

        kontrak = self.kost.sewa_kamar(
            self.penghuni,
            self.kamar,
            "11-07-2026"
        )

        self.assertTrue(self.kamar.terisi)
        self.assertEqual(kontrak.penghuni.nama, "Dian")

    def test_bayar(self):
        self.kost.tambah_kamar(self.kamar)

        kontrak = self.kost.sewa_kamar(
            self.penghuni,
            self.kamar,
            "11-07-2026"
        )

        kontrak.bayar("15-07-2026")

        self.assertTrue(kontrak.status.is_lunas())


if __name__ == "__main__":
    unittest.main()