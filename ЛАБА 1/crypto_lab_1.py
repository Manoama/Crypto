import math

with open("new_text.txt", "w") as myfile:
    myfile.writelines("")

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def Output_all_Entropies(Entrop_list):
    print("__________________\nEntropies:\n")
    c = 1
    for i in range(len(Entrop_list)):
        print(f'H_{c}{(i % 3) + 1} = {Entrop_list[i]}')
        if i == 2:
            print()
            c = 2
        


def Sorting(d):
    sorted_values = sorted(d.values()) 
    sorted_dict = {}
    for i in sorted_values:
        for k in d.keys():
            if d[k] == i:
                sorted_dict[k] = d[k]
                break
    return sorted_dict


def Mono_with_space(file_name):
    d = dict()
    with open(file_name, "r") as f_last: # Считываем из "Чистого" файла
        
        s = f_last.read()

        for i in s:
            if i.lower() not in d:
                d[i.lower()] = 1 # Добавляем новые символы
            else:
                d[i.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1
        
        sorted_dict = Sorting(d)
        return sorted_dict

def Bi_with_space_crossing(file_name):
    d = dict()    
    with open("new_text.txt", "r") as f_last: # Считываем из "Чистого" файла

        s = f_last.read()

        for i in range(len(s) - 1):
            bi = s[i] + s[i + 1]
            if bi.lower() not in d:
                d[bi.lower()] = 1 # Добавляем новые символы
            else:
                d[bi.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1
        
        sorted_dict = Sorting(d)
        return sorted_dict

def Bi_with_space_NOT_crossing(file_name):
    d = dict()
    with open("new_text.txt", "r") as f_last: # Считываем из "Чистого" файла

        s = f_last.read()

        for i in range(0, len(s) - 1, 2):
            bi = s[i] + s[i + 1]
            if bi.lower() not in d:
                d[bi.lower()] = 1 # Добавляем новые символы
            else:
                d[bi.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1 

        sorted_dict = Sorting(d)
        return sorted_dict

def Mono_withOUT_space(file_name):
    d = dict()
    with open("new_text.txt", "r") as f_last: # Считываем из "Чистого" файла
        
        s = f_last.read()

        for i in s:
            if i.lower() not in d:
                d[i.lower()] = 1 # Добавляем новые символы
            else:
                d[i.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1

        sorted_dict = Sorting(d)
        return sorted_dict
    
def Bi_withOUT_space_crossing(file_name):
    d = dict()
    with open("new_text.txt", "r") as f_last: # Считываем из "Чистого" файла

        s = f_last.read()

        for i in range(len(s) - 1):
            bi = s[i] + s[i + 1]
            if bi.lower() not in d:
                d[bi.lower()] = 1 # Добавляем новые символы
            else:
                d[bi.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1
        
        sorted_dict = Sorting(d)
        return sorted_dict

def Bi_withOUT_space_NOT_crossing(file_name):
    d = dict()
    with open("new_text.txt", "r") as f_last: # Считываем из "Чистого" файла

        s = f_last.read()

        for i in range(0, len(s) - 1, 2):
            bi = s[i] + s[i + 1]
            if bi.lower() not in d:
                d[bi.lower()] = 1 # Добавляем новые символы
            else:
                d[bi.lower()] += 1 # Увеличиваем кол-во символа 'i' на 1
        
        sorted_dict = Sorting(d)
        return sorted_dict


#######

def Probabil(d):
    size = 0
    # Calculate all elems 
    for key in d.keys():
        size += d[key]
    # Find prob-ies of each key: 
    for key in d.keys():
        d[key] = d[key] / size 

    # Demo: (table of prob-ies)
    for key,value in d.items():
        print(f'"{key}": {toFixed(value, 6)}') 
    print(f'Len = {len(d)}')

    #Checking the normalization condition:
    check_sum = 0
    for i in d.values():
        check_sum += i
    print(f'Check: Sum = {check_sum}')
    print(" ")
    return d

def H_mono(d):
    H1 = 0
    for val in d.values():
        H1 += val * math.log2(val)
    print(f'H = {-H1}')
    return -H1

def H_bi(d):
    H2 = 0
    for val in d.values():
        H2 += val * math.log2(val)
    print(f'H = {-H2/2}')
    return -H2/2
    

def main():
    d = dict()
    choice0 = int(input('Print...\n1 - To choose options \n2 - Output all\n>'))
    if choice0 == 1:    
        choise1 = int(input('Print...\n1 - With space \n2 - WithOUT Space\n>'))
    
        if choise1 == 1:
            # С пробелами
            with open('text.txt', 'r') as f: # "Грязный" файл
                print(f'{f.name} is opend')

                s = f.read()
                s = s.replace('ё','е')
                with open("new_text.txt", "a") as f_new: # "Чистый" файл
                    print(f'{f_new.name} is opend')
                    # Чистим файл от ненужных символов:
                    for i in s:
                        if (ord(i) >= 1040 and ord(i) <= 1103) or i == " ":
                            f_new.write(i.lower())
        elif choise1 == 2:
            # Без пробелов
            with open('text.txt', 'r') as f: # "Грязный" файл
                print(f'{f.name} is opend')

                s = f.read()
                s = s.replace('ё','е')
                size = len(s)

                with open("new_text.txt", "a") as f_new: # "Чистый" файл
                    print(f'{f_new.name} is opend')
                    # Чистим файл от ненужных символов:
                    for i in s:
                        if ord(i) >= 1040 and ord(i) <= 1103:
                            f_new.write(i.lower())
        else:
            print('Wrong input')
            exit(0)

        choise2 = int(input('Print...\n1 - Mono \n2 - Bi crossing \n3 - Bi NOT crossing\n>'))

        if choise1 == 1 and choise2 == 1:
            d = Mono_with_space("new_text.txt")
            print(d)
            d = Probabil(d)
            H_mono(d)
        elif choise1 == 1 and choise2 == 2:
            d = Bi_with_space_crossing("new_text.txt")
            print(d)
            d = Probabil(d)
            H_bi(d)
        elif choise1 == 1 and choise2 == 3:
            d = Bi_with_space_NOT_crossing("new_text.txt")
            print(d)
            d = Probabil(d)
            H_bi(d)
        elif choise1 == 2 and choise2 == 1:
            d = Mono_withOUT_space("new_text.txt")
            print(d)
            d = Probabil(d)
            H_mono(d)
        elif choise1 == 2 and choise2 == 2:
            d = Bi_withOUT_space_crossing("new_text.txt")
            print(d)
            d = Probabil(d)
            H_bi(d)
        elif choise1 == 2 and choise2 == 3:
            d = Bi_withOUT_space_NOT_crossing("new_text.txt")
            print(d)
            d = Probabil(d)
            H_bi(d)
        else:
            print("Wrong input")
            exit(0)
    elif choice0 == 2:
        #Create list of Entropies:
        Entropies = list()
        # С пробелами
        with open('text.txt', 'r') as f: # "Грязный" файл
            print(f'{f.name} is opend')

            s = f.read()
            s = s.replace('ё','е')
            with open("new_text.txt", "a") as f_new: # "Чистый" файл
                print(f'{f_new.name} is opend')
                # Чистим файл от ненужных символов:
                for i in s:
                    if (ord(i) >= 1040 and ord(i) <= 1103) or i == " ":
                        f_new.write(i.lower())
            d = Mono_with_space("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_mono(d))

            d = Bi_with_space_crossing("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_bi(d))

            d = Bi_with_space_NOT_crossing("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_bi(d))

        # Без пробелов
        with open('text.txt', 'r') as f: # "Грязный" файл
            print(f'{f.name} is opend')

            s = f.read()
            s = s.replace('ё','е')
            size = len(s)

            with open("new_text.txt", "a") as f_new: # "Чистый" файл
                print(f'{f_new.name} is opend')
                # Чистим файл от ненужных символов:
                for i in s:
                    if ord(i) >= 1040 and ord(i) <= 1103:
                        f_new.write(i.lower())
        
            d = Mono_withOUT_space("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_mono(d))

            d = Bi_withOUT_space_crossing("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_bi(d))

            d = Bi_withOUT_space_NOT_crossing("new_text.txt")
            # print(d)
            d = Probabil(d)
            Entropies.append(H_bi(d))

            Output_all_Entropies(Entropies)

    else:
        print("Wrong input") 
        exit(0)   


if __name__ == "__main__":
    main()
