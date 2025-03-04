from dictionary import Dictionary

class Translator:
    def __init__(self, diz):
       self.d = Dictionary(diz)

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print(f" 1. Aggiungi nuova parola")
        print(f" 2. cerca una traduzione")
        print(f" 3. Cerca con wildcard")
        print(f" 4. Exit")


    def loadDictionary(self):
        # dict is a string with the filename of the dictionary
        return self.d.dizionario

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parts = entry.split()
        alieno = parts[0]
        traduzioni = parts[1:]
        for traduzione in traduzioni:
            self.d.addWord(alieno, traduzione)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.d.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.d.translateWordWildCard(query)
        pass