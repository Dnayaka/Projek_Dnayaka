import subprocess
import sys

def clear():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)

def kasir():
    print("Selamat Datang Di Mesin Kasir Sederhana")
    print(50*"-")
    print("1. Kroket")
    print("2. Srundeng")
    print("3. Ayam Katsu")

    choice = input("Masukan Pesanan Anda: ")
    jumlah = float(input("Jumlah: "))
    kroket = float(input("Harga Kroket Saat Ini: "))
    Hasil = jumlah * kroket
    if choice == "1":
        print("Harga: ", Hasil)
    elif choice == "2":
        print("Harga: ", Hasil)
    elif choice == "3":
        print("Harga: ", Hasil)
    p()

def p():
    p = input("Apakah Ada Pesanan Lain?(Y/N): ")
    if p == "N":
        print("Terimakasih sudah membeli :)")
        print(50*"-")
    if p == "Y":
        clear()
        kasir()

clear() 
kasir()