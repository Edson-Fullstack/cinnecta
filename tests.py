import unittest
from app import myapp


class TestHome(unittest.TestCase):
    #testa a pagina principal
    def test_homepage(self):
        app = myapp.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)

    #testa a pagina para o primeiro exercicio
    def test_gram1page(self):
        app = myapp.test_client()
        response = app.get('/gram1')
        self.assertEqual(200, response.status_code)
        
    #testa a pagina para o segundo exercicio exercicio
    def test_gram2page(self):
        app = myapp.test_client()
        response = app.get('/gram2')
        self.assertEqual(200, response.status_code)
    #testa a pagina para o manual

    def test_manualPage(self):
        app = myapp.test_client()
        response = app.get('/manual')
        self.assertEqual(404, response.status_code)

    #verifica conteudo da pagina test
    def test_testPageContent(self):
        string = self.response.data.decode('utf-8')
        self.assertIn('<title>Home Page</title>', str(string))
        self.assertIn('<h1>Testes</h1>', str(string))
        self.assertIn('<p>Implementação de testes ', str(string))

if __name__ == '__main__':
    unittest.main()