from collections import deque
from project.railway_station import RailwayStation
from unittest import main, TestCase

class TestRailwayStationClass(TestCase):
    def setUp(self):
        self.station = RailwayStation("Kardzhali Train Station")
    
    def test_initialisation(self):
        self.assertEqual("Kardzhali Train Station", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

        self.assertEqual(type(getattr(RailwayStation, "name", None)), property)
    
    def test_name_setter_invalid_name(self):
        for name in ["", "a", "ab", "abc"]:
            with self.assertRaises(ValueError) as ctx:
                self.station.name = name
            self.assertEqual("Name should be more than 3 symbols!", f"{ctx.exception!s}")
    
    def test_name_setter_valid_name(self):
        for name in ["Kardzhali Railway Station", "Podkova Station", "Station Name"]:
            self.station.name = name
            self.assertEqual(name, self.station.name)
    
    def test_new_arrival_on_board(self):
        for train_info in [f"Train {n}" for n in range(1, 10)]:
            self.station.new_arrival_on_board(train_info)
            self.assertIn(train_info, self.station.arrival_trains)
            if train_info in self.station.arrival_trains:
                self.assertEqual(train_info, self.station.arrival_trains[-1])
    
    def test_train_has_arrived_wrong_train(self):
        self.station.arrival_trains = deque(f"Train {n}" for n in range(1, 10))
        wrong_train_info = "Wrong Train"
        expected = f"There are other trains to arrive before {wrong_train_info}."
        result = self.station.train_has_arrived(wrong_train_info)
        self.assertEqual(expected, result)
        self.assertNotIn(wrong_train_info, self.station.departure_trains)
    
    def test_train_has_arrived_arrival_train(self):
        trains_info = [f"Train {n}" for n in range(1, 10)]
        self.station.arrival_trains = deque(train_info for train_info in trains_info)

        for train_info in trains_info:
            result = self.station.train_has_arrived(train_info)
            expected = f"{train_info} is on the platform and will leave in 5 minutes."
            self.assertEqual(expected, result)
            self.assertNotIn(train_info, self.station.arrival_trains)
            self.assertIn(train_info, self.station.departure_trains)
    
    def test_train_has_left_true(self):
        trains_info = [f"Train {n}" for n in range(1, 10)]
        self.station.departure_trains = deque(train_info for train_info in trains_info)

        for train_info in trains_info:
            result = self.station.train_has_left(train_info)
            self.assertTrue(result)
            self.assertNotIn(train_info, self.station.departure_trains)
    
    def test_train_has_left_false(self):
        result = self.station.train_has_left("Wrong Train to Left")
        self.assertFalse(result)

        trains_info = [f"Train {n}" for n in range(1, 10)]
        self.station.departure_trains = deque(train_info for train_info in trains_info)
        for train_info in trains_info[1:]:
            result = self.station.train_has_left(train_info)
            self.assertFalse(result)
            self.assertIn(train_info, self.station.departure_trains)
            result = self.station.train_has_left(train_info)
            
        self.assertFalse(self.station.train_has_left("Wrong Train to Left"))









if __name__ == "__main__":
    main()