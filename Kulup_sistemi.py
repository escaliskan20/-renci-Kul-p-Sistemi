# Öğrenci Kulüp Sistemi (Set + Fonksiyonlar)

Kulüpler
müzik_kulubu = set()
spor_kulubu = set()
bilim_kulubu = set()

def ogrenci_ekle(kulup, isim):
    kulup.add(isim)
    print(f"{isim} başarıyla eklendi.")

def ogrenci_sil(kulup, isim):
    if isim in kulup:
        kulup.remove(isim)
        print(f"{isim} kulüpten silindi.")
    else:
        print(f"{isim} bu kulüpte bulunamadı.")

def listele(kulup, kulup_adi):
    if kulup:
        print(f"\n{kulup_adi} üyeleri:")
        for ogrenci in kulup:
            print("-", ogrenci)
    else:
        print(f"\n{kulup_adi} henüz boş.")
        
def ortak_uyeler(kulup1, kulup2):
    return kulup1.intersection(kulup2)

def tum_uyeler():
    return müzik_kulubu.union(spor_kulubu, bilim_kulubu)


# --- Kullanım Örneği ---
if __name__ == "__main__":
    ogrenci_ekle(müzik_kulubu, "Ahmet")
    ogrenci_ekle(spor_kulubu, "Ayşe")
    ogrenci_ekle(bilim_kulubu, "Mehmet")
    ogrenci_ekle(müzik_kulubu, "Mehmet")

    listele(müzik_kulubu, "Müzik Kulübü")
    listele(spor_kulubu, "Spor Kulübü")
    listele(bilim_kulubu, "Bilim Kulübü")

    print("\nMüzik & Bilim ortak üyeler:", ortak_uyeler(müzik_kulubu, bilim_kulubu))
    print("\nTüm üyeler:", tum_uyeler())

Öğrenci kulüp sistemi setler + fonksiyonlar kullanılarak yapılmaya çalışıldı 
