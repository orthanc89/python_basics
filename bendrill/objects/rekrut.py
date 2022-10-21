

"""dies erzeugt eine klasse/objekt rekrut"""

class rekrut():
    """dies ist die klasse rekrut()"""
    def __init__(self):
        self.vname = ""
        self.nname = ""
        self.alter = ""
        self.gender = ""

    def get_vname(self):
        return self.vname
    def set_vname(self, vname):
        self.vname = vname
        return self

    def get_nname(self):
        return self.nname
    def set_nname(self, nname):
        self.nname = nname
        return self

    def get_alter(self):
        return self.alter
    def set_alter(self, alter):
        self.alter = alter
        return self

    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender
        return self

    def get_dict(self):
        out = {'vname':self.vname,'nname':self.nname, 'alter':self.alter, 'gender':self.gender}
        return out

    def set_dict(self,dict):
        self.vname = dict["vname"]
        self.nname = dict["nname"]
        self.alter = dict["alter"]
        self.get_gender(dict["gender"])