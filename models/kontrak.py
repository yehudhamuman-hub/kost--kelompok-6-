from models.pembayaran import BelumLunas, Lunas


class Kontrak:

    def __init__(self, penghuni, kamar, tanggal_masuk):
        self.penghuni = penghuni
        self.kamar = kamar
        self.tanggal_masuk = tanggal_masuk
        self.status = BelumLunas("01-08-2026")

        kamar.isi()

    def bayar(self, tanggal_bayar):
        self.status = Lunas(tanggal_bayar)

    def __str__(self):
        return (
            f"Penghuni : {self.penghuni}\n"
            f"{self.kamar}\n"
            f"Status : {self.status.keterangan()}"
        )