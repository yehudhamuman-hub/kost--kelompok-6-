from abc import ABC, abstractmethod


class StatusSewa(ABC):

    @abstractmethod
    def status(self):
        pass


class Lunas(StatusSewa):

    def status(self):
        return "Sudah Dibayar"


class BelumLunas(StatusSewa):

    def status(self):
        return "Belum Dibayar"