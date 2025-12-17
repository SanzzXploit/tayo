import os
import time

tayo = r"""
        ____
       |   TAYO AUTO XSS SCAN  |
    _|____|_
   |   |   (•‿•)  Let's Go!!!     |  |
  (|   |__|  |)
   |____|
        O                      O
"""

def run(cmd):
    print(f"\n[+] {cmd}")
    os.system(cmd)

def loading():
    for i in range(3):
        os.system("clear")
        print(tayo)
        print("Loading" + "." * (i+1))
        time.sleep(0.7)

os.system("clear")
print(tayo)
print("[*] Starting auto install + auto scan...\n")
time.sleep(1)
loading()

print("[1] Installing ParamSpider...")
run("pip install paramspider")

print("[2] Installing GXSS...")
run("go install github.com/KathanP19/Gxss@latest")
run("mv ~/go/bin/Gxss /usr/local/bin/ 2>/dev/null")

print("[3] Installing DalFox...")
run("go install github.com/hahwul/dalfox/v2@latest")
run("mv ~/go/bin/dalfox /usr/local/bin/ 2>/dev/null")

print("[4] Installing Nuclei...")
run("apt install nuclei -y || sudo apt install nuclei -y")

os.system("clear")
print(tayo)
print("✔ Semua tools berhasil di-install!\n")

target = input("Masukkan domain target (contoh: example.com): ")

print("\n====================================")
print(f"[ SCANNING ] Target: {target}")
print("====================================")



print("\n[1] Running ParamSpider...")
run(f"paramspider --domain {target} --output paramspider_{target}.txt")

print("\n[2] Filtering with GXSS...")
run(f"cat paramspider_{target}.txt | Gxss -p Xss | tee gxss_{target}.txt")

print("\n[3] Running DalFox...")
run(f"dalfox file gxss_{target}.txt --only-poc --silence --no-spinner --output dalfox_{target}.txt")

print("\n[4] Running Nuclei XSS templates...")
run(f"nuclei -t xss/ -l gxss_{target}.txt -o nuclei_{target}.txt")

os.system("clear")
print(tayo)
print("SCAN SELESAI!\n")

print("Hasil tersimpan di:")
print(f" - paramspider_{target}.txt")
print(f" - gxss_{target}.txt")
print(f" - dalfox_{target}.txt")
print(f" - nuclei_{target}.txt")
print("\nSiap lanjutkan hunting 🔥")