class animals():
    def __init__(self, number,animal_species,age, feed =1,vaccine =0):
        self.number = number
        self.animal_species = animal_species
        self.age = age
        self.feed = feed
        self.vaccine =vaccine
    def information(self):
        print(f"numarası | {self.number}\n hayvan türü | {self.animal_species}\n yaş | {self.age}\n günlük mama miktarı {self.feed}")
    def feedchange(self,feedinc):
        print("mama miktarı değiştiriliyor")
        if self.feed <=10:
            self.feed += feedinc
        else:
            print("günclük mama limitine ulaştınız")
class dog(animals):
    def vaccines(self, vaccine_status):
        self.vaccine += vaccine_status
        print("yapilan aşi sayisi", self.vaccine)

tony =dog(1,"köpek", 2,3,5)
tony.information()
tony.vaccines(1)