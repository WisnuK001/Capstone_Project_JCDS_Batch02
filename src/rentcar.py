from tabulate import tabulate
import os
import pyinputplus as pyi

pathunitdetail = "src/1.dictunitdetail.csv"

def clearscreen():
    #untuk membersihkan layar tampilan
    # untuk pengguna windows
    if os.name == 'nt':
        os.system('cls')
    # untuk pengguna Mac or Linux
    else:
        os.system('clear')

def show(carDict):
    #menampilkan menu tampilan
    while True:
        prompt = '''
        
=============== ISTIMEWA TRANSPORT ===============
================= Data inventory =================

Data inventory Menu
1. Show inventory
2. Show by code
3. Back to main menu
'''
        print(prompt)
        list = pyi.inputInt('masukkan opsi: ') # user memilih submenu 
        clearscreen()
        if list == 1:
            showsub(carDict) # menampilkan seluruh data seutuhnya
        elif list == 2:
            showbycode(carDict) # menampilkan data tertentu dengan menggunakan code sebagai primary key
        elif list == 3:
            confirmmain= pyi.inputYesNo('Back to main menu ?: ') # konfirmasi user untuk kembali ke menu awal 
            if confirmmain == 'yes':
                clearscreen()
                break
        else:
            clearscreen()
            print('Opsi tidak tersedia')


def showsub(carDict):
    while True:
        if len(carDict) >= 1: # memastikan bahwa tersedia data untuk ditampilkan
            header = carDict['key']
            data = list(carDict.values())[1:]
            print(tabulate(data, header, tablefmt='pretty'))
            break
        else: #  Kondisiila data belum tersedia
            print('Maaf data belum tersedia')
            break

def showbycode(carDict):
    """function to display specific data with a primary key input by the user 

    Args:
        carDict (Dictionary): Inventory Database
    """    
    showsub(carDict)
    while True:
        header = carDict['key']
        data = False
        codevalue = []
        codeinput = pyi.inputStr("masukkan code : ").upper() # user memasukan code sebagai primary key
        for key, val in carDict.items():
            if codeinput.upper() == carDict[key][1].upper():
                codevalue.append(val)
                data = True
        if not data:
            print("\n\n\nMaaf data tidak tersedia") # kondisi apabila code yang dimasukkan tidak ada dalam database
        else:
            os.system('cls')
            print(f'\n{codeinput.upper()} data: \n')
            print(tabulate(codevalue, headers=header, tablefmt="pretty")) # menampilkan data dengan input dari user
        break




def add(carDict):
    while True:
        prompt = '''
=============== ISTIMEWA TRANSPORT ===============
================ Add New inventory ================

1. Add new item
2. back to main menu
'''
        print(prompt)
        submenuadd = pyi.inputInt('masukkan pilihan: ')
        clearscreen()
        if submenuadd == 1:
            adddata(carDict)
        elif submenuadd == 2:
            confirmout= pyi.inputYesNo('Back to main menu ?: ')
            if confirmout == 'yes':
                clearscreen()
                break
        else:
            clearscreen()
            print('Opsi tidak tersedia')


def adddata(carDict):
    os.system('cls')
    while True:
        newdata = pyi.inputChoice(
            prompt='ingin menambahkan data baru ?(y/n): ', choices=['y', 'n']) # konfirmasi penambahan data
        if newdata == 'y': # user menambahkan data
            No = len(carDict)
            code = input("masukkan code unit baru:").upper()
            if code in carDict: # pengecekan code untuk menghindari duplikasi
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n') # menampilkan data pada code yang sudah digunakan
                print("Maaf code sudah digunakan") 
            else: # code disetujui karena belum ada dalam database 
                #user memasukan informasi yang diperlukan
                Unitinfo = pyi.inputStr("masukkan nama unit baru(co: calya): ").capitalize()
                transmition = pyi.inputStr("masukkan jenis transmition (at/mt): ").upper()
                Merk = pyi.inputStr("masukkan nama merk(co: toyota): ").capitalize()
                Color = pyi.inputStr("masukkan warna unit(co: silver): ").capitalize()
                Year = pyi.inputInt("masukkan tahun pembuatan(co: 2021): ")
                Plate = pyi.inputStr("masukkan plat nomer(co: AB4511RD): ").upper()
                Fuel = pyi.inputStr("masukkan bahan bakar unit(co: pertalite): ").capitalize()
                Owner = pyi.inputStr("masukkan nama pemilik(co: Aditya): ").capitalize()
                saving = pyi.inputStr('Simpan data yang baru ? (y/n): ')
                if saving == 'y': # konfirmasi penyimpanan data
                    clearscreen()
                    carDict.update({f'{code}': [No, code, Unitinfo, transmition, Merk, Color, Year, Plate, Fuel,Owner]})
                    print('Data sudah berhasil di input') # data berhasil ditambahkan 
                    showsub(carDict) # menampilkan data setelah penambahan data berhasil
                elif saving == "n": # kondisi apabila user tidak memberi penambahan data
                    break 
        else:
            break
        return carDict # mengembalikan perubahan data 
    os.system('cls')

def update(carDict):
    while True:
        prompt = '''
=============== ISTIMEWA TRANSPORT ===============
=================== Update data ===================

1. Update / edit data
2. Update by column
3. back to main menu
'''
        print(prompt)
        subupdate = pyi.inputInt('masukkan pilihan: ')
        clearscreen()
        if subupdate == 1:
            updatedata(carDict) # update/edit data secara menyeluruh
        elif subupdate == 2:
            updatedatabycolumn(carDict) #update/edit data berdasarkan kolom tertentu
        elif subupdate == 3:
            confirmmain= pyi.inputYesNo('Back to main menu ?: ') # konfirmasi user kembali ke menu utama
            if confirmmain == 'yes':
                clearscreen()
                break
        else:
            os.system('cls')
            print('Opsi tidak tersedia')

def updatedata(carDict):
    
    os.system('cls')
    while True:
        os.system('cls')
        updatingdata = pyi.inputChoice(prompt='ingin mengubah data tertentu ?(y/n): ', choices=['y', 'n']) # konfirmasi user untuk edit data
        if updatingdata == 'y':
            showsub(carDict)
            code = pyi.inputStr("masukkan code data yang ingin di update:").upper() # memasukan primary key untuk menentukan data yang akan di edit
            if code in carDict: # memastikan code yang diinputkan ada dalam databse
                clearscreen()
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n') # menammpilkan data yang ingin di edit
                continueupdating = pyi.inputChoice(prompt='Apakah data ini ingin di update ?(y/n): ', choices=['y', 'n'])
                if continueupdating == 'y':
                    No = carDict[code][0]
                    #memastikan untuk code akan menggunakan code yang lama atau diganti
                    confirmupdatecode= pyi.inputChoice(prompt='Ganti code atau tetap gunakan code yang sama? (ganti/tetap): ', choices=['ganti', 'tetap']).lower()
                    if confirmupdatecode == 'ganti':
                        codebaru = pyi.inputStr("[Code] Ganti dengan code yang baru:").upper()
                        if  codebaru in carDict.keys():
                            clearscreen()
                            print('Maaf Code sudah digunakkan')
                            break
                        elif codebaru not in carDict.keys():
                            carDict[code][1] = codebaru
                            print(carDict)
                    unitinfo    = pyi.inputStr('[Unit info] Silahkan ganti dengan nama yang baru: ',).title()
                    carDict[code][2] : unitinfo
                    Transmition = pyi.inputStr('[Transmition] Silahkan ganti jenis transmition (at/mt): ',).upper()
                    carDict[code][3] : Transmition
                    Merk        = pyi.inputStr('[Merk] Silahkan masukkan Merk unit: ',).title()
                    carDict[code][4] : Merk
                    Color       = pyi.inputStr('[Color] Silahkan masukkan warna terbaru: ',).title()
                    carDict[code][5] : Color
                    Year        = pyi.inputInt('[Year] Silahkan masukkan tahun produksi: ',) 
                    carDict[code][6] : Year
                    Plate       = pyi.inputStr('[Plate] Silahkan ganti dengan plat nomor yang sesuai: ',).upper()
                    carDict[code][7] : Plate
                    Fuel        = pyi.inputStr('[Fuel] Silahkan masukan jenis bahan bakar: ',).title()
                    carDict[code][8] : Fuel
                    Owner       = pyi.inputStr('[Owner] Silahkan masukkan nama pemilik yang baru: ',).title()
                    carDict[code][9] : Owner
                    confirmupdate = pyi.inputYesNo(prompt='Apakah data ini ingin di update ?(y/n): ')
                    if confirmupdate == 'yes':
                        carDict[code]= [No, codebaru, unitinfo, Transmition, Merk, Color, Year, Plate, Fuel,Owner]
                        clearscreen()
                        print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                        print('Data sudah berhasil di update')
                        return carDict
                    else:
                        os.system('cls')
                        break
                else:
                    os.system('cls')
                    break
            else:
                os.system('cls')
                print('Maaf code tidak terdaftar')
                break
        else:
            os.system('cls')
            break
    return carDict

def updatedatabycolumn(carDict):
    clearscreen()
    while True:
        updatingdata = pyi.inputChoice(prompt='Update data tertentu ?(y/n): ', choices=['y', 'n'])
        if updatingdata == 'y':
            showsub(carDict)
            code = pyi.inputStr("masukkan code data yang ingin di update:").upper()
            if code in carDict:
                clearscreen()
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                continueupdating = pyi.inputChoice(prompt='Apakah data ini ingin di update ?(y/n): ', choices=['y', 'n'])
                if continueupdating == 'y':
                    pilihdata= pyi.inputChoice(
                        prompt='Masukkan nama kolom yang ingin di update: ',
                        choices=['Code','Unit info', 'Transmition', 'Merk', 'Color', 'Year', 'Plate', 'Fuel', 'Owner']).capitalize()
                    if pilihdata == 'Code':
                        code1 = pyi.inputStr("Ganti dengan code yang baru:").upper()
                        if  code1 in carDict.keys():
                            clearscreen()
                            print('Maaf Code sudah digunakkan')
                        elif code1 not in carDict.keys():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan code yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][1] = code1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Unit info':
                        nama1 = pyi.inputStr("Masukkan nama yang baru:").capitalize()
                        if  nama1 in carDict[code][2]:
                            clearscreen()
                            print('\n\nMaaf tidak ada perbedaan pada data yang di update')
                        elif nama1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan data yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][2] = nama1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Transmition':
                        transmition1 = pyi.inputStr("Masukkan jenis transmisi unit:").upper()
                        if  transmition1 in carDict[code][3]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif transmition1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan jenis transmisi yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][3] = transmition1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Merk':
                        Merk1 = pyi.inputStr("Masukkan merk unit:").capitalize()
                        if  Merk1 in carDict[code][4]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Merk1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan merk yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][4] = Merk1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Color':
                        Color1 = pyi.inputStr("Masukkan warna baru unit:").capitalize()
                        if  Color1 in carDict[code][5]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Color1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan warna yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][5] = Color1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Year':
                        Year1 = str(pyi.inputInt('Silahkan masukkan tahun produksi: '))
                        if  Year1 in carDict[code][6]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Year1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan tahun produksi yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][6] = Year1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Plate':
                        Plate1 = pyi.inputStr('Masukkan nomor plate baru: ').upper()
                        if  Plate1 in carDict[code][7]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Plate1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan nomor plate yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][7] = Plate1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Fuel':
                        Fuel1 = pyi.inputStr("Ubah jenis bahan bakar unit:").capitalize()
                        if  Fuel1 in carDict[code][8]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Fuel1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan jenis bahan bakar yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][8] = Fuel1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    elif pilihdata == 'Owner':
                        Owner1 = pyi.inputStr("Ubah nama pemilik yang baru:").title()
                        if  Owner1 in carDict[code][9]:
                            clearscreen()
                            print('Maaf tidak ada perbedaan pada data yang di update')
                        elif Owner1 not in carDict.items():
                            confirmupdat= pyi.inputChoice(prompt='Simpan perubahan nama pemilik yang baru?(y/n): ', choices=['y', 'n'])
                            if confirmupdat == 'y':
                                carDict[code][9] = Owner1
                                clearscreen()
                                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                                print('Data sudah berhasil di update')
                            else:
                                clearscreen()
                                break
                    else:
                        continue
                else:
                    clearscreen()
                    continue
            else:
                clearscreen()
                print('Maaf code yang anda masukkan tidak terdaftar')
                continue
        elif updatingdata == 'n':
            break
        else:
            continue
    
        return carDict
    clearscreen()

def delete(carDict):
    while True:
        prompt = '''
---CAR DATA ISTIMEWA TRANSPORT---
-- Update data--

1. Delete data
2. Bact to main menu
'''
        print(prompt)
        subdelete = pyi.inputInt('masukkan pilihan: ')
        clearscreen()
        if subdelete == 1:
            deletedata(carDict) # penghapusan data dari database
        elif subdelete == 2:
            confirmmenu= pyi.inputYesNo('Back to main menu ?: ') # konfirmasi user kembali ke menu utama
            if confirmmenu == 'yes':
                clearscreen()
                break
        else:
            os.system('cls')
            print('Opsi tidak tersedia')

def deletedata(carDict):
    while True:
        showsub(carDict)
        deletingdata = pyi.inputChoice(prompt='Apakah ada data yang perlu di hapus ?(y/n): ', choices=['y', 'n'])
        if deletingdata == 'y':
            code = pyi.inputStr("masukkan code data yang ingin di hapus:").upper()
            clearscreen()
            if code in carDict:
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                for i in carDict.values():
                    if i[0]== 'No':
                        continue
                    elif i[0] > carDict[code][0]:
                        i[0]-= 1
                continuedeleting = pyi.inputChoice(prompt='Hapus data ini ?(y/n): ', choices=['y', 'n'])
                if continuedeleting == 'y':
                    del carDict[code]
                    showsub(carDict)
                    print('Data sudah berhasil dihapus')

                    break
                else:
                    clearscreen()
                    for i, val in enumerate(carDict.values()):
                        if val[0] == 'No':
                            continue
                        val[0] = i
                    break
            else:
                print('Maaf code yang anda masukan tidak tersedia')
                break
        else:
            clearscreen()
            break