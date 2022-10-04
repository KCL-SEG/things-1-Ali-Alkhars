from django.forms import ValidationError
from django.test import TestCase
from things.models import Thing

class ThingModelTestCase(TestCase):
    def test_thing_can_be_created(self):
        thing = Thing(name='Key', description='used to open doors', quantity=1)

        try:
            thing.full_clean()
        except(ValidationError):
            self.fail("Cannot create user")
