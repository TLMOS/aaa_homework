import unittest
import json

from advert import Advert


class TestAdvert(unittest.TestCase):
    def test_empty_mapping(self):
        json_str = '{}'
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        self.assertEqual(advert.__dict__, {'_Advert__price': 0})

    def test_basic_field(self):
        json_str = '''{
            "title": "iPhone X",
            "price": 100
            }'''
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        self.assertEqual(advert.title, 'iPhone X')
        self.assertEqual(advert.price, 100)

    def test_nested_field(self):
        json_str = '''{
            "title": "iPhone X",
            "price": 100,
            "location": {
                "address": "город Самара",
                "metro_stations": ["Спортивная", "Гагаринская"]
                }
            }'''
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        self.assertEqual(advert.location.address, 'город Самара')

    def test_keyword_field(self):
        json_str = '''{
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs"
            }'''
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        self.assertEqual(advert.class_, 'dogs')

    def test_default_price(self):
        json_str = '''{
            "title": "iPhone X"
            }'''
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        self.assertEqual(advert.price, 0)

    def test_negative_price(self):
        json_str = '''{
            "title": "iPhone X",
            "price": -10
            }'''
        mapping = json.loads(json_str)
        with self.assertRaises(ValueError):
            Advert(mapping)

    def test_repr(self):
        json_str = '''{
            "title": "Вельш-корги",
            "price": 1000
            }'''
        mapping = json.loads(json_str)
        advert = Advert(mapping)
        advert.repr_color_code = 33
        self.assertEqual(advert.__repr__(), 'Вельш-корги | 1000 ₽')
        self.assertEqual(advert.__str__()[:7], '\033[0;33m')
        print('(Visual Test) Must be yellow: ', end='')
        print(advert)


if __name__ == '__main__':
    unittest.main()
