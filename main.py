from services.kost import Kost
from models.kamar import KamarStandard, KamarDeluxe
from models.penghuni import Penghuni


def main():
    # Membuat objek Kost
    kost = Kost()

    # Menambahkan kamar
    kamar1 = KamarStandard(
        "101",
        750000,
        ["Kasur", "Lemari", "Kipas Angin"]
    )

    kamar2 = KamarDeluxe(
        "201",
        1200000,
        ["Kasur", "Lemari", "AC", "TV"],
        24
    )

    kost.tambah_kamar(kamar1)
    kost.tambah_kamar(kamar2)

    print("===== DAFTAR KAMAR =====")
    kost.tampilkan_kamar()

    # Membuat penghuni
    penghuni = Penghuni(
        "Dian Laranga",
        "3578123456789001",
        "081234567890"
    )

    # Menyewa kamar
    kontrak = kost.sewa_kamar(
        penghuni,
        kamar1,
        "11-07-2026"
    )

    print("\n===== SETELAH KAMAR DISEWA =====")
    kost.tampilkan_kamar()

    print("\n===== DATA KONTRAK =====")
    print(kontrak)

    # Pembayaran
    kontrak.bayar("15-07-2026")

    print("\n===== SETELAH PEMBAYARAN =====")
    print(kontrak)


if __name__ == "__main__":
    main()