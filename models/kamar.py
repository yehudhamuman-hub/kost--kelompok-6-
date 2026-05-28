class Kamar:
    def __init__(self, nomor, harga):
        self.nomor = nomor
        self.harga = harga


class KamarStandar(Kamar):
    def __init__(self, nomor, harga, fasilitas):
        super().__init__(nomor, harga)
        self.fasilitas = fasilitas


class KamarDeluxe(Kamar):
    def __init__(self, nomor, harga, fasilitas, luas):
        super().__init__(nomor, harga)
        self.fasilitas = fasilitas
        self.luas = luas