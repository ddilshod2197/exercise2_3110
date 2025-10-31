class Televizor:
    def __init__(self, brend, ovoz, kanal):
        self.brend = brend
        self.ovoz = ovoz
        self.kanal = kanal

    def ovoz_oshir(self, miqdor=1):
        self.ovoz += miqdor
        print(f"Ovoz darajasi: {self.ovoz}")

    def kanal_ozgartir(self, yangi_kanal):
        self.kanal = yangi_kanal
        print(f"Yangi kanal: {self.kanal}")



tv1 = Televizor("Samsung", 10, 5)
print(f"Brend: {tv1.brend}, Ovoz: {tv1.ovoz}, Kanal: {tv1.kanal}")

tv1.ovoz_oshir(3)
tv1.kanal_ozgartir(7)
