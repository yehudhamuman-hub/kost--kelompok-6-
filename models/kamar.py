from abc import ABC


class KamarPenuhError(Exception):
    pass


class Kamar(ABC):
    def __init__(self, nomor: str, harga: float):
        self._nomor = nomor
        self.harga = harga
        self._terisi = False
    @property
    def nomor(self):
        return self._nomor   

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, value):
        if value < 0:
            raise ValueError("Harga tidak boleh negatif")
        self._harga = value

    @property
    def terisi(self):
        return self._terisi

    def isi(self):
        if self._terisi:
            raise KamarPenuhError("Kamar sudah terisi")
        self._terisi = True

    def kosongkan(self):
        self._terisi = False

    def __str__(self):
        status = "Terisi" if self._terisi else "Kosong"
        return f"Kamar {self._nomor} | Harga:{self._harga} | {status}"


class KamarStandard(Kamar):
    def __init__(self, nomor, harga, fasilitas):
        super().__init__(nomor, harga)
        self.fasilitas = fasilitas

    def __str__(self):
        return super().__str__() + f" | Fasilitas: {', '.join(self.fasilitas)}"


class KamarDeluxe(Kamar):
    def __init__(self, nomor, harga, fasilitas, luas):
        super().__init__(nomor, harga)
        self.fasilitas = fasilitas
        self.luas_m2 = luas

    def __str__(self):
        return super().__str__() + f" | Luas:{self.luas_m2} m2"