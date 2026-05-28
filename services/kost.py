class Kost:
    def __init__(self):
        self.daftar_kamar = []
        self.daftar_penghuni = []
        self.daftar_kontrak = []

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)

    def tambah_penghuni(self, penghuni):
        self.daftar_penghuni.append(penghuni)

    def tambah_kontrak(self, kontrak):
        self.daftar_kontrak.append(kontrak)