#! python3

import pyautogui
import sys
import time
import random
import string

# Fungsi untuk menampilkan pesan dengan 3 mode
def msg(_option_, _message_):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')

# Fungsi untuk keluar dari program
def ext():
    msg(1, 'Exiting...')
    sys.exit()

# Fungsi untuk membuka Firefox
def open_firefox():
    msg(1, 'Membuka Firefox...')
    _start_button_ = pyautogui.locateOnScreen(
        r'C:\Users\user\Documents\Tugas\Global\gmail-generator-master\source\images\start_button.png',
        confidence=0.8
    )
    if _start_button_:
        _location_ = pyautogui.center(_start_button_)
        pyautogui.click(_location_)
        msg(1, 'Menu mulai berhasil dibuka!')
    else:
        msg(3, 'Gagal membuka menu mulai!')
        ext()

    time.sleep(2)
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    msg(1, 'Firefox sekarang terbuka dan berjalan.')

# Fungsi untuk membuka halaman Gmail
def locate_gmail():
    time.sleep(3)
    msg(1, 'Membuka Gmail...')
    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('a')
    pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')
    time.sleep(6)
    msg(1, 'Mencari form...')
    pyautogui.press('tab')
    time.sleep(2)

    _gmail_ = pyautogui.locateOnScreen(
        r'C:\Users\user\Documents\Tugas\Global\gmail-generator-master\source\images\gmail_form.png',
        confidence=0.8
    )
    if _gmail_:
        formx, formy = pyautogui.center(_gmail_)
        pyautogui.click(formx, formy)
        msg(1, 'Form berhasil ditemukan.')
    else:
        msg(3, 'Gagal menemukan form.')
        ext()

# Fungsi untuk mengacak data kredensial
def randomize(_option_, _length_):
    if _length_ > 0:
        if _option_ == '-p':
            characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
        elif _option_ == '-l':
            characters = string.ascii_letters
        elif _option_ == '-n':
            characters = string.digits
        elif _option_ == '-m':  # Bulan
            return random.randint(1, 12)
        elif _option_ == '-d':  # Hari
            return random.randint(1, 28)
        elif _option_ == '-y':  # Tahun
            return random.randint(1950, 2000)
        else:
            characters = ''
        return ''.join(random.choice(characters) for _ in range(_length_))
    else:
        msg(3, 'Panjang yang valid tidak diberikan...')
        ext()

# Fungsi untuk menghasilkan informasi kredensial
def generate_info():
    msg(1, 'Menghasilkan kredensial...')

    # Nama depan dan belakang
    _first_name_ = randomize('-l', 7)
    pyautogui.typewrite(_first_name_)
    pyautogui.typewrite('\t')
    _last_name_ = randomize('-l', 8)
    pyautogui.typewrite(_last_name_)
    msg(2, f'Nama: {_first_name_} {_last_name_}')

    # Menekan tombol Next setelah Nama Depan dan Belakang
    pyautogui.press('tab')  # Pindah ke tombol Next
    pyautogui.press('enter')  # Tekan tombol Next
    msg(1, 'Menekan "Next" setelah mengisi Nama Depan dan Belakang.')
    time.sleep(3)  # Tunggu halaman berikutnya selesai dimuat

    pyautogui.press('tab')  # Pindah ke tombol Next
    # Mengisi Hari, Bulan, Tahun, Gender menggunakan Tab
    _day_ = randomize('-d', 1)
    pyautogui.typewrite(str(_day_))
    pyautogui.press('tab')  # Pindah ke bulan
    pyautogui.press('a')
    pyautogui.press('tab')  # Pindah ke tahun
    _year_ = randomize('-y', 1)
    pyautogui.typewrite(str(_year_))
    msg(2, f'Tanggal lahir: {_day_}/April/{_year_}')

    # Menekan tab 2x untuk memilih gender
    pyautogui.press('tab')  # Pindah ke dropdown gender
    pyautogui.press('enter')  # Buka dropdown
    gender_choice = random.choice(['w', 'p', 't'])  # Pilih gender secara acak
    pyautogui.press(gender_choice)
    msg(2, f'Pilih Gender: {gender_choice}')

    # Menekan Tab dua kali untuk pindah ke tombol selanjutnya
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.press('tab')  # Pindah ke tombol submit
    pyautogui.press('enter')  # Klik tombol Selanjutnya
    msg(1, 'Menekan "Next" setelah mengisi Tanggal Lahir dan Gender.')
    time.sleep(3)

    # Masuk ke halaman username gmail
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.press('down')  # Pindah ke tombol Selanjutnya
    pyautogui.press('down')  # Pindah ke tombol Selanjutnya

    _username_ = randomize('-l', 8)
    pyautogui.typewrite(_username_)
    msg(2, f'Username: {_username_}')
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.press('enter')  # Klik tombol Selanjutnya
    time.sleep(3)

    # Menghasilkan Password
    _password_ = randomize('-p', 8)  # Menghasilkan password dengan campuran karakter
    pyautogui.typewrite(_password_)
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.typewrite(_password_)  # Masukkan password sekali lagi
    msg(2, f'Password: {_password_}')
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.press('tab')  # Pindah ke tombol Selanjutnya
    pyautogui.press('enter')  # Pindah ke tombol Selanjutnya

# Fungsi utama
if __name__ == '__main__':
    open_firefox()
    locate_gmail()
    generate_info()
    msg(1, 'Selesai...')
    ext()
