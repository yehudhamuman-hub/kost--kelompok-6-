class Penghuni:

    def __init__(self, nama, no_ktp, no_hp):
        self.nama = nama
        self.no_ktp = no_ktp
        self.no_hp = no_hp

    def __str__(self):
        return f"{self.nama} ({self.no_hp})"