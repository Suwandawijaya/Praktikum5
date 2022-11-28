print("===================================================================")
print("Nama : Suwanda wijaya")
print("NIM : 312210028")
print("Kelas : TI.22.B1")
print("Mata Kuliah : Bahasa Pemrograman")
print("===================================================================")


data = {}
while True:
    a = input('\n(T)ambah data, (H)apus data, (U)bah data, (L)ihat data, (C)ari data,(K)eluar  ')
    if a=="t":
        print('tambah data mahasiswa')
        nama=input('masukan nama\t\t: ')
        nim=input('masukan NIM\t\t: ')
        nilaiTugas=int(input('masukan nilai tugas\t: '))
        nilaiUts=int(input('masukan nilai UTS\t: '))
        nilaiUas=int(input('masukan nilai UAS\t: '))
        nilaiakhir=(0.30*nilaiTugas)+(0.35*nilaiUts)+(0.35*nilaiUas)
        data[nama]=nim,nilaiTugas,nilaiUts,nilaiUas,nilaiakhir
        print('\ndata berhasil ditambahkan')

    elif a=="u":
        print('ubah data')
        nama=input('masukan nama: ')
        if nama in data.keys():
            nim=input('masukan NIM baru\t: ')
            nilaiTugas=int(input('masukan nilai tugas\t: '))
            nilaiUts=int(input('masukan nilai UTS\t: '))
            nilaiUas=int(input('masukan nilai UAS\t: '))
            nilaiakhir=(0.30*nilaiTugas)+(0.35*nilaiUts)+(0.35*nilaiUas)
            data[nama]=nim,nilaiTugas,nilaiUts,nilaiUas,nilaiakhir
            print('\ndata berhasil diubah')
        else:
            print('data tidak ditemukan')

    elif a=="h":
        print('hapus data')
        nama = input('masukan nama: ')
        if nama in data.keys():
            del data[nama]
            print('data berhasil dihapus')
        else:
            print('data tidak ditemukan')
        

    elif a=='c':
        print('cari data')
        nama = input('masukan nama: ')
        if nama in data.keys():
            print("\n                   DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiakhir)) 
            print("==============================================================")
        else:
            print('data tidak ditemukan')


    elif a=='l':
        if data.items():
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print('data tidak ditemukan')

    elif a=='k':
        print('======terimakasih=====')
        break
    else:
        print('mohon memasukan pilihan yang benar')