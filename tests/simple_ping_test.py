import pytest

class TestClass:
  def inc(self, x):
    return x + 1

  def test_answer(self):
    print('test')
    assert self.inc(3) == 4

