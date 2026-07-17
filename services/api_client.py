"""
services/api_client.py
Layer 2 - Konsumsi REST API frankfurter.app untuk kurs mata uang real-time.
"""

import requests

BASE_URL = "https://api.frankfurter.app"


def get_kurs(mata_uang_tujuan: str) -> float:
    """
    Ambil kurs IDR -> mata_uang_tujuan dari frankfurter.app.

    Raise:
        ConnectionError: jika timeout atau tidak ada koneksi.
        ValueError: jika API mengembalikan status error (4xx/5xx)
                    atau mata uang tidak valid.
    """
    url = f"{BASE_URL}/latest"
    params = {"from": "IDR", "to": mata_uang_tujuan}

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.Timeout:
        raise ConnectionError(
            "Tidak dapat terhubung ke layanan kurs mata uang (timeout)."
        )
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "Tidak dapat terhubung ke internet / layanan kurs mata uang."
        )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise ValueError(
            f"Gagal mengambil kurs (status {response.status_code}). "
            f"Periksa kode mata uang '{mata_uang_tujuan}'."
        )

    data = response.json()
    rates = data.get("rates", {})

    if mata_uang_tujuan not in rates:
        raise ValueError(f"Mata uang '{mata_uang_tujuan}' tidak valid.")

    return float(rates[mata_uang_tujuan])


def harga_dalam_mata_uang(harga_idr: float, mata_uang_tujuan: str) -> str:
    """
    Konversi harga_idr ke mata uang tujuan.
    Return string siap tampil, contoh: "USD 51.20".
    """
    kurs = get_kurs(mata_uang_tujuan)
    hasil = harga_idr * kurs
    return f"{mata_uang_tujuan} {hasil:.2f}"