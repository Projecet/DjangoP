# countrydb table
# id(str), pwd(str), name(str)

class CountryVO:
    def __init__(self, id, name, qurantine, population, total_cases, infected, safe):
        self.id = id
        self.name = name
        self.qurantine = qurantine
        self.population = population
        self.total_cases = total_cases
        self.infected = infected
        self.safe = safe

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getQurantine(self):
        return self.qurantine

    def getPopulation(self):
        return self.population

    def getTotal_cases(self):
        return self.total_cases

    def getInfected(self):
        return self.infected

    def getSafe(self):
        return self.safe

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setQurantine(self, qurantine):
        self.qurantine = qurantine

    def setPopulation(self, population):
        self.population = population

    def setTotal_cases(self, total_cases):
        self.total_cases = total_cases

    def setInfected(self, infected):
        self.infected = infected

    def setSafe(self, safe):
        self.safe = safe

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.id, self.name, self.qurantine, self.population,
                                         self.total_cases, self.infected, self.safe)
