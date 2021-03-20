import unittest
from classy import Classy
from show_excitement import show_excitement
from manatees import example1, example2, example3, example4


class ClassyTests(unittest.TestCase):
    def setUp(self):
        self.me = Classy()

    def test_get_classiness_equal_zero(self):
        self.assertEqual(0, self.me.getClassiness())

    def test_add_item_tophat(self):
        self.me.addItem("tophat")
        self.assertEqual(2, self.me.getClassiness())

    def test_add_more_three_items(self):
        self.me.addItem("tophat")
        self.me.addItem("bowtie")
        self.me.addItem("jacket")
        self.me.addItem("monocle")
        self.assertEqual(11, self.me.getClassiness())

    def test_add_more_item(self):
        self.me.addItem("tophat")
        self.me.addItem("bowtie")
        self.me.addItem("jacket")
        self.me.addItem("monocle")
        self.me.addItem("bowtie")
        self.assertEqual(15, self.me.getClassiness())

    def test_add_item_no_fancy(self):
        self.me.addItem("tophat")
        self.me.addItem("bowtie")
        self.me.addItem("jacket")
        self.me.addItem("monocle")
        self.me.addItem("bowtie")
        self.me.addItem("cap")
        self.assertEqual(15, self.me.getClassiness())


class ShowExcitementTests(unittest.TestCase):
    def test_return_five_time(self):
        self.string_expected = 'I am super excited for this course! '
        self.assertEqual(self.string_expected * 5, show_excitement())


class ManateesTests(unittest.TestCase):
    def setUp(self):
        self.manatees = [{"name": "Fulano", "age": 10}, {"name": "Beltrano", "age": 20}]

    def test_example1(self):
        expect_test = "Beltrano\nFulano\n"
        expect_function = example1(self.manatees)
        self.assertEqual(expect_test, expect_function)

    def test_example2(self):
        expect_test = "Fulano\n10"
        expect_function = example2(self.manatees)
        self.assertEqual(expect_test, expect_function)

    def test_example4(self):
        expect_function = example4(self.manatees)
        self.assertEqual("Beltrano", expect_function)


if __name__ == '__main__':
    unittest.main()
