import qrcode
import os

def generate_qr():
    # 1. Kullanıcıdan Link İste
    print("--------------------------------")
    print("🔹 Python QR Code Generator 🔹")
    print("--------------------------------")
    
    data = input("QR Koda dönüştürülecek linki girin: ")
    if not data:
        print("❌ Boş veri girdiniz!")
        return

    file_name = input("Dosya adı ne olsun? (Örn: github_profil): ")
    if not file_name.endswith(".png"):
        file_name += ".png"

    # 2. QR Kodunu Oluştur (Gelişmiş Ayarlar)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    
    qr.add_data(data)
    qr.make(fit=True)

    # 3. Görsele Çevir ve Kaydet
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    print(f"\n✅ Başarılı! '{file_name}' oluşturuldu.")
    print(f"📂 Kayıt Yeri: {os.getcwd()}/{file_name}")

if __name__ == "__main__":
    generate_qr()