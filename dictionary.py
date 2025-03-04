class Dictionary:

    dizionario = {}
    def __init__(self, dict):
        with open(dict, "r", encoding="utf-8") as file:
            righe = file.readlines()
            for riga in righe:
                [key, value] = riga.strip("\n").split(" ")
                if(key in self.dizionario):
                    self.dizionario[key].append(value)
                else:
                    self.dizionario[key] = [value]


    def addWord(self, alieno, italiano):
       if alieno.lower() in self.dizionario:
           if italiano.lower not in self.dizionario[alieno.lower()]:
               self.dizionario[alieno.lower()].append(italiano.lower())
       else:
           self.dizionario[alieno.lower()] = [italiano.lower()]

    def translate(self, alieno):
        return self.dizionario.get(alieno.lower(), [])

    def translateWordWildCard(self, txt):
        trovate = []
        parts = txt.split("?")
        for t in self.dizionario.keys():
            if len(txt) == len(t):
                if(parts[0]) == t[0:len(parts[0])] and parts[1] == t[len(parts[0])+1:len(t)]:
                    trovate.append(t)
        return trovate