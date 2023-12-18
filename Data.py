# Implementação da classe data

class Data(object):
    # Médoto construtor
    def __init__(self, dia, mes, ano):
        self.setMes(mes)
        # self.dia = dia obsoleto
        self.setDia(dia)
        # self.mes = mes obsoleto
        self.ano = ano
        # self.ano = ano obsoleto

    # Encapsulamento
    def getDia(self):
        return self.dia

    def setDia(self, dia):
        if dia >= 1 and dia <= 31:
            if self.getMes() in(4, 6, 9, 11):
                if dia <= 30:
                    self.dia = dia
                else:
                    self.dia = 1
            elif self.getMes() == 2:
                if dia <= 28:
                    self.dia = dia
                else:
                    self.dia = 1
            else:
                self.dia = dia
        else:
            self.dia = 1

    def getMes(self):
        return self.mes

    def setMes(s