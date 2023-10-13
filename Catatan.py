from colorama import init, Fore, Back, Style
import subprocess
import sys

init()

error_message = "\033[31m!!Error!!\033[32m"

def menu():
    print("\033[32m-----------------------------------------")
    print("|  1. Masukan Catatan                   |")
    print("|  2. Lihat Catatan                     |")
    print("|  3. Hapus Kata Pada Baris Di Catatan  |")
    print("|  4. Keluar")
    print("|          Made By Dnayaka              |")
    print("-----------------------------------------")
    pilih = input("Masukan Nomor Yang Sesuai: ")
    if pilih ==  "1":
        with open("Catatan.txt", "a") as file:
            p = input("Masukan Kata: ")
            file.write(p)
        clear()
    elif pilih == "2":
        with open("Catatan.txt", "r") as file:
            p = file.readlines()
            print(p)
        clear()
    elif pilih == "3":
        kata_dihapus = input("Masukan Kata: ")
        with open("Catatan.txt", 'r') as file:
            isi_file = file.read()
        for kata in kata_dihapus:
            isi_file = isi_file.replace(kata, '')
        with open("Catatan.txt", 'w') as file:
            file.write(isi_file)
        clear()
    elif pilih == "4":
        sys.exit()
    else:
        print(error_message)
        clear()
            
            


def clear():
    input("Pencet Enter untuk kembali ke menu....")
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)
    menu()



clear()
menu()
