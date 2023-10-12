import subprocess
import sys

def menu1():
    print(50*"=")
    print("Menghitung Bangun Ruang")
    print("1. Bola")
    print("2. Balok")
    print("3. Kubus")
    print("4. Tabung")
    print("5. Kerucut")

    pilih()

def clear():
    input("Pencet Enter untuk kembali ke menu....")
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)
    menu1()

def Bola():
    print("1. Luas")
    print("2. Volume")
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
        print("Input tidak tersedia")
        clear()

def Balok():
    print("1. Luas")
    print("2. Volume")
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
        print("Input tidak tersedia")
        clear()

def kubus():
    print("1. Luas")
    print("2. Volume")
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
        print("Input tidak tersedia")
        clear()

def tabung():
    print("1. Luas")
    print("2. Volume")
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
        print("Input tidak tersedia")
        clear()

def kerucut():
    print("1. Luas")
    print("2. Volume")
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
        print("Input tidak tersedia")
        clear()

def pilih():
    pilih = input("Masukan input berupa nomor: ")
    if pilih == "1":
        Bola()
    elif pilih == "2":
        Balok()
    elif pilih == "3":
        kubus()
    elif pilih == "4":
        tabung()
    elif pilih == "5":
        kerucut()
    else:
        print("Input tidak tersedia")
        clear()

clear()
menu1()