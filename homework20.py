import unittest
from homework19 import new_contact, search_con, app, phonebook


class TestPhonebook(unittest.TestCase):
    def test_dict(self):
        test_dict = new_contact("A", "B", "12345", "C")
        expected_dict = {
            "first_name": "A",
            "last_name": "B",
            "full_name": "A" + " " + "B",
            "number": "12345",
            "city": "C"
        }
        self.assertEqual(test_dict, expected_dict)

    def test_book(self):
        exd_first_name = 'A'
        exd_last_name = 'B'
        exd_full_name = 'A' + ' ' + 'B'
        exd_phone = 12345
        exd_city = 'C'

        test_phone = new_contact(exd_first_name, exd_last_name, exd_phone,
                                 exd_city)
        self.assertEqual(test_phone["first_name"], exd_first_name)
        self.assertEqual(test_phone["last_name"], exd_last_name)
        self.assertEqual(test_phone["full_name"], exd_full_name)
        self.assertEqual(test_phone["number"], exd_phone)
        self.assertEqual(test_phone["city"], exd_city)

    def test_search(self):
        test_arg = search_con("B", "last_name", phonebook)
        test_info = {
            "first_name": "A",
            "last_name": "B",
            "full_name": "A" + " " + "B",
            "number": "12345",
            "city": "C"
        }
        app(test_info, phonebook)

        self.assertEqual(test_arg, test_info)


if __name__ == '__main__':
    unittest.main()

    #print(user_info["first_name"])