import translator as tr

t = tr.Translator("dictionary.txt")


while(True):

    t.printMenu()

    t.loadDictionary()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input("Ok, quale parola devo aggiungere?\n")
        t.handleAdd(txtIn)
    elif int(txtIn) == 2:
        txtIn = input("Ok, quale parola devo tradurre?\n")
        print(f"la traduzione di {txtIn} è {t.handleTranslate(txtIn)}")
    elif int(txtIn) == 3:
        txtIn = input("Ok, quale wild devo tradurre?\n")
        for p in t.handleWildCard(txtIn):
            print(f"la traduzione di {p} é {t.handleTranslate(p)}")
    elif int(txtIn) == 4:
        break