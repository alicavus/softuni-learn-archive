from project.restaurant import Restaurant
from unittest import main, TestCase

class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Efsanenin Yeri", 15)

    def test_constructor_data(self):
        self.assertEqual("Efsanenin Yeri", self.restaurant._Restaurant__name)
        self.assertEqual(15, self.restaurant._Restaurant__capacity)
        self.assertEqual([], self.restaurant.waiters)

        self.assertIsInstance(self.restaurant._Restaurant__name, str)
        self.assertIsInstance(self.restaurant._Restaurant__capacity, int)
        self.assertIsInstance(self.restaurant.waiters, list)

    def test_properties(self):
        self.assertEqual(self.restaurant.name, self.restaurant._Restaurant__name)
        self.assertEqual(self.restaurant.capacity, self.restaurant._Restaurant__capacity)

    def test_name_setter_wrong_name(self):
        for wrong_name in ["               ", None, ""]:
            with self.assertRaises(ValueError) as ctx:
                self.restaurant.name = wrong_name
            self.assertEqual("Invalid name!", ctx.exception.__str__())

    def test_name_setter_valid_name(self):
        for valid_name in ["       Johnny         ", "Nusret", "    Кръстопът"]:
            self.restaurant.name = valid_name
            self.assertEqual(valid_name, self.restaurant._Restaurant__name)
            self.assertIsInstance(self.restaurant._Restaurant__name, str)

    def test_capacity_setter_invalid_capacity(self):
        for invalid_capacity in [-45, -3, -1]:
            with self.assertRaises(ValueError) as ctx:
                self.restaurant.capacity = invalid_capacity
            self.assertEqual("Invalid capacity!", str(ctx.exception))

    def test_capacity_setter_valid_capacity(self):
        for valid_capacity in [0, 45, 3, 7]:
            self.restaurant.capacity = valid_capacity
            self.assertEqual(valid_capacity, self.restaurant._Restaurant__capacity)
            self.assertIsInstance(self.restaurant._Restaurant__capacity, int)

    def test_get_waiters(self):
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]
        self.restaurant.waiters = [waiter for waiter in waiters]
        self.assertEqual(waiters, self.restaurant.get_waiters())
        self.assertEqual([ {
                "name": "Mark",
                "total_earnings": 375.00
            }], self.restaurant.get_waiters(300))
        self.assertEqual([ {
                "name": "Jane",
                "total_earnings": 175.00
            }], self.restaurant.get_waiters(100, 200))
        self.assertEqual([ {
                "name": "Beth"
            }], self.restaurant.get_waiters(None, 0))
        self.assertEqual([], self.restaurant.get_waiters(1000, 200))

    def test_add_waiter_no_capacity(self):
        self.restaurant.capacity = 0
        self.assertEqual("No more places!", self.restaurant.add_waiter("Beth"))

    def test_add_waiter_existing_waiter(self):
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]
        self.restaurant.waiters = [waiter for waiter in waiters]

        for waiter in waiters:
            self.assertEqual(f"The waiter {waiter['name']} already exists!", self.restaurant.add_waiter(waiter["name"]))

        self.assertEqual(waiters, self.restaurant.waiters)

    def test_add_waiter_non_existing_waiter(self):
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]
        self.restaurant.waiters = [waiter for waiter in waiters]
        result = self.restaurant.add_waiter("Ben")
        self.assertEqual(f"The waiter Ben has been added.", result)
        waiters.append({"name": "Ben"})
        self.assertEqual(waiters, self.restaurant.waiters)

    def test_remove_waiter_nonexistent_waiter(self):
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]
        self.restaurant.waiters = [waiter for waiter in waiters]
        self.assertEqual(f"No waiter found with the name Gilly.", self.restaurant.remove_waiter("Gilly"))
        self.assertEqual(waiters, self.restaurant.waiters)

    def test_remove_waiter_existent_waiter(self):
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]

        for waiter in waiters:
            waiters_copy = [waiter for waiter in waiters]
            self.restaurant.waiters = [waiter for waiter in waiters]
            self.assertEqual(f"The waiter {waiter['name']} has been removed.", self.restaurant.remove_waiter(waiter["name"]))
            waiters_copy.remove(next(w for w in waiters if w["name"] == waiter["name"]))
            self.assertEqual(waiters_copy, self.restaurant.waiters)

    def test_get_total_earnings(self):
        self.assertEqual(0, self.restaurant.get_total_earnings())
        waiters = [
            {
                "name": "Jane",
                "total_earnings": 175.00
            },
            {
                "name": "Mark",
                "total_earnings": 375.00
            },
            {
                "name": "Vasil",
                "total_earnings": 75.77
            },
            {
                "name": "Beth"
            }
        ]
        self.restaurant.waiters = [waiter for waiter in waiters]
        self.assertEqual(625.77, self.restaurant.get_total_earnings())






if __name__ == "__main__":
    main()