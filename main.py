##############################################
#         SerbaGuna With Python              #
##############################################
import subprocess
import sys


def clear():
    input("Pencet Enter untuk kembali ke menu....")
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)
    menu()

def menu():
    print("\033[1;32;40m---------------------------------------------\n")
    print("|            ▄︻デֆɛʀɮǟɢʊռǟ══━-            |")
    print("|         Made Original By Dnayaka         |")
    print("--------------------------------------------")
    print("|                                          |")
    print("|        1. Menghitung Bangun Ruang        |")
    print("|        2. Menghitung Bangun Datar        |")
    print("|             3. Konversi Suhu             |")
    print("|                                          |")
    print("--------------------------------------------")
    Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")

    if Q == "1":
        Bangun_Ruang()
    else:
        print("Opsi Tidak Tersedia!!")
        menu()

def Bangun_Ruang():
    print("---------------------------------------------")
    print("|           ▄︻デɮǟռɢʊռ_ʀʊǟռɢ══━一          |")
    print("|          Made Original By Dnayaka         |")
    print("--------------------------------------------|")
    print("|                                           |")
    print("|                 1. Bola                   |")
    print("|                 2. Balok                  |")
    print("|                 3. Kubus                  |")
    print("|                4. Tabung                  |")
    print("|                5. Kerucut                 |")
    print("|         6. Limas (Tidak Tersedia)         |")
    print("|        7. Prisma (Tidak Tersedia)         |")
    print("|                0. Kembali                 |")
    print("|                                           |")
    print("---------------------------------------------")
    Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")

    if Q == "1":
        Bola()
    elif Q == "2":
        Balok()
    elif Q == "3":
        Kubus()
    elif Q == "4":
        Tabung()
    elif Q == "5":
        Kerucut()
    elif Q == "6":
        Limas()
    elif Q == "7":
        Prisma()
    elif Q == "0":
        menu()
    else:
        print("Opsi Tidak Tersedia!!")

    def Bola():
            print("---------------------------------------------")
            print("|                 1. Luas                   |")
            print("|                2. Volume                  |")
            print("---------------------------------------------")
            pilih = input("Masukan input berupa nomor: ")
            if pilih == "1":
                jari = float(input("Masukan Jari-Jari lingkaran: "))
                jumlah = 4 * 3.14 * jari * jari
                print(jumlah)
                clear()
            elif pilih == "2":
                jari = float(input("Masukan Jari-Jari lingkaran: "))
                jumlah = 4/3 * 3.14 * jari * jari
                print(jumlah)
                clear()
            else:
                print("Opsi Tidak Tersedia!!")
                clear()

    def Balok():
        print("---------------------------------------------")
        print("|                 1. Luas                   |")
        print("|                2. Volume                  |")
        print("---------------------------------------------")
        pilih = input("Masukan input berupa nomor: ")
        if pilih == "1":
            panjang = float(input("Masukan Panjang Balok: "))
            lebar = float(input("Masukan Lebar Balok: "))
            tinggi = float(input("Masukan Tinggi Balok: "))
            jumlah = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            print(jumlah)
            clear()
        elif pilih == "2":
            panjang = float(input("Masukan Panjang Balok: "))
            lebar = float(input("Masukan Lebar Balok: "))
            tinggi = float(input("Masukan Tinggi Balok: "))
            jumlah = panjang * lebar * tinggi
            print(jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia")
            clear()

    def Kubus():
        print("---------------------------------------------")
        print("|                 1. Luas                   |")
        print("|                2. Volume                  |")
        print("---------------------------------------------")
        pilih = input("Masukan input berupa nomor: ")
        if pilih == "1":
            sisi = float(input("Masukan Panjang Sisi Kubus: "))
            jumlah = 6 * sisi * sisi
            print(jumlah)
            clear()
        elif pilih == "2":
            panjang = float(input("Masukan Panjang Kubus: "))
            lebar = float(input("Masukan Lebar Kubus: "))
            tinggi = float(input("Masukan Tinggi Kubus: "))
            jumlah = panjang * lebar * tinggi
            print(jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia!!")
            clear() 

    def Tabung():
        print("---------------------------------------------")
        print("|                 1. Luas                   |")
        print("|                2. Volume                  |")
        print("---------------------------------------------")
        pilih = input("Masukan input berupa nomor: ")
        if pilih == "1":
            Jari = float(input("Masukan Jari Jari Tabung: "))
            tinggi = float(input("Masukan Tinggi Tabung: "))
            jumlah = 2 * 3.14 * Jari * ( Jari * tinggi )
            print(jumlah)
            clear()
        elif pilih == "2":
            Jari = float(input("Masukan Jari Jari Tabung: "))
            tinggi = float(input("Masukan Tinggi Tabung: "))
            jumlah = 3.14 * Jari * Jari * tinggi
            print(jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia!!")
            clear() 

    def Kerucut():
        print("---------------------------------------------")
        print("|                 1. Luas                   |")
        print("|                2. Volume                  |")
        print("---------------------------------------------")
        pilih = input("Masukan input berupa nomor: ")
        if pilih == "1":
            Jari = float(input("Masukan Jari Jari Kerucut: "))
            lukis = float(input("Masukan Garis Lukis Kerucut: "))
            jumlah = 3.14 * Jari * ( lukis + Jari )
            print(jumlah)
            clear()
        elif pilih == "2":
            Jari = float(input("Masukan Jari Jari Kerucut: "))
            tinggi = float(input("Masukan Tinggi Kerucut: "))
            jumlah = 1/3 * 3.14 * Jari * Jari * tinggi
            print(jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia!!")
            clear()

    def Limas():
        print("Maafkan Saya Di Karenakan Rumus Limas Terlalu Susah, Sehingga Membuat Bangun Ruang Prisma Tidak Tersedia")

    def Prisma():
        print("Maafkan Saya Di Karenakan Rumus Prisma Terlalu Susah, Sehingga Membuat Bangun Ruang Prisma Tidak Tersedia")


input("Pencet Enter untuk kembali ke menu....")
operating_system = sys.platform
if operating_system == 'win32':
    subprocess.run('cls', shell=True)
if operating_system == 'linux' or operating_system == 'darwin':
    subprocess.run('clear', shell=True)
menu()

