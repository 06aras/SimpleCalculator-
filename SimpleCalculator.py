print("""*************************
Basit Hesap Makinesi Programı
İşlemler;
1. Toplama İşlemi

2. Çıkartma İşlemi

3. Çarpma İşlemi

4. Bölme işlemi
********************
""")

try:
    a=float(input("Birinci Sayı:"))#Inputları int olarak değil de float olarak almak istedim .
    b=float(input("İkinci Sayı:"))#Inputları int olarak değil de float olarak almak istedim .
except ValueError:#Sayı değerli olmayan bir verinin, float() fonksiyonu aracılığıyla sayıya çevrilmeye çalışılması.
    print("Lütfen inputu sayı girin.")
    print("Programdan çıkılıyor...")
    quit()




işlem=input("İşlemi Giriniz:")

if işlem== "1":#Kullanıcı işlem 1'i seçerse toplama işlemi yapılacak.
    print ("{} ile {} in toplamı {} dir.".format(a,b,a+b))

elif işlem== "2":#Kullanıcı işlem 2'i seçerse çıkartma işlemi yapılacak.
    print ("{} den {} çıkarsa sonuç  {} dir.".format(a,b,a-b))

elif işlem== "3":#Kullanıcı işlem 3'i seçerse çarpma işlemi yapılacak.
    print ("{} ile {} in çarpımı {} dir.".format(a,b,a*b))

elif işlem== "4":#Kullanıcı işlem 4'i seçerse bölme işlemi yapılacak.
    try:
        print ("{} i {} e bölersek sonuç {} dir.".format(a,b,a/b))
    except ZeroDivisionError:#Buradaki sorun ise, bir sayının 0’a bölünmeye çalışılıyor olması.
        print("Bir sayı 0'a bölünemez.")

else:#Kullanıcı 1-4 aralığından hariç bir işlem seçerse program sonlanır.
    print("Geçersiz İşlem!!")

