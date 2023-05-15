data_anak_kost = [
    {'no_kamar' : 1, 'nama' : 'NATHANEL CORNELIUS LODAR', 'asal_daerah' : 'PAPUA', 'universitas' : 'UKDW', 'no_hp' : '082332686779'},
    {'no_kamar' : 2, 'nama' : 'VINA JHOPHINE SURUH', 'asal_daerah' : 'SULAWESI UTARA', 'universitas' : 'UKDW', 'no_hp' : '0898789887'},
    {'no_kamar' : 3, 'nama' : 'JENNY MARPAUNG', 'asal_daerah' : 'SUMATERA UTARA', 'universitas' : 'UST', 'no_hp' : '081234567890'},
    {'no_kamar' : 4, 'nama' : 'BRILIAN MADIUW', 'asal_daerah' : 'MALUKU', 'universitas' : 'UGM', 'no_hp' : '080987654321'},
    {'no_kamar' : 5, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 6, 'nama' : 'APRIZIAN SESILIA LODAR', 'asal_daerah' : 'NUSA TENGGARA TIMUR', 'universitas' : 'UIN', 'no_hp' : '081237052552'},
    {'no_kamar' : 7, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 8, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 9, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 10, 'nama' : 'AGUS', 'asal_daerah' : 'JAWA TIMUR', 'universitas' : 'UII', 'no_hp' : '081237052552'},
    {'no_kamar' : 11, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 12, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 13, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 14, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 15, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 16, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 17, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 18, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 19, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
    {'no_kamar' : 20, 'nama' : '', 'asal_daerah' : '', 'universitas' : '', 'no_hp' : ''},
]
def menu_satu(nama):
    indikator = 0
    banyak_orang = 0
    for panggil in data_anak_kost:
        if panggil['nama'] == nama:
            return True
        else:
            if len(panggil['nama']) > 0:
                indikator += 1
                banyak_orang += 1
            else:
                continue
    if indikator == banyak_orang:
        return False
def menu_dua(no):
    for panggil in data_anak_kost:
        if panggil['no_kamar'] == no:
            if len(panggil['nama']) > 0:
                return True
            else:
                return False
def menu_lima(no, nama, asal, univ, no_hp):
    for panggil in data_anak_kost:
        if panggil['no_kamar'] == no:
            panggil['nama'] = nama
            panggil['asal_daerah'] = asal
            panggil['universitas'] = univ
            panggil['no_hp'] = no_hp
def menu_tujuh(no):
    for panggil in data_anak_kost:
        if panggil['no_kamar'] == no:
            panggil['nama'] = ''
            panggil['asal_daerah'] = ''
            panggil['universitas'] = ''
            panggil['no_hp'] = ''
while True:
    print("Selamat datang di pengelolaan data anak kost")
    print('1. Mencari data dari nama.')
    print('2. Mencari data dari no kamar.')
    print('3. Mencari no hp dari nama.')
    print('4. Mencari no hp dari no kamar.')
    print('5. Menambahkan orang.')
    print('6. Memindahkan orang.')
    print('7. Menghapus data.')
    print('8. Melihat data sekarang.')
    print('0. exit')
    pilihan_menu = int(input("Pilih menu no: "))
    if pilihan_menu == 1:
        nama = input("Masukan nama yang mau dicari: ").upper()
        if menu_satu(nama) == False:
            print("Gak ada orangnya!")
        else:
            indikator = 0
            banyak_orang = 0
            for panggil in data_anak_kost:
                if panggil['nama'] == nama:
                    print(52*'=')
                    print(f'No kamar\t: {panggil["no_kamar"]}\nNama\t\t: {panggil["nama"]}\nAsal\t\t: {panggil["asal_daerah"]}\nUniversitas\t: {panggil["universitas"]}\nNo Handphone\t: {panggil["no_hp"]}')
                    print(52*'=')
                else:
                    if len(panggil['nama']) > 0:
                        indikator += 1
                        banyak_orang += 1
                    else:
                        continue
    elif pilihan_menu == 2:
        no = int(input("Masukan no kamar yang mau dicari: "))
        if menu_dua(no) == False:
            print("Kamar kosong!")
        else:
            for panggil in data_anak_kost:
                if panggil['no_kamar'] == no:
                    print(52*'=')
                    print(f'No kamar\t: {panggil["no_kamar"]}\nNama\t\t: {panggil["nama"]}\nAsal\t\t: {panggil["asal_daerah"]}\nUniversitas\t: {panggil["universitas"]}\nNo Handphine\t: {panggil["no_hp"]}')
                    print(52*'=')
    elif pilihan_menu == 3:
        nama = input("Masukan nama yang mau dicari: ").upper()
        if menu_satu(nama) != False:
            for panggil in data_anak_kost:
                if panggil['nama'] == nama:
                    print(f'No Hp dari {panggil["nama"]} adalah {panggil["no_hp"]}')
        else:
            print('Gak ada orangnya!')
    elif pilihan_menu == 4:
        no = int(input("Masukan no kamar yang mau diketahui no hpnya: "))
        if menu_dua(no) == True:
            for panggil in data_anak_kost:
                if panggil['no_kamar'] == no:
                    print(52*'=')
                    print(f'Kamar: "{no}"\nNama penghuni: {panggil["nama"]}\nNo HP: {panggil["no_hp"]}')
                    print(52*'=')
        else:
            print("Kamar Kosong!")
    elif pilihan_menu == 5:
        while True:
            no = int(input("Mau masuk ke kamar no berapa? "))
            if menu_dua(no) == True:
                print("Kamar ini sudah terisi!")
            else:
                break
        nama = input("Masukan nama lengkap: ").upper()
        asal = input("Masukan asal daerah: ").upper()
        univ = input("Jika berkuliah masukan nama UNIV jika tidak, ketik 'Tidak berkuliah': ").upper()
        no_hp = input("Masukan no handphone aktif/wa: ").upper()
        menu_lima(no, nama, asal, univ, no_hp)
    elif pilihan_menu == 6:
        nama = input("Masukan nama lengkap orang yang mau dipindahkan: ").upper()
        while True:
            no = int(input("Mau dipindahkan ke kamar no berapa? "))
            if menu_dua(no) == True:
                print(f'Kamar no {no} telah terisi')
            else:
                break
        asal = None
        univ = None
        no_hp = None
        no_kamar_sebelum = None
        for panggil in data_anak_kost:
            if panggil['nama'] == nama:
                asal = panggil['asal_daerah']
                univ = panggil['universitas']
                no_hp = panggil['no_hp']
                no_kamar_sebelum = panggil['no_kamar']
        menu_tujuh(no_kamar_sebelum)
        menu_lima(no, nama, asal, univ, no_hp)
    elif pilihan_menu == 7:
        no = int(input('Masukan no kamar yang ingin datanya dihapus: '))
        if menu_dua(no) == False:
            print('Kamar ini memang udah kosong!')
        else:
            menu_tujuh(no, nama, asal, univ, no_hp)
            print(f'data dari kamar nomor {no} berhasil di hapus')
    elif pilihan_menu == 8:
        for panggil in data_anak_kost:
            print(52*'=')
            print(f'No kamar\t: {panggil["no_kamar"]}\nNama\t\t: {panggil["nama"]}')
            print(f'Asal\t\t: {panggil["asal_daerah"]}\nUniversitas\t: {panggil["universitas"]}\nNo Handphone\t: {panggil["no_hp"]}')
            print(52*'=')
    elif pilihan_menu == 0:
        print('GOOD BYE!')
        break
    else:
        print('Pilihan tidak tersedia!')