import csv
import sys
import os
import rentcar as rc
import pyinputplus as pyi
os.system('cls')





carDict = {} # membuat dictionasry database kosong

def getCardb():
    global carDict # mengakses data database
    with open(pathunitdetail, 'r') as file:
        car_reader = csv.reader(file, delimiter=':')
        for i, val in enumerate(car_reader): #mengiterasi file csv untuk dijadikan dictionary database
            if i == 0:
                header = val
                carDict.update({'key': header}) 
                continue
            No, Code, Unit_info, transmition, Merk, Color, Year, Plate, Fuel, Owner = val
            carDict.update({(Code): [int(No), Code, Unit_info, transmition, Merk, Color, Year, Plate, Fuel, Owner]}) # menjadikan code sebagai primary key 
        return carDict #mengmbalikan hasil iterasi ke dalam database dengan format dictionary 


prompt = '''

---VEHICLE DATA---
list Display main
1. Data
2. Add data
3. Update data
4  Delete data
5. EXIT

'''
def clearscreen():
    #untuk membersihkan layar tampilan
    # untuk pengguna windows
    if os.name == 'nt':
        os.system('cls')
    # untuk pengguna Mac or Linux
    else:
        os.system('clear')

def main():
    global carDict #untuk mengakses database carDict
    while True:
        print(prompt)
        menu = pyi.inputInt(prompt='Silahkan pilih menu: ')
        os.system('cls')
        if menu == 1:
            rc.show(carDict) # menampilkan menu tampilan data
        elif menu == 2:
            rc.add(carDict) # menambahkan data baru pada database
        elif menu == 3:
            rc.update(carDict) # untuk edit data apabila ada perubahan pada data
        elif menu == 4:
            rc.delete(carDict) # untuk menghapus data apabila ada data yang tidak diperlukan
        else:
            # konfirmasi user untuk exit dari program
            confirmexit= pyi.inputYesNo('Do you want to exit from the program ?: ')
            if confirmexit == 'yes':
                clearscreen()
                break
            else:
                clearscreen()
                continue
            
    # setelah exit data pada database akan diperbaharui 
    with open(pathunitdetail, 'w') as file:
        carDictWritter = csv.writer(file, delimiter=':', lineterminator='\n')
        carDictWritter.writerows(carDict.values())
        


if __name__ == '__main__':
    pathunitdetail = "data/1.dictunitdetail.csv"
    getCardb()
    main()
