import time,os,sys
from time import sleep
import curses
from curses import KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT

m = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;34m'
u = '\033[1;35m'
c = '\033[1;36m'
p = '\033[1;37m'

def loading():
    for i in "\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/":
        print(f"\r Loading: {i}",end='',flush=True)
        time.sleep(0.1)

def main():
    print(f"{p}")
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Figlet...")
    time.sleep(3)
    os.system("pkg install figlet")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Tetris...")
    time.sleep(3)
    os.system("pkg install bastet")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Pacman...")
    time.sleep(3)
    os.system("pkg install pacman4console")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!]{k} Installing Moon-Buggy...")
    time.sleep(3)
    os.system("pkg install moon-buggy")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Space Invaders...")
    time.sleep(3)
    os.system("pkg install ninvaders")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Snake...")
    time.sleep(3)
    os.system("pkg install git && git clone https://github.com/TU4ND3VIL/Game-Termux")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Greed...")
    time.sleep(3)
    os.system("pkg install greed")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Hangman...")
    time.sleep(3)
    os.system("pkg install git && git clone https://github.com/KokoEmwe/Hangman")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing 2048...")
    time.sleep(3)
    os.system("pkg install git -y && pkg install wget -y && pkg install clang -y && wget https://raw.githubusercontent.com/mevdschee/2048.c/master/2048.c && sleep 2 && gcc -o 2048 2048.c")
    time.sleep(1)
    os.system("clear")
    os.system("figlet [!]NOTE")
    print(f" {p}[!] {m}Mohon jangan tekan ctrl + Z sebelum installasi selesai")
    print(f" {p}[!] {m}Please do not ctrl + Z while installation")
    time.sleep(3)
    print(f" {p}[!] {k}Installing Sudoku...")
    time.sleep(3)
    os.system("pkg install nudoku")
    time.sleep(1)
    os.system("clear")
    print(f"{c}")
    os.system("clear")
    os.system("figlet GAMES")
    print(f" {p}[#]==============================================[#]")
    print(f"  {p}|     Author : {b}Koko Emwe                          {p}|")
    print(f"  {p}|     Youtube: {m}Koko Emwe                          {p}|")
    print(f"  {p}|     Github : {k}https://github.com/KokoEmwe        {p}|")
    print(f" {p}[#]==============================================[#]")
    print("")
    print(f" {p}<----------[{c}Menu{p}]---------->")
    print(f" {p}[01] {k}Tetris              {p}[{h}WORK{p}]")
    print(f" {p}[02] {k}Pacman              {p}[{h}WORK{p}]")
    print(f" {p}[03] {k}Moon-Buggy          {p}[{h}WORK{p}]")
    print(f" {p}[04] {k}Space Invaders      {p}[{h}WORK{p}]")
    print(f" {p}[05] {k}Snake               {p}[{h}WORK{p}]")
    print(f" {p}[06] {k}Greed               {p}[{h}WORK{p}]")
    print(f" {p}[07] {k}NetHack             {p}[{h}WORK{p}]")
    print(f" {p}[08] {k}Hangman             {p}[{h}WORK{p}]")
    print(f" {p}[09] {k}2048                {p}[{h}WORK{p}]")
    print(f" {p}[10] {k}Sudoku              {p}[{h}WORK{p}]")
    print(f" {p}[88] {u}Info")
    print(f" {p}[99] {b}Enable Arrow")
    print(f" {p}[00] {c}Exit")
    print("")
    print(f" {p}[•] {k}Masukan pilihan anda")
    inp = input(f" {p}<•> {h}")
    if(inp=="1"):
      loading()
      os.system("clear")
      os.system("bastet")
    elif(inp=="2"):
      loading()
      os.system("clear")
      os.system("pacman")
    elif(inp=="3"):
      loading()
      os.system("clear")
      os.system("moon-buggy")
    elif(inp=="4"):
      loading()
      os.system("clear")
      os.system("nInvaders")
    elif(inp=="5"):
      loading()
      os.system("clear")
      os.system("cd Game-Termux")
      os.system("python2 ular.py")
    elif(inp=="6"):
      loading()
      os.system("clear")
      os.system("greed")
    elif(inp=="7"):
      loading()
      os.system("clear")
      os.system("nethack")
    elif(inp=="8"):
      loading()
      os.system("clear")
      os.system("cd hangman")
      os.system("python hangman.py")
    elif(inp=="9"):
      loading()
      os.system("clear")
      os.system("./2048")
    elif(inp=="10"):
      loading()
      os.system("clear")
      os.system("nudoku")
    elif(inp=="88"):
      loading()
      os.system("clear")
      info()
    elif(inp=="99"):
      loading()
      os.system("clear")
      key()
    elif(inp=="00"):
      loading()
      print(f" {p}[!] {h}Thanks for using my Script :)")
      os.system("clear")
      os.system("exit")
    else:
      time.sleep(1)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      main()










if __name__=="__main__":
    main()
