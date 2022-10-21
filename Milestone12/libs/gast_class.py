
class gast_class():
    """diese klasse vereint die eigenschaften eiens gastes"""

    def __init__(self):
        self.vname = "john"
        self.nname = "Doe"
        self.gender = "d"  # m/w/d
        self.alter = "00"
        self.covid = False
        self.status = "noshow"
        self.gebdate = '0000.00.00'

    def get_vname(self):
        return self.vname
    def set_vname(self ,name):
        self.vname = name
        return self

    def get_nname(self):
        return self.vname
    def set_nname(self, name):
        self.nname = name
        return self

    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender
        return self

    def get_ater(self):
        return self.alter
    def set_age(self, alter):
        self.alter = alter
        return self

    def get_covid(self):
        return self.covid
    def set_covid(self, covid):
        self.covid = covid
        return self

    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
        return self

    def get_gebdate(self):
        return self.gebdate
    def set_gebdate(self ,gebdate):
        self.gebdate = gebdate
        return self
#################################################################
# gaesteliste = []
# gaesteliste.append(gast())
# gaesteliste.append(gast())
# gaesteliste.append(gast())
# gaesteliste.append(gast())
