
# kost--kelompok-6-
membuat apklikasi bebasis CLI dengan tema sistem kost-kostan untuk mata kuliah pemrograman lanjut
python main.py
python -m pytest tests/ -v
models-kamar,models-pembayaran,kontrak,kos-main
                    +------------------+
                    |      Kamar       |
                    +------------------+
                    | - nomor          |
                    | - harga          |
                    +------------------+
                    | + __init__()     |
                    +------------------+
                             ▲
               ┌─────────────┴─────────────┐
               │                           │
     +-------------------+      +-------------------+
     |   KamarStandar    |      |   KamarDeluxe    |
     +-------------------+      +-------------------+
     | - fasilitas       |      | - fasilitas       |
     |                   |      | - luas            |
     +-------------------+      +-------------------+
     | + __init__()      |      | + __init__()      |
     +-------------------+      +-------------------+



                    +------------------+
                    |    Penghuni      |
                    +------------------+
                    | - nama           |
                    | - ktp            |
                    | - no_hp          |
                    +------------------+
                    | + __init__()     |
                    +------------------+



                 +----------------------+
                 |    <<Abstract>>      |
                 |     StatusSewa       |
                 +----------------------+
                 |                      |
                 +----------------------+
                 | + status()           |
                 +----------------------+
                             ▲
               ┌─────────────┴─────────────┐
               │                           │
      +-------------------+      +-------------------+
      |       Lunas       |      |    BelumLunas    |
      +-------------------+      +-------------------+
      |                   |      |                   |
      +-------------------+      +-------------------+
      | + status()        |      | + status()        |
      +-------------------+      +-------------------+



                    +----------------------+
                    |       Kontrak        |
                    +----------------------+
                    | - penghuni           |
                    | - kamar              |
                    | - tanggal_masuk      |
                    | - status_sewa        |
                    +----------------------+
                    | + __init__()         |
                    +----------------------+
                         |        |       |
                         |        |       |
                         v        v       v
                   +---------+ +------+ +-------------+
                   |Penghuni | |Kamar | | StatusSewa |
                   +---------+ +------+ +-------------+



                    +----------------------+
                    |         Kost         |
                    +----------------------+
                    | - daftar_kamar       |
                    | - daftar_penghuni    |
                    | - daftar_kontrak     |
                    +----------------------+
                    | + tambah_kamar()     |
                    | + tambah_penghuni()  |
                    | + tambah_kontrak()   |
                    +----------------------+



             +----------------------------------+
             |      Custom Exceptions           |
             +----------------------------------+
             | KamarPenuhError                  |
             | PenghuniTidakDitemukanError      |
             | KamarTidakDitemukanError         |
             | PembayaranGandaError             |
             +----------------------------------+
             
models/
services/
exceptions/
tests/
Tujuannya agar kode lebih:

rapi
mudah dibaca
mudah dikembangkan
mudah diperbaiki jika terjadi error

Dengan pemisahan ini, setiap folder memiliki tugas masing-masing.
