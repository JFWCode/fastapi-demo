from unittest import TestCase

from auth import get_user


class Test(TestCase):
    def test_get_user(self):
        try:
            get_user(12, '...').send(None)
        except StopIteration as e:
            print(e.value)
