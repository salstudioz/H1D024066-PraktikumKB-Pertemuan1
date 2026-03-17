
#Tugas Praktikum Kecerdasan Buatan - Pertemuan 1

import random
import time

def main():
    # 1. IMPLEMENTASI LIBRARY (random & time)
    
    print("="*50)
    print("   SELAMAT DATANG DI SIMULATOR GRAND LINE   ")
    print("="*50)

    # 2. IMPLEMENTASI STRUKTUR DATA
    # List (Mutable): Kru Mugiwara yang bisa bertambah
    kru_topi_jerami = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji"]
    
    # Tuple (Immutable): Koordinat tujuan akhir (Laugh Tale) yang tidak boleh berubah
    koordinat_laugh_tale = (-0.1234, 123.4567)
    
    # Set (Unique): Koleksi Buah Iblis yang ditemukan (tidak boleh duplikat)
    buah_iblis_ditemukan = {"Gomu Gomu no Mi", "Hito Hito no Mi", "Ope Ope no Mi"}

    print(f"\nKru saat ini: {', '.join(kru_topi_jerami)}")
    print(f"Mencari koordinat Laugh Tale di: {koordinat_laugh_tale}")

    # 3. IMPLEMENTASI STRUKTUR KONTROL (Looping & Logic)
    target_bounty = 1000000000  # 1 Miliar Belly
    bounty_saat_ini = 0
    hari_berlayar = 0

    print("\n--- Mulai Berlayar ke Pulau Baru ---")
    
    # While Loop: Terus berlayar sampai bounty mencapai target
    while bounty_saat_ini < target_bounty:
        hari_berlayar += 1
        time.sleep(0.5) # efek jeda simulasi
        
        # Simulasi kejadian random
        kejadian = random.choice(["Lawan Marine", "Bertemu Nakama Baru", "Badai Laut"])
        
        print(f"Hari ke-{hari_berlayar}: {kejadian}")

        if kejadian == "Lawan Marine":
            tambahan = random.randint(50000000, 200000000)
            bounty_saat_ini += tambahan
            print(f"  > Menang! Bounty naik sebesar {tambahan:,} Belly.")
        
        elif kejadian == "Bertemu Nakama Baru":
            pilihan_nakama = ["Chopper", "Robin", "Franky", "Brook", "Jinbe"]
            nakama = random.choice(pilihan_nakama)
            
            # Percabangan IF untuk mengecek apakah sudah ada di list
            if nakama not in kru_topi_jerami:
                kru_topi_jerami.append(nakama)
                print(f"  > {nakama} telah bergabung dengan kru!")
            else:
                print(f"  > Bertemu {nakama}, tapi dia sudah di kapal.")
                
        elif kejadian == "Badai Laut":
            print("  > Cuaca buruk! Nami berhasil mengarahkan kapal dengan selamat.")

    # For Loop: Menampilkan status akhir kru
    print("\n" + "="*50)
    print(f"MISI SELESAI DALAM {hari_berlayar} HARI!")
    print(f"Total Bounty Akhir: {bounty_saat_ini:,} Belly")
    print("-" * 50)
    print("Daftar Kru Akhir:")
    
    for i, anggota in enumerate(kru_topi_jerami, 1):
        # Struktur Kontrol IF di dalam Loop
        status = "Kapten" if anggota == "Luffy" else "Anggota"
        print(f"{i}. {anggota} ({status})")

    # Menampilkan Set Buah Iblis
    print(f"\nKoleksi Buah Iblis Unik: {buah_iblis_ditemukan}")
    print("="*50)

if __name__ == "__main__":
    main()
