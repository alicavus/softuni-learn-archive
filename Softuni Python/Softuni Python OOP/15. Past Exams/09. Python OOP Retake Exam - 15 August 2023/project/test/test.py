from project.trip import Trip
from unittest import main, TestCase

class TestTripClass(TestCase):
    def setUp(self):
        self.destinations = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}
        self.solo = Trip(10_000.0, 7, False)
        self.family = Trip(7_000.0, 4, True)

    def test_initialisation(self):
        self.assertEqual(10_000.0, self.solo.budget)
        self.assertEqual(7_000.0, self.family.budget)
        self.assertEqual(7, self.solo.travelers)
        self.assertEqual(4, self.family.travelers)
        self.assertFalse(self.solo.is_family)
        self.assertTrue(self.family.is_family)
        self.assertFalse(self.solo.booked_destinations_paid_amounts)
        self.assertFalse(self.family.booked_destinations_paid_amounts)

        self.assertIsInstance(self.solo.budget, float)
        self.assertIsInstance(self.family.budget, float)
        self.assertIsInstance(self.solo.travelers, int)
        self.assertIsInstance(self.family.travelers, int)
        self.assertIsInstance(self.solo.is_family, bool)
        self.assertIsInstance(self.family.is_family, bool)
        self.assertIsInstance(self.solo.booked_destinations_paid_amounts, dict)
        self.assertIsInstance(self.family.booked_destinations_paid_amounts, dict)

    def test_travelers_setter_zero_or_negative_count(self):
        for cnt in -2, -1, 0:
            for obj in self.solo, self.family:
                with self.assertRaises(ValueError) as ctx:
                    obj.travelers = cnt
                self.assertEqual('At least one traveler is required!', ctx.exception.args[0])

    def  test_travelers_setter_valid_count(self):
        for cnt in 1, 7, 15:
            for obj in self.solo, self.family:
                obj.travelers = cnt
                self.assertEqual(cnt, obj.travelers)

    def test_is_family_setter_one_traveler(self):
        self.solo.travelers = 1
        self.family.travelers = 1
        for is_family in [True, False]:
            traveler = Trip(7_000.0, 1, is_family)
            self.assertFalse(traveler.is_family)

            for obj in self.solo, self.family:
                obj.is_family = is_family
                self.assertFalse(obj.is_family)

    def test_is_family_setter_more_than_one_traveler(self):
        for obj in self.solo, self.family:
            for is_family in [True, False]:
                obj.is_family = is_family
                self.assertEqual(is_family, obj.is_family)

    def test_book_a_trip_wrong_destination(self):
        for dest in (f"Destination {n}" for n in range(1, 10)):
            for obj in self.solo, self.family:
                result = obj.book_a_trip(dest)
                self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_not_enough_budget(self):
        for dest in self.destinations:
            self.solo.budget = self.destinations[dest] * self.solo.travelers - 0.01
            self.family.budget =  self.destinations[dest] * self.family.travelers * 0.9 - 0.01

            result_solo = self.solo.book_a_trip(dest)
            result_family = self.family.book_a_trip(dest)
            expected = 'Your budget is not enough!'
            self.assertEqual(expected, result_solo)
            self.assertEqual(expected, result_family)
            for obj in self.solo, self.family:
                self.assertNotIn(dest, obj.booked_destinations_paid_amounts)

    def test_book_a_trip_enough_budget(self):
        for money_left in 0, 0.01, 5.1, 1000, 7000:
            for dest in self.destinations:
                self.solo.budget = self.destinations[dest] * self.solo.travelers + money_left
                self.family.budget =  self.destinations[dest] * self.family.travelers * 0.9 + money_left
                result_solo = self.solo.book_a_trip(dest)
                result_family = self.family.book_a_trip(dest)
                expected = f'Successfully booked destination {dest}! Your budget left is {money_left:.2f}'
                self.assertEqual(expected, result_solo)
                self.assertEqual(expected, result_family)
                for obj in self.solo, self.family:
                    self.assertIn(dest, obj.booked_destinations_paid_amounts)

    def test_booking_status_no_bookings(self):
        for obj in self.solo, self.family:
            self.assertEqual(f'No bookings yet. Budget: {obj.budget:.2f}', obj.booking_status())

    def test_booking_status_with_bookings(self):
        for obj in self.solo, self.family:
            destinations = {dest:self.destinations[dest] * obj.travelers for dest in sorted(self.destinations.keys())}
            obj.booked_destinations_paid_amounts = {k:v for k, v in destinations.items()}
            result = [f"Booked Destination: {k}\nPaid Amount: {v:.2f}" for k, v in destinations.items()]
            result.append(f"Number of Travelers: {obj.travelers}\nBudget Left: {obj.budget:.2f}")
            self.assertEqual("\n".join(result), obj.booking_status())




if __name__ == "__main__":
    main()