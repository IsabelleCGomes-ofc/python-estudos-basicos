class Cliente:
    def __init__(self, n, fone): #metodo construtor, constroi objeto
        self._nome = n #define atributo = parametro que passa pra ele
        self._telefone = fone

    #método get
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome






