
import pytest

def deco(f):
  print("before myfunc() called.")
  f()
  print("after myfunc() called.")
  return f

@deco
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')




if __name__ == '__main__':
    pytest.main("-q --html=a.html")