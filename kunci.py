import os

os.system('clear')
m = '\033[1;32m'
c = '\033[3;31m'
print(m)
os.system('figlet -f script " Robot Pace Usa"')
print('\r')
os.system('printf "\033[3;31m"')

# Langsung menggunakan wordlist.txt sebagai input
aaa = 'wordlist.txt'

os.system('clear')
print(c)
os.system('figlet -f script "  Robot Pace Usa"')
os.system('printf "\033[3;32m"')
print('By : Developer Pace Usa')
print('-'*29)

# Membuka file wordlist.txt dan menambahkan isinya ke set aa
with open(aaa, 'r') as file:
    aa = set(file.read().splitlines())

oio = set([])

kk = 1
while True:
    b = input('Entre {} : '.format(kk))
    if b == 'save':
        print('\033[3;33m')
        # Tidak perlu menutup file lagi karena sudah tidak menulis ke file wordlist.txt
        os.system('printf "\033[3;33m"')
        print('-'*60)
        print('>> {} Passwords in ---> {} '.format(len(aa), aaa))
        print('-'*60)
        break

    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio:
            oio.add(i)
            # Tambahkan logika yang diperlukan untuk memproses input pengguna jika diperlukan
            # ...

        c = b + i
        d = i + b
        if len(c) >= 6:
            with open(aaa, 'a') as file:
                file.write(c + '\n')
        if c != d and len(d) >= 6:
            with open(aaa, 'a') as file:
                file.write(d + '\n')

    kk += 1
    print('-'*40)
