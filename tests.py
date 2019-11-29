import unittest
from app import myapp


class TestPages(unittest.TestCase):
    #testa a pagina principal
    def test_page_home(self):
        app = myapp.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)

    #testa a pagina para o primeiro exercicio
    def test_page_gram1(self):
        app = myapp.test_client()
        response = app.get('/gram1')
        self.assertEqual(200, response.status_code)
        
    #testa a pagina para o segundo exercicio exercicio
    def test_page_gram2(self):
        app = myapp.test_client()
        response = app.get('/gram2')
        self.assertEqual(200, response.status_code)

    #testa a pagina para o manual
    def test_page_manual(self):
        app = myapp.test_client()
        response = app.get('/manual')
        self.assertEqual(200, response.status_code)
    
    #teste acesso a pagina inexistente
    def test_page_fail(self):
        app = myapp.test_client()
        response = app.get('/fail')
        self.assertEqual(404, response.status_code)




if __name__ == '__main__':
    unittest.main()