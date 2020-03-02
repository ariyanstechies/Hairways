from django.test import TestCase
from django.test.client import Client


class IsBotTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_i_am_a_bot(self):
        """
        Test by setting HTTP_USER_AGENT to Googlebot/2.1
        """
        user_agent = "Googlebot/2.1"
        response = self.client.get("/", **{"HTTP_USER_AGENT": user_agent, "REMOTE_ADDR": "127.0.0.1"})
        self.assertTrue(response.context["request"].META.get("IS_BOT"))

    def test_i_am_a_normal_user(self):
        """
        Test by setting HTTP_USER_AGENT to Mozilla/5.0
        """
        user_agent = "Mozilla/5.0"
        response = self.client.get("/", **{"HTTP_USER_AGENT": user_agent, "REMOTE_ADDR": "127.0.0.1"})
        self.assertFalse(response.context["request"].META.get("IS_BOT"))
