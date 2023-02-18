import os

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. View All Contact")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")

        if os.path.isfile('./contact.txt') == True:
            with open("contact.txt", 'a') as f:
                f.write(f'{name} {phone}\n')
            f.close()
        else:
            with open("contact.txt", 'w') as f:
                f.write(f'{name} {phone}\n')
            f.close()
        os.system('cls')

    elif choice == '2':
        name = input("Enter Name : ")
        f = open('contact.txt')
        data = f.readlines()

        with open('contact.txt', 'r') as fr:
            fc = fr.read()

            if name in fc:
                for line in data:
                    x = line.split()
                    if (name == x[0]):
                        print(f"{x[0]} : {x[1]}")
            else:
                print("Contact not found")

        f.close()
        os.system('pause')
        os.system('cls')

    elif choice == '3':
        name = input("Enter Name : ")
        f = open('contact.txt')
        data = f.read()
        ds = data.split("\n")
        save = {}
        i = 0

        with open('contact.txt', 'r') as fr:
            fc = fr.read()

            if name in fc:
                for line in ds:
                    x = line.split(" ")
                    if (name != x[0]):
                        save[i] = line
                        i = i + 1

                f = open('contact.txt', 'w')
                for i in save:
                    if i != len(save)-1:
                        f.write(f"{save[i]}\n")
                else:
                    f.write(save[i])
                f.close()
            else:
                print("Contact not found")

        os.system('pause')
        os.system('cls')

    elif choice == '4':
        name = input("Enter Name : ")
        f = open('contact.txt')
        data = f.readlines()
        update = {}
        i = 0

        with open('contact.txt', 'r') as fr:
            fc = fr.read()

            if name in fc:
                for line in data:
                    x = line.split()
                    if (name == x[0]):
                        new_number = input("Enter New Number : ")
                        update_number = line.replace(x[1], new_number)
                        update[i] = update_number
                    else:
                        update[i] = line
                    i = i + 1
                f = open('contact.txt', 'w')
                for i in update:
                    f.write(update[i])
                f.close()
            else:
                print("Contact not found")

        os.system('pause')
        os.system('cls')

    elif choice == '5':
        f = open('contact.txt')
        data = f.readlines()

        if data:
            print("Contacts : ")
            for line in data:
                x = line.split()
                print(f"{x[0]} : {x[1]}")
        else:
            print("No contacts in phone book")
        f.close()
        os.system('pause')
        os.system('cls')

    elif choice == '6':
        print("Sayonara :)")
        break
    else:
        print("Invalid Choice")
        os.system('pause')
        os.system('cls')
