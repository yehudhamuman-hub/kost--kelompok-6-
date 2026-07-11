from models.kamar import KamarStandard, KamarDeluxe
from models.penghuni import Penghuni
from models.kontrak import Kontrak


class Kost:

    def __init__(self):
        self._daftar_kamar = []
        self._kontrak = []

    def tambah_kamar(self, kamar):
        self._daftar_kamar.append(kamar)

    def tampilkan_kamar(self):
        for k in self._daftar_kamar:
            print(k)

    def sewa_kamar(self, penghuni, kamar, tanggal):
        kontrak = Kontrak(penghuni, kamar, tanggal)
        self._kontrak.append(kontrak)
        return kontrak

    def tampilkan_kontrak(self):
        for k in self._kontrak:
            print("----------------")
            print(k)