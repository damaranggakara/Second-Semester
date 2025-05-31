class Unggas:
    def __init__(self):
        self.bertelur = True
        self.bersayap = True

    def output(self):
        return "Unggas itu:\nBertelur\nBersayap\n"

class Ayam(Unggas):
    def __init__(self):
        self.berkokok = True

    def output(self):
        return "Ayam itu:\nBertelur\nBersayap\nBerkokok\n"

class Bebek(Unggas):
    def __init__(self):
        self.berenang = True

    def output(self):
        return "Bebek itu:\nBertelur\nBersayap\nBerenang\n"

class Burung(Unggas):
    def __init__(self):
        self.terbang = True

    def output(self):
        return "Burung itu:\nBertelur\nBersayap\nTerbang\n"

def main():
    pilihan = input("Pilih jenis unggas (unggas/ayam/bebek/burung): ")
    if pilihan.lower() == "unggas":
        unggas = Unggas()
        print(unggas.output())
    elif pilihan.lower() == "ayam":
        ayam = Ayam()
        print(ayam.output())
    elif pilihan.lower() == "bebek":
        bebek = Bebek()
        print(bebek.output())
    elif pilihan.lower() == "burung":
        burung = Burung()
        print(burung.output())
    else:
        print("Pilihan tidak valid.")
main()
