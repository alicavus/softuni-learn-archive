from project.gallery import Gallery
from unittest import TestCase, main

class GalleryTest(TestCase):
    def setUp(self):
        self.gallery = Gallery("MilenRouge", "Kardzhali", 120.0)
    
    def test_constructor_data(self):
        self.assertEqual("MilenRouge", self.gallery._Gallery__gallery_name)
        self.assertEqual("Kardzhali", self.gallery._Gallery__city)
        self.assertEqual(120.0, self.gallery._Gallery__area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)
    
    def test_constructor_data_with_open_to_public_false(self):
        self.gallery = Gallery("MilenRouge", "Kardzhali", 120.0, False)
        self.assertEqual("MilenRouge", self.gallery._Gallery__gallery_name)
        self.assertEqual("Kardzhali", self.gallery._Gallery__city)
        self.assertEqual(120.0, self.gallery._Gallery__area_sq_m)
        self.assertFalse(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)
    
    def test_property_gallery_name(self):
        self.assertEqual(self.gallery.gallery_name, self.gallery._Gallery__gallery_name)
    
    def test_setter_gallery_name_ok(self):
        self.gallery.gallery_name = " Bonjour98 "
        self.assertEqual("Bonjour98", self.gallery._Gallery__gallery_name)
    
    def test_setter_gallery_name_empty(self):
        with self.assertRaises(ValueError) as ctx:
            self.gallery.gallery_name = ""
        self.assertEqual("Gallery name can contain letters and digits only!", ctx.exception.__str__())
    
    def test_setter_gallery_name_not_alnum(self):
        with self.assertRaises(ValueError) as ctx:
            self.gallery.gallery_name = "$Test"
        self.assertEqual("Gallery name can contain letters and digits only!", ctx.exception.__str__())
    
    def test_property_city(self):
        self.assertEqual(self.gallery.city, self.gallery._Gallery__city)
    
    def test_setter_city_ok(self):
        self.gallery.city = "Iva8lo$gra bourg"
        self.assertEqual(self.gallery.city, self.gallery._Gallery__city)
    
    def test_setter_city_empty_or_none(self):
        with self.assertRaises(ValueError) as ctx:
            self.gallery.city = ""
        self.assertEqual("City name must start with a letter!", ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.gallery.city = None
        self.assertEqual("City name must start with a letter!", ctx.exception.__str__())
    
    def test_setter_city_starts_nonalpha(self):
        with self.assertRaises(ValueError) as ctx:
            self.gallery.city = "$offia Loren"
        self.assertEqual("City name must start with a letter!", ctx.exception.__str__())
    
    def test_property_area_sq_m(self):
        self.assertEqual(self.gallery.area_sq_m, self.gallery._Gallery__area_sq_m)
    
    def test_setter_area_sq_m_ok(self):
        self.gallery.area_sq_m = 0.7
        self.assertEqual( 0.7, self.gallery._Gallery__area_sq_m)
    
    def test_setter_area_sq_m_zero_or_negative(self):
        with self.assertRaises(ValueError) as ctx:
            self.gallery.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.gallery.area_sq_m = -0.1
        self.assertEqual("Gallery area must be a positive number!", ctx.exception.__str__())
    
    def test_add_exhibition_ok(self):
        result = self.gallery.add_exhibition("Loopable If", 2025)
        self.assertEqual({"Loopable If": 2025}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "Loopable If" added for the year 2025.', result)
    
    def test_add_exhibition_exists(self):
        self.gallery.add_exhibition("Ines and her Loopable If", 2025)
        result = self.gallery.add_exhibition("Ines and her Loopable If", 2020)
        expected_result = 'Exhibition "Ines and her Loopable If" already exists.'
        self.assertEqual(expected_result, result)
    
    def test_remove_exhibition_ok(self):
        self.gallery.add_exhibition("Loopable If", 2025)
        self.gallery.add_exhibition("Аксесева Велюту", 1999)
        result = self.gallery.remove_exhibition("Loopable If")
        expected = 'Exhibition "Loopable If" removed.'
        self.assertEqual({"Аксесева Велюту": 1999}, self.gallery.exhibitions)
        self.assertEqual(expected, result)
    
    def test_remove_exhibition_unexistent(self):
        self.gallery.add_exhibition("Loopable If", 2025)
        result = self.gallery.remove_exhibition("Аксесева Велюту")
        expected = 'Exhibition "Аксесева Велюту" not found.'
        self.assertEqual(expected, result)
    
    def test_list_exhibitions_closed(self):
        self.gallery = Gallery("MilenRouge", "Kardzhali", 120.0, False)
        result = self.gallery.list_exhibitions()
        expected = "Gallery MilenRouge is currently closed for public! Check for updates later on."
        self.assertEqual(expected, result)
    
    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("Loopable If", 2025)
        self.gallery.add_exhibition("Аксесева Велюту", 1999)
        self.gallery.add_exhibition("Search on Google for roman numerals", 2020)
        self.gallery.add_exhibition("Ask DeepSeek", 2057)
        result = self.gallery.list_exhibitions()
        expected = "Loopable If: 2025\nАксесева Велюту: 1999\nSearch on Google for roman numerals: 2020\nAsk DeepSeek: 2057"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()