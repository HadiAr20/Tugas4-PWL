import unittest
from pyramid import testing
from setup import login, logout

class test(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
    def tearDown(self):
        testing.tearDown()
    def LoginTest(self):
        request=testing.DummyRequest(post={'login':'12345','password':'12345'})
        res=login(request)
        self.assertEqual(res['greet'], 'ok')
        self.assertIn('token', res)
    def LogoutTest(self):
        request=testing.DummyRequest(cookies={'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjIsIm5hbWUiOiIxMjM0NSIsImV4cCI6MTY5Nzk5NjkxMn0.EiXl-QTmYP4eRLNLYMb1XFVqbfLbSnJjpeSCxx7aUN4'})
        res=logout(request)
        self.assertEqual(res['greet'], 'ok')
        self.assertEqual(res['messages'], 'Successfully logged out')
if __name__ == '__main__':
    unittest.main()