import unittest
from limal import *


class TestLimal(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_limal(self):
        self.assertEqual(limal(23), "ñaar-fukk-ak-ñatt")
        self.assertEqual(limal(32), "fanweer-ak-ñaar")
        self.assertEqual(limal(39), "fanweer-ak-juròom-ñeent")
        self.assertEqual(limal(81), "juròom-ñatt-fukk-ak-been")
        self.assertEqual(limal(131), "téeméer-ak-fanweer-ak-been")
        self.assertEqual(limal(264), "ñaar-téeméer-ak-juròom-been-fukk-ak-ñeent")
        self.assertEqual(limal(618), "juròom-been-téeméer-ak-fukk-ak-juròom-ñatt")
        self.assertEqual(limal(1073), "junni-ak-juròom-ñaar-fukk-ak-ñatt")
        self.assertEqual(
            limal(20456),
            "ñaar-fukk-junni-ak-ñeent-téeméer-ak-juròom-fukk-ak-juròom-been",
        )
        # self.assertEqual(limal(987652), "junni-ak-juròom-ñaar-fukk-ak-ñatt")

    def test_been_beenu(self):
        self.assertEqual(been_beenu(0), "")
        self.assertEqual(been_beenu(3), "-ak-ñatt")
        with self.assertRaises(AssertionError):
            been_beenu(10)

    def test_fukk_fukku(self):
        self.assertEqual(fukk_fukku(1), "fukk")
        self.assertEqual(fukk_fukku(3), "fanweer")
        self.assertEqual(fukk_fukku(5), "juròom-fukk")
        with self.assertRaises(AssertionError):
            fukk_fukku(0)


if __name__ == "__main__":
    unittest.main()
