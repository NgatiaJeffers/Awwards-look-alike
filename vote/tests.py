from vote.views import profile
from django.test import TestCase
from .models import Profile, Projects, Comments, Votes

# Create your tests here.
class ProfileTestCase(TestCase):
    # SetUp Method
    def setUp(self):
        self.dev = Profile(image = "https://res.cloudinary.com/devgallery/image/upload/v1617715345/h5szydfcbge2exhgdxxk.jpg", user = "John Doe", bio = "I love coding")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.dev, Profile))

    # Testing Save Method
    def test_save_method(self):
        self.dev.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)