from tabulate import tabulate
import os
import pyinputplus as pyi

pathunitdetail = "src/1.dictunitdetail.csv"

def clearscreen():
    # windows
    if os.name == 'nt':
        os.system('cls')
    # Mac or Linux
    else:
        os.system('clear')

def show(carDict):
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
        list = pyi.inputInt('masukkan opsi: ')
        clearscreen()
        if list == 1:
            showsub(carDict)
        elif list == 2:
            showbycode(carDict)
        elif list == 3:
            confirmmain= pyi.inputYesNo('Back to main menu ?: ')
            if confirmmain == 'yes':
                clearscreen()
                break
        else:
            clearscreen()
            print('Opsi tidak tersedia')


def showsub(carDict):
    while True:
        if len(carDict) >= 1:
            header = carDict['key']
            data = list(carDict.values())[1:]
            print(tabulate(data, header, tablefmt='pretty'))
            break
        else:
            print('Maaf data belum tersedia')
            break

def showbycode(carDict):
    showsub(carDict)
    while True:
        header = carDict['key']
        data = False
        codevalue = []
        codeinput = pyi.inputStr("masukkan code : ").upper()
        for key, val in carDict.items():
            if codeinput.upper() == carDict[key][1].upper():
                codevalue.append(val)
                data = True
        if not data:
            print("\n\n\nMaaf data tidak tersedia")
        else:
            os.system('cls')
            print(f'\n{codeinput.upper()} data: \n')
            print(tabulate(codevalue, headers=header, tablefmt="pretty"))
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
            prompt='ingin menambahkan data baru ?(y/n): ', choices=['y', 'n'])
        if newdata == 'y':
            No = len(carDict)
            code = input("masukkan code unit baru:").upper()
            if code in carDict:
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                print("Maaf code sudah digunakan")
            else:
                Unitinfo = pyi.inputStr("masukkan nama unit baru(co: calya): ").capitalize()
                transmition = pyi.inputStr("masukkan jenis transmition (at/mt): ").upper()
                Merk = pyi.inputStr("masukkan nama merk(co: toyota): ").capitalize()
                Color = pyi.inputStr("masukkan warna unit(co: silver): ").capitalize()
                Year = pyi.inputInt("masukkan tahun pembuatan(co: 2021): ")
                Plate = pyi.inputStr("masukkan plat nomer(co: AB4511RD): ").upper()
                Fuel = pyi.inputStr("masukkan bahan bakar unit(co: pertalite): ").capitalize()
                Owner = pyi.inputStr("masukkan nama pemilik(co: Aditya): ").capitalize()
                saving = pyi.inputStr('Simpan data yang baru ? (y/n): ')
                if saving == 'y':
                    clearscreen()
                    carDict.update({f'{code}': [No, code, Unitinfo, transmition, Merk, Color, Year, Plate, Fuel,Owner]})
                    print('Data sudah berhasil di input')
                    showsub(carDict)                
                elif saving == "n":
                    break
        # elif:
        # print('maaf opsi yang anda masukan salah')
        else:
            break
        return carDict
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
            updatedata(carDict)
        elif subupdate == 2:
            updatedatabycolumn(carDict)
        elif subupdate == 3:
            confirmmain= pyi.inputYesNo('Back to main menu ?: ')
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
        updatingdata = pyi.inputChoice(prompt='ingin mengubah data tertentu ?(y/n): ', choices=['y', 'n'])
        if updatingdata == 'y':
            showsub(carDict)
            code = pyi.inputStr("masukkan code data yang ingin di update:").upper()
            if code in carDict:
                clearscreen()
                print(tabulate([carDict[code]], carDict['key'], tablefmt='pretty'), '\n\n')
                continueupdating = pyi.inputChoice(prompt='Apakah data ini ingin di update ?(y/n): ', choices=['y', 'n'])
                if continueupdating == 'y':
                    No = carDict[code][0]
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
                    unitinfo    = pyi.inputStr('[Unit info] Silahkan ganti dengan nama yang baru: ',).title() #applyFunc=lambda x: x.capitalize())
                    carDict[code][2] : unitinfo
                    Transmition = pyi.inputStr('[Transmition] Silahkan ganti jenis transmition (at/mt): ',).upper()  #applyFunc=lambda x: x.upper())
                    carDict[code][3] : Transmition
                    Merk        = pyi.inputStr('[Merk] Silahkan masukkan Merk unit: ',).title()  #applyFunc=lambda x: x.title())
                    carDict[code][4] : Merk
                    Color       = pyi.inputStr('[Color] Silahkan masukkan warna terbaru: ',).title()  #applyFunc=lambda x: x.title())
                    carDict[code][5] : Color
                    Year        = pyi.inputInt('[Year] Silahkan masukkan tahun produksi: ',)  #applyFunc=lambda x: x)
                    carDict[code][6] : Year
                    Plate       = pyi.inputStr('[Plate] Silahkan ganti dengan plat nomor yang sesuai: ',).upper()  #applyFunc=lambda x: x.upper())
                    carDict[code][7] : Plate
                    Fuel        = pyi.inputStr('[Fuel] Silahkan masukan jenis bahan bakar: ',).title()  #applyFunc=lambda x: x.title())
                    carDict[code][8] : Fuel
                    Owner       = pyi.inputStr('[Owner] Silahkan masukkan nama pemilik yang baru: ',).title()  #applyFunc=lambda x: x.title())
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
            deletedata(carDict)
        elif subdelete == 2:
            confirmmenu= pyi.inputYesNo('Back to main menu ?: ')
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