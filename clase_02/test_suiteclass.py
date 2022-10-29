class TestSuite:

    def do_something(self):
        print('Hola')

    def test_hola_mundo(self):
        raise ValueError()

    def test_valido(self):
        self.do_something()
        True
