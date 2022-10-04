from django.forms import ValidationError
from django.test import TestCase
from things.models import Thing

class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing = Thing(name='Key', description='used to open doors', quantity=1)

    def test_thing_can_be_created(self):
        self._assert_thing_is_valid()
    
    def test_accepted_zero_quantity(self):
        self.thing.quantity = 0
        self._assert_thing_is_valid()

    def test_accepted_hundred_quantity(self):
        self.thing.quantity = 100
        self._assert_thing_is_valid()
    
    def test_cannot_create_negative_quantity(self):
        self.thing.quantity = -1
        self._assert_thing_is_invalid()
    
    def test_cannot_create_above_hundred_quantity(self):
        self.thing.quantity = 101
        self._assert_thing_is_invalid()
    
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except(ValidationError):
            self.fail("Cannot create user")
    
    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
