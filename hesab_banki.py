hesab_ha = []

# giriad tedad hesab
tedad = int(input("chand hesab mikhai ijad koni? "))

# giriad etelaat hesab ha
for i in range(tedad):
    name = input("esm saheb hesab ra vared kon: ")
    mablagh = float(input("mojodi avaliye hesab ra vared kon: "))
    hesab_ha.append([name, mablagh])

# menue asli
while True:
    print("\n===== menue amaliyat banki =====")
    print("1. namayesh mojodi hame hesab ha")
    print("2. sepordegozari dar hesab")
    print("3. bardasht az hesab")
    print("4. namayesh hesab ha ba mojodi bishtar az miyangin")
    print("5. khoroj az barname")
    
    entekhab = input("yek gozine entekhab kon: ")

    if entekhab == "1":
        print("\nmojodi hame hesab ha:")
        for hesab in hesab_ha:
            print(hesab[0], ":", hesab[1])

    elif entekhab == "2":
        name = input("esm hesab baraye sepordegozari ra vared kon: ")
        mablagh = float(input("mablagh sepord ra vared kon: "))
        found = False
        for hesab in hesab_ha:
            if hesab[0] == name:
                hesab[1] = hesab[1] + mablagh
                print("seporde ba movafaghiat anjam shod!")
                found = True
                break
        if not found:
            print("hesab peida nashod!")

    elif entekhab == "3":
        name = input("esm hesab baraye bardasht ra vared kon: ")
        mablagh = float(input("mablagh bardasht ra vared kon: "))
        found = False
        for hesab in hesab_ha:
            if hesab[0] == name:
                if hesab[1] >= mablagh:
                    hesab[1] = hesab[1] - mablagh
                    print("bardasht ba movafaghiat anjam shod!")
                else:
                    print("mojodi kafi nist!")
                found = True
                break
        if not found:
            print("hesab peida nashod!")

    elif entekhab == "4":
        if len(hesab_ha) == 0:
            print("hesabi vojod nadarad!")
        else:
            majmo = 0
            for hesab in hesab_ha:
                majmo = majmo + hesab[1]
            miyangin = majmo / len(hesab_ha)
            print("hesab ha ba mojodi bishtar az miyangin (", miyangin, "):")
            for hesab in hesab_ha:
                if hesab[1] > miyangin:
                    print(hesab[0], ":", hesab[1])

    elif entekhab == "5":
        print("khoroj az barname...")
        break

    else:
        print("lotfan yek gozine sahih vared kon!")
