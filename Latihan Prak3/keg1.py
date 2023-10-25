def konversi(minggu=0, hari=0, jam=0):
    def menit(menit=0):
        return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)

    return menit

# Data dalam format yang diinginkan
data_list = ["3 minggu 3 hari 7 jam 21 menit",
             "5 minggu 5 hari 8 jam 11 menit",
             "7 minggu 1 hari 0 jam 33 menit"]

# Iterasi melalui setiap data dalam daftar
for data in data_list:
    data_parts = data.split()
    minggu = 0
    hari = 0
    jam = 0
    menit = 0

    # Iterasi melalui setiap bagian data dan mengidentifikasi komponennya
    for part in data_parts:
        if part == "minggu":
            minggu = int(data_parts[data_parts.index(part) - 1])
        elif part == "hari":
            hari = int(data_parts[data_parts.index(part) - 1])
        elif part == "jam":
            jam = int(data_parts[data_parts.index(part) - 1])
        elif part == "menit":
            menit = int(data_parts[data_parts.index(part) - 1])

    konvert = konversi(minggu, hari, jam)(menit)
    print(f"Data: {data}, Hasil konversi: {konvert} menit")
