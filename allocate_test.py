import unittest
import random


class MyTestCase(unittest.TestCase):
    def test_allocate(self):
        new_list = [0.9, 0.1]

        result = random.choices(
            population=[{'id': 1, 'speed': 7}, {'id': 2, 'speed': 3}],
            weights=new_list,
            k=10
        )
        counter = 0
        for fast_elev in result:
            if fast_elev.id == 1:
                counter = counter + 1

        if counter > 5:
            self.assertTrue(self, True, "fast elev shows up more")


if __name__ == '__main__':
    unittest.main()
