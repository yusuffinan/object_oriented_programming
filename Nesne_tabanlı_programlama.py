class calisan():
    def __init__(self,isim,maas,departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgi(self):
        print(f"{self.isim}, {self.maas}, {self.departman} :)" )
    def degisim(self,yenidep):
        self.departman = yenidep
a = calisan("yusuf",25000,"bilişim")
a.bilgi()

class yönetici(calisan):
    def zam(self, zammiktar):
        self.maas += zammiktar
    def __init__(self,isim,maas,departman,kisi):
        super().__init__(isim,maas,departman)
        
        self.kisi = kisi
    def bilgi(self):
        print(f"{self.isim}, {self.maas}, {self.departman},{self.kisi} " )
yöneti= yönetici("serhat inan",30000,"bilişim",10)
yöneti.bilgi()
yöneti.degisim("insan kaynakları")
yöneti.zam(600)
yöneti.bilgi()
