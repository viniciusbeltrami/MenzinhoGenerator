import unittest
from EstagiariosGen import estagiarios

class TestGeradorEstagiarios(unittest.TestCase):
    def setUp(self):
        self.estagiarios = estagiarios
    def teste_estagiarios(self):
        #verificiar se todos tem nome e apelido
        for estagiario in self.estagiarios:
            self.assertIsNotNone(estagiario.nome,'Todo estagiario deve ter um nome')
            self.assertIsNotNone(estagiario.apelido,'Todo estagiario deve ter um apelido')
    def teste_estagiarios_mesmo_nome(self):
        nomes=set()
        for estagiario in self.estagiarios:
            self.assertNotIn(estagiario.nome, nomes, f"Nome duplicado:{estagiario.nome}")
            nomes.add(estagiario.nome)
    def teste_estagiarios_mesmo_apelido(self):
        apelidos=set()
        for estagiario in self.estagiarios:
            self.assertNotIn(estagiario.apelido, apelidos, f"Apelido duplicado:{estagiario.apelido}")
            apelidos.add(estagiario.apelido)

if __name__ == '__main__':
    unittest.main()