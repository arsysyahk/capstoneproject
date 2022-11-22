
#daftar mobil
def daftarmobil():
    ListMobil = { '1': {'id' : '1','brand mobil' : 'Honda','tipe mobil' : 'HRV','tahun' : '2015','sewa' : '120000'},
		'2': {'id' : '2','brand mobil' : 'TOYOTA','tipe mobil' : 'Avanza','tahun' : '2010','sewa' : '100000'},
        '3' : {'id' : '3','brand mobil' : 'daihatsu','tipe mobil' : 'xenia','tahun' : '2006','sewa' : '80000'}}
    print(ListMobil)
  

# tambah mobil
def tambahmobil() :
    ListMobil = { '1': {'id' : '1','brand mobil' : 'Honda','tipe mobil' : 'HRV','tahun' : '2015','sewa' : '120000'},
		'2': {'id' : '2','brand mobil' : 'TOYOTA','tipe mobil' : 'Avanza','tahun' : '2010','sewa' : '100000'},
        '3' : {'id' : '3','brand mobil' : 'daihatsu','tipe mobil' : 'xenia','tahun' : '2006','sewa' : '80000'}}
    
    ListMobil['4'] = input ('masukan id, brand mobil, tipe mobil, tahun, dan sewa : ')
    print(ListMobil)

# del
    def hapusmobil():
        del ListMobil['4']
    hapusmobil()

    

# hapus mobil
def hapusmobil() :
    print('HAPUS MOBIL')
    

# ubah mobil
def ubahmobil() :
    print('ubah mobil')



# menu
def menu():
    print("[1] Lihat Mobil")
    print("[2] tambah mobil")
    print("[3] ubah mobil")
    print("[4] Hapus Mobil")
    print("[0] exit program")

menu()
option = int(input("enter yout option: "))

while option !=0:
    if option == 1:
        daftarmobil()
    elif option == 2:
        tambahmobil()
    elif option == 3:
        ubahmobil()
    elif option == 4:
        hapusmobil()
    else:
        print("invalid")
    
    print()
    menu()
    option = int(input("enter your option :"))
print ("thanks for using")

