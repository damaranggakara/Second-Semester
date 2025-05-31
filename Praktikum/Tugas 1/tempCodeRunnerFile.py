#PENJUALAN/PEMBELIAN WARUNG
#pembuatan class
class inventory:
    def __init__(self, item, jumlah, harga):
        self.item = item
        self.jumlah = jumlah
        self.harga = harga
    def __str__(self):
        return f"{self.item}, stock: {self.jumlah}, harga: {self.harga} IDR"

#rumus pembelian barang
def rumus_harga(items):
    harga_total = 0
    num_items = sum(items.values())
    for item, jumlah in items.items():
        harga_total += item.harga * jumlah
    #diskon 10% min 5 barang
    if num_items >= 5:
        diskon = harga_total * 0.1
        harga_diskon = harga_total - diskon
        print(f"Harga sebelum diskon: {harga_total} IDR")
        print(f"Diskon (10%): {diskon} IDR")
        print(f"Total setelah diskon: {harga_diskon} IDR")
        return harga_diskon
    print(f"Harga Total: {harga_total} IDR")
    return harga_total

#isi class
telur = inventory("Telur", 20, 10000)
garam = inventory("Garam", 20, 15000)
gula = inventory("Gula", 20, 13000)
tepung = inventory("Tepung", 20, 12000)
beras = inventory("Beras", 20, 6000)
galon = inventory("Galon", 20, 9000)
kecap = inventory("Kecap", 20, 5000)
bawang = inventory("Bawang", 20, 7000)
lada = inventory("Lada", 20, 20000)
cabe = inventory("Cabe", 20, 16000)

#display inventory
all_items = [telur, garam, gula, tepung, beras, galon, kecap, bawang, lada, cabe]
for item in all_items:
    print(item)

#input pembelian
pembelian = {}
while True:
    barang_terpilih = input("Masukkan nama barang yang ingin dibeli (ketik 'selesai' kalau sudah): ").capitalize()
    if barang_terpilih == 'Selesai':
        break
    jumlah_barang = int(input(f"jumlah {barang_terpilih}: "))
    for item in all_items:
        if item.item == barang_terpilih:
            pembelian[item] = jumlah_barang
            break

#total pembelian
harga_pembelian = rumus_harga(pembelian)
print("Harga total:", harga_pembelian, "IDR")
