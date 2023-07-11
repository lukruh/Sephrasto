# Implementation for Waffen. Using the type object pattern.
# WaffeDefinition: type object, initialized with database values
# Waffe: character editor values, initialised with definition but supports overrides.

class WaffeDefinition:
    displayName = "Waffe"
    keinKampfstil = "Kein Kampfstil"

    def __init__(self):
        # Serialized properties
        self.name = ''
        self.würfel = 0
        self.würfelSeiten = 6
        self.plus = 0
        self.eigenschaften = []
        self.härte = 6
        self.rw = 0
        self.wm = 0
        self.fertigkeit = ''
        self.talent = ''
        self.kampfstile = []
        self.lz = 0
        self.fernkampf = False

        # Derived properties after deserialization
        self.anzeigename = ''

    def deepequals(self, other): 
        if self.__class__ != other.__class__: return False
        return self.__dict__ == other.__dict__
    
    def finalize(self, db):
        self.anzeigename = self.name
        for trim in [f" ({self.talent})", " (NK)", " (FK)"]:
            if self.anzeigename.endswith(trim):
                self.anzeigename = self.anzeigename[:-len(trim)]

    @property
    def nahkampf(self):
        return not self.fernkampf

    def typname(self, db):
        return self.talent

    def details(self, db):
        lz = ""
        if self.fernkampf:
            lz = f"| LZ {self.lz} "
        eigenschaften = " -"
        if len(self.eigenschaften) > 0:
            eigenschaften = ', '.join(self.eigenschaften)

        return f"TP {self.würfel}W{self.würfelSeiten}{'+' if self.plus >= 0 else ''}{self.plus} | WM {self.wm} | RW {self.rw} {lz}| Härte {self.härte} | {eigenschaften}"

class Waffe:
    def __init__(self, definition):
        self.definition = definition
        self._lzOverride = None
        self._wmOverride = None
        self._rwOverride = None
        self._würfelOverride = None
        self._würfelSeitenOverride = None
        self._plusOverride = None
        self._eigenschaftenOverride = None
        self._härteOverride = None
        self._anzeigenameOverride = None
        self.kampfstil = WaffeDefinition.keinKampfstil

    def __deepcopy__(self, memo=""):
        W = Waffe(self.definition)
        W._lzOverride = self._lzOverride
        W._wmOverride = self._wmOverride
        W._rwOverride = self._rwOverride
        W._würfelOverride = self._würfelOverride
        W._würfelSeitenOverride = self._würfelSeitenOverride
        W._plusOverride = self._plusOverride
        if self._eigenschaftenOverride:
            W._eigenschaftenOverride = self._eigenschaftenOverride.copy()
        W._härteOverride = self._härteOverride
        W._anzeigenameOverride = self._anzeigenameOverride
        W.kampfstil = self.kampfstil
        return W

    @property
    def name(self):
        return self.definition.name

    @property
    def würfel(self):
        if self._würfelOverride is not None:
            return self._würfelOverride
        return self.definition.würfel

    @würfel.setter
    def würfel(self, würfel):
        self._würfelOverride = würfel

    @property
    def würfelSeiten(self):
        if self._würfelSeitenOverride is not None:
            return self._würfelSeitenOverride
        return self.definition.würfelSeiten

    @würfelSeiten.setter
    def würfelSeiten(self, würfelSeiten):
        self._würfelSeitenOverride = würfelSeiten

    @property
    def plus(self):
        if self._plusOverride is not None:
            return self._plusOverride
        return self.definition.plus

    @plus.setter
    def plus(self, plus):
        self._plusOverride = plus

    @property
    def eigenschaften(self):
        if self._eigenschaftenOverride is not None:
            return self._eigenschaftenOverride
        return self.definition.eigenschaften

    @eigenschaften.setter
    def eigenschaften(self, eigenschaften):
        self._eigenschaftenOverride = eigenschaften

    @property
    def härte(self):
        if self._härteOverride is not None:
            return self._härteOverride
        return self.definition.härte

    @härte.setter
    def härte(self, härte):
        self._härteOverride = härte

    @property
    def rw(self):
        if self._rwOverride is not None:
            return self._rwOverride
        return self.definition.rw

    @rw.setter
    def rw(self, rw):
        self._rwOverride = rw

    @property
    def wm(self):
        if self._wmOverride is not None:
            return self._wmOverride
        return self.definition.wm

    @wm.setter
    def wm(self, wm):
        self._wmOverride = wm

    @property
    def fertigkeit(self):
        return self.definition.fertigkeit

    @property
    def talent(self):
        return self.definition.talent

    @property
    def kampfstile(self):
        return self.definition.kampfstile

    @property
    def lz(self):
        if self._lzOverride is not None:
            return self._lzOverride
        return self.definition.lz

    @lz.setter
    def lz(self, lz):
        self._lzOverride = lz

    @property
    def fernkampf(self):
        return self.definition.fernkampf

    @property
    def nahkampf(self):
        return self.definition.nahkampf

    @property
    def anzeigename(self):
        if self._anzeigenameOverride is not None:
            return self._anzeigenameOverride
        return self.definition.anzeigename

    @anzeigename.setter
    def anzeigename(self, anzeigename):
        self._anzeigenameOverride = anzeigename

    def typname(self, db):
        return self.definition.typname(db)