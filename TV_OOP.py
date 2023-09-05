import time
import random

class rcontrol():
    def __init__(self,tv_status="off", sound= 0, channellist=["trt1"], channel = "trt1"):
        self.tv_status = tv_status
        self.sound = sound
        self.channellist = channellist
        self.channel = channel

    def tv_on(self):
        if self.tv_status =="on":
            print("tv zaten açik")
        else:
            print("televizyon açiliyor...")
            time.sleep(1)
            self.tv_status = "on"
    def tv_off(self):
        if self.tv_status == "off":
            print("tv zaten kapali")
        else:
            print("tv kapaniyor...")
            time.sleep(1)
            self.tv_status = "off"

    def sounds(self):
        
        while True:
            slevel = input("sesi arttirmak için: a tuşu \n azaltmak için k tuşuna basiniz \n çikiş için q")
            if slevel == "k":
                if self.sound != 0:
                    self.sound -= 1
                    print("ses: ", self.sound)
            elif slevel == "a":
                if self.sound !=60:
                    self.sound += 1
                    print("ses: ", self.sound)
            elif slevel == "q":
                print("çikiş yapiliyor..."),
                time.sleep(1)
                break
            else:
                print("anlamsiz tuş.")

    def channel_in(self, ch_ap):
        print("kanal ekleme ekranina hoş geldiniz. ")
        if ch_ap in self.channellist:
            print("eklemek istediğiniz kanal zaten mevcut")
        else:
            self.channellist.append(ch_ap)
            print(self.channellist)

    def channelc(self,knl):
        kanal =0
        while True:
            print("kanal değişiyor...")
            time.sleep(1)
            if knl == "next":
                kanal += 1
                self.channel = self.channellist[kanal]
                print("kanal: ", self.channel)
            
            elif knl == "back":
                kanal-=1
                self.channel = self.channellist[kanal]
                print("kanal: ", self.channel)

            elif knl == "random":
                rand_ch = random.randint(0, len(self.channellist)-1)
                self.channel = self.channellist[rand_ch]
                print("kanal: ", self.channel)
            questt = input("bu kanal kalsin mi cevap evetse q değilse rastgele değer giriniz")
            if questt == "q":
                break
            else:
                continue

    def __len__(self):
        return len(self.channellist)
    
    def __str__(self):
        return """tv durumu {}\n 
             tv ses {}\n 
             tv listesi {}\n 
             şu anki kanal {}\n
             """.format(self.tv_status,self.sound, self.channellist,self.channel)
    
control =rcontrol()
        
print("""
TV UYGULAMASINA HOŞ GELDİNİZ.\n
      -----------------------\n
      TV aç  = 1 \n
      TV kapat = 2 \n
      Ses ayarlari = 3 \n
      Kanal ekleme = 4 \n
      Kanal değişimi = 5 (next ileri, back geri, rastgele ise random) \n
      Tv durumu için = 6 \n
      Çikiş için = q
""")

while True:
    choice = input("işlemi seçiniz")
    if choice == "q":
        print("çikiş yapiliyor..")
        break
    elif choice == "1":
        control.tv_on()
    elif choice == "2":
        control.tv_off()
    elif choice == "3":
        control.sounds()
    elif choice == "4":
        chn = input("eklemek istediğiniz kanali giriniz")
        control.channel_in(chn)
    elif choice == "5":
        chnc = input("next or back or random")
        control.channelc(chnc)
    elif choice == "6":
        print(control)
    elif choice == "q":
        print("çikiş yapiliyor")
        break
    else:
        print("hatali seçim")