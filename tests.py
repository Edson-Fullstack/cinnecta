import unittest
from app import fatorial


class TestFatorial(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(4), 24)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)

if __name__ == '__main__':
    unittest.main()
    resultProva=['falar', 'é' , 'fácil' ,'mostre' , 'me' , 'o' , 'código' , 'escrever' , 'difícil' , 'que' , 'funcione']
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']