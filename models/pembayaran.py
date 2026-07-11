from abc import ABC, abstractmethod


class StatusSewa(ABC):

    @abstractmethod
    def keterangan(self):
        pass

    @abstractmethod
    def is_lunas(self):
        pass


class Lunas(StatusSewa):

    def __init__(self, tanggal_bayar):
        self.tanggal_bayar = tanggal_bayar

    def keterangan(self):
        return "Lunas"

    def is_lunas(self):
        return True


class BelumLunas(StatusSewa):

    def __init__(self, jatuh_tempo):
        self.jatuh_tempo = jatuh_tempo

    def keterangan(self):
        return "Belum Lunas"

    def is_lunas(self):
        return False

    def hitung_denda(self, hari):
        return hari * 5000