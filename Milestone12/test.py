
def testfunktion():
    return "test"

class tier():

    def __init__(self):
        self.tierart = "biene"
        self.bewegung = "fliegen/krabbeln/laufen"
        self.laut = "sum sum"
        self.name = 'Biene maja'
        self.beine = "6"
        self.gattung = 'Insekt'
        self.stoerfaktor = True

    def bewegen(self):
        return "laufen"

    def laut_geben(self):
        return "sum sum"

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name


#test = testfunktion()

meintier = tier()
print(meintier.get_name())

deintier = tier()
deintier.set_name("Willi")
print(deintier.get_name())