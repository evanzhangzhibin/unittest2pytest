# required-method: assertLess

class TestAssertLess(TestCase):
    def test_you(self):
        assert abc < 'xxx'

    def test_me(self):
        assert 123 < xxx+y

    def test_everybody(self):
        assert 'abc' < 'def'

    def test_message(self):
        assert 123+z < xxx+z, 'This is wrong!'
        assert 123 < xxx+z, 'This is wrong!'
