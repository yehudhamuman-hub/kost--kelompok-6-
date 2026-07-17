from services.kost import Kost
from models.kamar import KamarStandard, KamarDeluxe
from models.penghuni import Penghuni

from database.db_handler import (
    init_db,
    simpan_kamar,
    simpan_kontrak,
    update_status_lunas,
    update_status_kamar
)

def main():
    # Membuat objek Kost
    kost = Kost()
    init_db()

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
    
    simpan_kamar(
    kamar1.nomor,
    "standard",
    kamar1.harga
)
    kost.tambah_kamar(kamar2)
    simpan_kamar(
    kamar2.nomor,
    "deluxe",
    kamar2.harga
)

    print("===== DAFTAR KAMAR =====")
    kost.tampilkan_kamar()

    # Membuat penghuni
    penghuni = Penghuni(
    "Yehudha Muman",
    "3578123456789001",
    "082345144370"
)

    # Menyewa kamar
    kontrak = kost.sewa_kamar(
        penghuni,
        kamar1,
        "11-07-2026"
    )
    update_status_kamar(kamar1.nomor, True)
    
    simpan_kontrak(
    1,
    penghuni.nama,
    penghuni.no_ktp,
    penghuni.no_hp,
    "11-07-2026"
)


    print("\n===== SETELAH KAMAR DISEWA =====")
    kost.tampilkan_kamar()

    print("\n===== DATA KONTRAK =====")
    print(kontrak)

    # Pembayaran
    kontrak.bayar("15-07-2026")

    update_status_lunas(1)

    print("\n===== SETELAH PEMBAYARAN =====")
    print(kontrak)


if __name__ == "__main__":
    main()