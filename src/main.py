import csv
import sys
import os
import rentcar as rc
import pyinputplus as pyi
os.system('cls')





carDict = {}

def getCardb():
    global carDict
    with open(pathunitdetail, 'r') as file:
        car_reader = csv.reader(file, delimiter=':')
        for i, val in enumerate(car_reader):
            if i == 0:
                # print(i, val)
                header = val
                carDict.update({'key': header})
                # print(f'{key}: {val}')
                continue
            No, Code, Unit_info, transmition, Merk, Color, Year, Plate, Fuel, Owner = val
            carDict.update({(Code): [int(No), Code, Unit_info, transmition, Merk, Color, Year, Plate, Fuel, Owner]})
        return carDict


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
    # windows
    if os.name == 'nt':
        os.system('cls')
    # Mac or Linux
    else:
        os.system('clear')

def main():
    global carDict
    while True:
        print(prompt)
        menu = pyi.inputInt(prompt='Silahkan pilih menu: ')
        os.system('cls')
        if menu == 1:
            rc.show(carDict)
        elif menu == 2:
            rc.add(carDict)
        elif menu == 3:
            rc.update(carDict)
        elif menu == 4:
            rc.delete(carDict)
        else:
            confirmexit= pyi.inputYesNo('Do you want to exit from the program ?: ')
            if confirmexit == 'yes':
                clearscreen()
                break
            else:
                clearscreen()
                continue
            

    with open(pathunitdetail, 'w') as file:
        carDictWritter = csv.writer(file, delimiter=':', lineterminator='\n')
        carDictWritter.writerows(carDict.values())
        


if __name__ == '__main__':
    pathunitdetail = "data/1.dictunitdetail.csv"
    getCardb()
    main()
