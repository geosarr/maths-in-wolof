import unittest
from limal import *


class TestLimal(unittest.TestCase):
    def test_limal(self):
        self.assertEqual(limal(23), "ñaar-fukk-ak-ñatt")
        self.assertEqual(limal(32), "fanweer-ak-ñaar")
        self.assertEqual(limal(39), "fanweer-ak-juròom-ñeent")
        self.assertEqual(limal(81), "juròom-ñatt-fukk-ak-been")
        self.assertEqual(limal(131), "téeméer-ak-fanweer-ak-been")
        self.assertEqual(limal(264), "ñaar-téeméer-ak-juròom-been-fukk-ak-ñeent")
        self.assertEqual(limal(618), "juròom-been-téeméer-ak-fukk-ak-juròom-ñatt")
        self.assertEqual(limal(1073), "junni-ak-juròom-ñaar-fukk-ak-ñatt")
        self.assertEqual(limal(100000), "téeméer-junni")
        self.assertEqual(
            limal(20456),
            "ñaar-fukk-junni-ak-ñeent-téeméer-ak-juròom-fukk-ak-juròom-been",
        )
        self.assertEqual(
            limal(987000),
            "juròom-ñeent-téeméer-ak-juròom-ñatt-fukk-ak-juròom-ñaar-junni",
        )
        self.assertEqual(limal(1000006), "milliong-ak-juròom-been")
        self.assertEqual(
            limal(283496736),
            "ñaar-téeméer-ak-juròom-ñatt-fukk-ak-ñatt-milliong-ak-ñeent-téeméer-ak-juròom-ñeent-fukk-ak-juròom-been-junni-ak-juròom-ñaar-téeméer-ak-fanweer-ak-juròom-been",
        )


if __name__ == "__main__":
    unittest.main()
