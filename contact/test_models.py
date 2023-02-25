from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Contact


class TestContactModel(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name='Test name',
            email='Test email',
            message='Test message'
        )

    def test_post_name(self):
        testname = get_object_or_404(Contact, name="Test name")

        self.assertEqual(self.contact.created_on, testname.created_on)

    def test_post_email(self):
        testemail = get_object_or_404(Contact, email="Test email")

        self.assertEqual(self.contact.created_on, testemail.created_on)

    def test_post_message(self):
        testmessage = get_object_or_404(Contact, message="Test mesaage")

        self.assertEqual(self.contact.created_on, testmessage.created_on)
