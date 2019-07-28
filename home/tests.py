from django.test import TestCase
from home.models import User, Owner, Salons


class UserTestCase(TestCase):
    """docstring for UserTestCase"""

    def setUp(self):
        user = User.objects.create(is_owner=True, nickname="Alexander")

    def test_user_was_created(self):
        """ Confirms that user was created as expected."""
        user = User.objects.get(nickname="Alexander")
        self.assertEqual(str(user.nickname), "Alexander")
