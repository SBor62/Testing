import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 3), 1)  # 10 % 3 = 1
        self.assertEqual(remainder(8, 4), 0)   # 8 % 4 = 0
        self.assertEqual(remainder(15, 4), 3) # 15 % 4 = 3

    def test_remainder_by_zero(self):
        # Проверяем, что при делении на 0 вызывается ValueError
        self.assertRaises(ValueError, remainder, 10, 0)
        # Альтернативный вариант с контекстным менеджером
        with self.assertRaises(ValueError):
            remainder(5, 0)

if __name__ == '__main__':
    unittest.main()
