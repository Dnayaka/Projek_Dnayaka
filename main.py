##############################################
#         SerbaGuna With Python              #
##############################################
import subprocess
import sys
import pyfiglet
import os
from plyer import notification
import time
def clear():
    input("Pencet Enter untuk kembali ke menu....")
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)
    menu()

def menu():
    print("""\033[96m
 ########::'##::: ##::::'###::::'##:::'##::::'###::::'##:::'##::::'###::::
 ##.... ##: ###:: ##:::'## ##:::. ##:'##::::'## ##::: ##::'##::::'## ##:::
 ##:::: ##: ####: ##::'##:. ##:::. ####::::'##:. ##:: ##:'##::::'##:. ##::
 ##:::: ##: ## ## ##:'##:::. ##:::. ##::::'##:::. ##: #####::::'##:::. ##:
 ##:::: ##: ##. ####: #########:::: ##:::: #########: ##. ##::: #########:
 ##:::: ##: ##:. ###: ##.... ##:::: ##:::: ##.... ##: ##:. ##:: ##.... ##:
 ########:: ##::. ##: ##:::: ##:::: ##:::: ##:::: ##: ##::. ##: ##:::: ##:
........:::..::::..::..:::::..:::::. .:::::..:::::..::..::::..::..:::::..::
       :'######:::'#######::'########::'####:'##::: ##::'######:::
       '##... ##:'##.... ##: ##.... ##:. ##:: ###:: ##:'##... ##::
        ##:::..:: ##:::: ##: ##:::: ##:: ##:: ####: ##: ##:::..:::
        ##::::::: ##:::: ##: ##:::: ##:: ##:: ## ## ##: ##::'####:
        ##::::::: ##:::: ##: ##:::: ##:: ##:: ##. ####: ##::: ##::
        ##::: ##: ##:::: ##: ##:::: ##:: ##:: ##:. ###: ##::: ##::
       . ######::. #######:: ########::'####: ##::. ##:. ######:::
       :......::::.......:::........:::....::..::::..:::......::::

           ╔═══════════════════════════════════╗
           ║         ♡◇♤     𝙈𝙀𝙉𝙐      ♤◇●     ║
           ╚═══════════════════════════════════╝
           ╔═══════════════════════════════════╗
           ║    1. Menghitung Bangun Ruang     ║
           ║    2. Menghitung Bangun Datar     ║
           ║            3. Font 3D             ║
           ║            4. Catatan             ║
           ║                                   ║
           ║           DNayaka Script          ║
           ╚═══════════════════════════════════╝

\n""")
    Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")

    if Q == "1":
        Bangun_Ruang()
    if Q == "2":
        Bangun_Datar()
    if Q == "3":
        Font_3D()
    if Q == "4":
        notepad()
    else:
        print("Opsi Tidak Tersedia!!")
        clear()

def notepad():
    def one():
            with open("new.txt", 'r')as file:
                P = file.read()
                print(P)
                file.close()
            input("Lanjut══> ")
            notepad()

    def two():
        P = input("Masukan Kata══> ")
        with open("new.txt", 'a')as file:
           file.write(P)
           file.close()
        input("Lanjut══> ")
        notepad()

    def three():
        P1  = input("Masukan Kata Lama══> ")
        P2  = input("Masukan Kata Baru══> ")
        with open("new.txt", 'r')as file:
           data = file.read()
           file.close()
        data = data.replace(P1, P2)
        with open("new.txt", 'w')as file:
           file.write(data)
           file.close()
        input("Lanjut══> ")
        notepad()

    def menu():
        print("""

           ╔╦═════════════════════════════════╦╗
           ║║            Notepad++            ║║
           ║║═════════════════════════════════║║
           ║║        1. Lihat Catatan         ║║
           ║║      2. Memasukan Catatan       ║║
           ║║        3. Mengganti Kata        ║║
           ╚╩═════════════════════════════════╩╝

    """)
    menu()
    Q = input("Masukan Input══>: ")
    if Q == "1":
        one()
    elif Q == "2":
        two()
    elif Q == "3":
        three()
    else:
        input("[>]Command Tidak Tersedia")
        notepad()

def Font_3D():
    kata = input("Masukan Kata ╚════> ")
    result = pyfiglet.figlet_format(kata, font='banner3-D')
    print(result)
    clear()

def Bangun_Ruang():
    def Bola():
            print("""
           ╔═══════════════════════╗
           ╚═══════════════════════╝
           ╔═══════════════════════╗
           ║        1. Luas        ║
           ║       2. Volume       ║
           ╚═══════════════════════╝

""")
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
        print("""
           ╔═══════════════════════╗
           ╚═══════════════════════╝
           ╔═══════════════════════╗
           ║        1. Luas        ║
           ║       2. Volume       ║
           ╚═══════════════════════╝

""")
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
        print("""
           ╔═══════════════════════╗
           ╚═══════════════════════╝
           ╔═══════════════════════╗
           ║        1. Luas        ║
           ║       2. Volume       ║
           ╚═══════════════════════╝

""")
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
        print("""
           ╔═══════════════════════╗
           ╚═══════════════════════╝
           ╔═══════════════════════╗
           ║        1. Luas        ║
           ║       2. Volume       ║
           ╚═══════════════════════╝

""")
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
        print("""
           ╔═══════════════════════╗
           ╚═══════════════════════╝
           ╔═══════════════════════╗
           ║        1. Luas        ║
           ║       2. Volume       ║
           ╚═══════════════════════╝

""")
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
    
    print("""
           ╔═══════════════════════════════════════════╗
           ║           ▄︻デɮǟռɢʊռ_ʀʊǟռɢ══━一          ║
           ║          Made Original By Dnayaka                ║
           ╚═══════════════════════════════════════════╝
           ╔═══════════════════════════════════════════╗
           ║                 1. Bola                   ║
           ║                 2. Balok                  ║
           ║                 3. Kubus                  ║
           ║                4. Tabung                  ║
           ║                5. Kerucut                 ║
           ║         6. Limas (Tidak Tersedia)         ║
           ║        7. Prisma (Tidak Tersedia)         ║
           ║                0. Kembali                 ║
           ║                                           ║
           ╚═══════════════════════════════════════════╝""")
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
        clear()
        menu()
    else:
        print("Opsi Tidak Tersedia!!")

def Bangun_Datar():
    def Lingkaran():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":
            Jari = float(input("Masukan Jari Jari: "))
            jumlah = 3.14 * Jari * Jari
            print("Hasil: ",jumlah)
            clear()
        elif Q == "2":
            Jari = float(input("Masukan Jari Jari: "))
            jumlah = 2 * 3.14 * Jari * Jari
            print("Hasil: ", jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia!!")
            clear()

    def Persegi_Panjang():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":
            Panjang = float(input("Masukan Panjang: "))
            Lebar = float(input("Masukan Lebar: "))
            jumlah = Panjang * Lebar
            print("Hasil: ",jumlah)
            clear()
        elif Q == "2":
            Panjang = float(input("Masukan Panjang: "))
            Lebar = float(input("Masukan Lebar: "))
            jumlah = ( 2 * Panjang ) + ( 2 * Lebar )
            print("Hasil: ", jumlah)
        else:
            print("Input Tidak Tersedia!!")
    
    def Persegi():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":
            Sisi = float(input("Masukan Panjang Sisi: "))
            jumlah = Sisi * Sisi
            print("Hasil: ",jumlah)
        elif Q == "2":
            Sisi = float(input("Masukan Panjang Sisi: "))
            jumlah = 4 * Sisi
            print("Hasil: ", jumlah)
        else:
            print("Opsi Tidak Tersedia!!")
            clear

    def Segitiga():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":    
            Alas = float(input("Masukan Panjang Alas: "))
            Tinggi = float(input("Masukan Panjang Tinggi: "))
            jumlah = 1/2 * Alas * Tinggi
        if Q == "2":
            Sisi1 = float(input("Masukan Sisi Pertama: "))
            Sisi2 = float(input("Masukan Sisi Kedua: "))
            Sisi3 = float(input("Masukan Sisi Ketiga: "))
            jumlah = Sisi1 + Sisi2 + Sisi3
            print("Hasil: ", jumlah)
        else:
            print("Opsi Tidak Tersedia!!")
            clear()
        print("Hasil: ", jumlah)
    
    def Jajar_Genjang():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":
            Alas = float(input("Masukan Alas: "))
            Tinggi = float(input("Masukan Tinggi: "))
            jumlah = Alas * Tinggi
            print("Hasil: ",jumlah)
        elif Q == "2":
            Sisi1 =  float(input("Masukan Sisi Pertama: "))
            Sisi2 = float (input("Masukan Sisi Kedua: "))
            Sisi3 = float(input("Masukan Sisi Ketiga: "))
            Sisi4 = float(input("Masukan Sisi Keempat: "))
            jumlah = Sisi1 + Sisi2 + Sisi3 + Sisi4
        else:
            print("Opsi Tidak Tersedia!!")
            clear()

    def Belah_Ketupat():
        print("╔═══════════════════════════════════════════╗")
        print("║              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                 ║")
        print("║          Made Original By Dnayaka         ║")
        print("╚═══════════════════════════════════════════╝")
        print("╔═══════════════════════════════════════════╗")
        print("║                1. Luas                    ║")
        print("║               2. Keliling                 ║")
        print("╚═══════════════════════════════════════════╝")
        Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
        if Q == "1":
            D1 = float(input("Masukan Diagonal Satu: "))
            D2 = float(input("Masukan Diagonal Kedua:"))
            jumlah = 1/2 * D1 * D2
            print("Hasil: ", jumlah)
            clear()
        elif Q == "2":
            S1 = float(input("Masukan Sisi Pertama: "))
            S2 = float(input("Masukan Sisi Kedua: "))
            S3 = float(input("Masukan Sisi Ketiga: "))
            S4 = float(input("Masukan Sisi Keempat: "))
            jumlah = S1 * S2 * S3 * S4
            print("Hasil: ", jumlah)
            clear()
        else:
            print("Opsi Tidak Tersedia!!")

    print("---------------------------------------------")
    print("|              𝕭𝖆𝖓𝖌𝖚𝖓 𝕯𝖆𝖙𝖆𝖗                |")
    print("|          Made Original By Dnayaka         |")
    print("--------------------------------------------|")
    print("|                                           |")
    print("|               1. Lingkaran                |")
    print("|             2. Persegi Panjang            |")
    print("|                3. Persegi                 |")
    print("|               4. Segitiga                 |")
    print("|             5. Jajar Genjang              |")
    print("|             6. Belah Ketupat              |")
    print("|                0. Kembali                 |")
    print("|                                           |")
    print("---------------------------------------------")
    Q = input("Pilih Opsi Sesuai Nomor Yang Ada Di Atas: ")
    if Q == "1":
        Lingkaran()
    elif Q == "2":
        Persegi_Panjang()
    elif Q == "3":
        Persegi()
    elif Q == "4":
        Segitiga()
    elif Q == "5":
        Jajar_Genjang()
    elif Q == "6":
        Belah_Ketupat()
    elif Q == "0":
        clear()
        menu()
    else:
        print("Opsi Tidak Tersedia!!")
        clear()



def username():
    User = input("\033[96mMasukan Username: ")
    if User == "DSilent":
        print("\033[96mUsername Benar!")
        password()
    elif User == "Admin":
        input("\033[96mMode Admin Activated")
        operating_system = sys.platform
        if operating_system == 'win32':
            input("Program Not Supported!!")
            username()
        if operating_system == 'linux' or operating_system == 'darwin':
            subprocess.run('nano main.py', shell=True)
    else:
        print("\033[96mUsername Salah!")
        username()

def password():
    Password = input("Masukan Password: ")
    if Password == "01122011":
        print("\033[96mPassword Benar!")
        clear()
    else:
        print("\033[96mPassword Salah!")
        password()


username()
