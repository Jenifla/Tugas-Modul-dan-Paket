#import package
import bgn_datar
import bgn_ruang

#fungsi untuk menampilkan menu utama
def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Bangun 2 Dimensi")
    print("[2] Bangun 3 Dimensi")
    print("[3] Lainnya")

#fungsi untuk menampilkan submenu bangun 2 dimensi
def dimensi2():
    print("\n")
    print("----------- Bangun 2 Dimensi ----------")
    print("[1] Persegi")
    print("[2] Persegi Panjang")
    print("[3] Segitiga")
    print("[4] Lingkaran")
    print("[5] Jajargenjang")
    print("[6] Trapesium")

#fungsi untuk menampilkan submenu bangun 3 dimensi
def dimensi3():
    print("\n")
    print("----------- Bangun 3 Dimensi ----------")
    print("[1] Kubus")
    print("[2] Balok")
    print("[3] Tabung")
    print("[4] Kerucut")
    print("[5] Limas")
    print("[6] Prisma")

#fungsi untuk menampilkan menu utama dan submenu sesuai pilihan pengguna
def main():
    #menampilkan menu utama dan meminta pengguna menginputkan pilihan menu
    show_menu()
    menu = input("PILIH MENU> ")
    print("\n")

    #jika pengguna memilih menu 1 maka program akan menampilkan submenu dimensi2 dan pengguna diminta untuk memilih menu yang ada dalam submenu dimensi2
    if menu == "1": 
        dimensi2()
        menu= input("PILIH MENU> ")
        print("\n")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_persegi dan menampilkan hasil perhitungan luas persegi
        if menu == "1":
            hasil_persegi= bgn_datar.persegi.ht_persegi(20)
            print(f"Luas Persegi = {hasil_persegi}")
        #jika pengguna memilih submenu 2 maka program akan memanggil fungsi ht_persepanjang dan menampilkan hasil perhitungan luas persegi panjang
        elif menu == "2":
            hasil_persepanjang= bgn_datar.persegipjng.ht_persepanjang(15, 8)
            print(f"Luas Persegi Panjang = {hasil_persepanjang}")
        #jika pengguna memilih submenu 3 maka program akan memanggil fungsi ht_segitiga dan menampilkan hasil perhitungan luas segitiga
        elif menu == "3":
            hasil_segitiga= bgn_datar.segitiga.ht_segitiga(6, 12)
            print(f"Luas Segitiga = {hasil_segitiga}")
        #jika pengguna memilih submenu 4 maka program akan memanggil fungsi ht_lingkaran dan menampilkan hasil perhitungan luas lingkaran
        elif menu == "4":
            hasil_lingkaran= bgn_datar.lingkaran.ht_lingkaran(7)
            print(f"Luas Lingkaran = {hasil_lingkaran}")
        #jika pengguna memilih submenu 5 maka program akan memanggil fungsi ht_jajargenjang dan menampilkan hasil perhitungan luas jajargenjang
        elif menu == "5":
            hasil_jajargenjang= bgn_datar.jajargenjang.ht_jajargenjang(9, 14)
            print(f"Luas Jajar Genjang= {hasil_jajargenjang}")
        #jika pengguna memilih submenu 6 maka program akan memanggil fungsi ht_trapesium dan menampilkan hasil perhitungan luas trapesium
        else:
            hasil_trapesium= bgn_datar.trapesium.ht_trapesium(6, 6, 4)
            print(f"Luas Trapesium= {hasil_trapesium}")
    #jika pengguna memilih menu 2 maka program akan menampilkan submenu dimensi3 dan pengguna diminta untuk memilih menu yang ada dalam submenu dimensi3
    elif menu == "2":
        dimensi3()
        menu= input("PILIH MENU> ")
        print("\n")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_kubus dan menampilkan hasil perhitungan volume kubus
        if menu == "1":
            hasil_kubus = bgn_ruang.ht_kubus(10)
            print(f"Volume Kubus = {hasil_kubus}")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_balok dan menampilkan hasil perhitungan volume balok
        elif menu == "2":
            hasil_balok= bgn_ruang.ht_balok(12, 6, 9)
            print(f"Volume Balok = {hasil_balok}")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_tabung dan menampilkan hasil perhitungan volume tabung
        elif menu == "3":
            hasil_tabung= bgn_ruang.ht_tabung(14, 24)
            print(f"Volume Tabung = {hasil_tabung}")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_kerucut dan menampilkan hasil perhitungan volume kerucut
        elif menu == "4":
            hasil_kerucut= bgn_ruang.ht_kerucut(15, 27)
            print(f"Volume Kerucut = {hasil_kerucut}")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_limas dan menampilkan hasil perhitungan volume limas
        elif menu == "5":
            hasil_limas = bgn_ruang.ht_limas(12, 19)
            print(f"Volume Limas = {hasil_limas}")
        #jika pengguna memilih submenu 1 maka program akan memanggil fungsi ht_prisma dan menampilkan hasil perhitungan volume prisma
        else:
            hasil_prisma= bgn_ruang.ht_prisma(9, 12, 21)
            print(f"Volume Prisma = {hasil_prisma}")
    #jika pengguna memilih menu 3 maka program akan berhenti
    else:
        exit()
#fungsi untuk memanggil fungsi main
if __name__ == '__main__':
    main()
