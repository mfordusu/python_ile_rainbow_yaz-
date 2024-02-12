from colorama import init, Fore
import time
import sys

def print_rainbow(text):
    init()  # Colorama'nın terminalde renkli çıktılar için başlatılması

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]  # Rainbow renkler listesi

    for i, char in enumerate(text):
        color = colors[i % len(colors)]  # Karakterin pozisyonuna bağlı olarak renk seçimi
        print(color + char, end='', flush=True)  # flush=True, her karakterin hemen yazdırılmasını sağlar
        time.sleep(0.1)  # Her karakter arasında bir gecikme ekler

    print()  # Yazdırma işlemi tamamlandığında bir satır atlatır

text = "deneme123 by user_xdd"
repeat_count = 10

for _ in range(repeat_count):
    print_rainbow(text)

# 7 saniye sonra programı kapat
time.sleep(7)
sys.exit()
