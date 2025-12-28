import random
Lottery = []

while True:
        print("وش تبي تسوي هنا")
        print("1- إضافة عنصر")
        print("2- تعديل عنصر")
        print("3- حذف عنصر")
        print("4- طباعة العناصر")
        print("5- قرعة")
        print("6- خروج")

        choice = input("اكتب رقم الخيار: ")

        if choice == "1":
                new_Lottery = input("العنصر الجديدة")
                Lottery.append(new_Lottery)
                print("تم إضافة العنصر بنجاح")
                print(Lottery)

        elif choice == "2":
                x = int(input("رقم العنصر اللي تبي تعدله"))
                new_Lottery = input("العنصر الجديد")
                Lottery[x - 1] = new_Lottery
                print("تم تعديل العنصر بنجاح")
                print(Lottery)

        elif choice == "3":
                y = int(input("اكتب رقم العنصر الذي تريد حذفه"))
                del Lottery[y-1]
                print("تم حذف العنصر بنجاح")
                print(Lottery)

        elif choice == "4":
                print(Lottery)

        elif choice == "5":
                s = random.randint(0, 4)
                print(Lottery[s])

        elif choice == "6":
                print("مع السلامة")
                break

        else:
                print("الرقم خاطئ")
