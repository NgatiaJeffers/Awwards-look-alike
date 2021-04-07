from django.test import TestCase
from .models import Projects, Profile, Votes
from django.contrib.auth.models import User

# Create your tests here
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'janedoe' ,email = 'janedoe@gmail.com', password = 'abcdef')
        self.profile = Profile(image = '/path/jefflogo.svg', user = self.user, bio ='Talk is cheap, show me the code',)
        
        
    def test_save_profile(self):
        self.user.save()
        self.profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_profile(self):
        self.user.save()
        self.profile.save()
        self.profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        
    def test_get_profile_id(self):
        self.user.save()
        self.profile.save()
        # self.profile.profile_id(self.profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


class ProjectsTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    # Set up method
    def setUp(self):
        self.user = User(username = 'John Doe', email = 'johndoe@gmail.com', password = '123456')
        self.profile = Profile(image = '/path/jefflogo.svg' ,user = self.user, bio = "I love coding")
        self.project = Projects(name = 'Testing', image = '/path/jefflogo.svg', description = 'Project one', link = '/path/jefflogo.svg')

    # Testing Save Method
    def test_save_project(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)
    
    def test_search_project(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        
        projects = self.project.search_by_project('Testing')
        self.assertTrue(len(projects) > 0)

    def test_get_project_id(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        self.project.get_project_id(self.project.id)
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)
    
    def test_delete_project(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        self.project.delete_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) == 0)
        

class VotesTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'John Doe', email = 'johndoe@gmail.com', password = '123456')
        self.profile = Profile(image = '/path/jefflogo.svg' ,user = self.user, bio = "I love coding")
        self.project = Projects(name = 'Testing', image = '/path/jefflogo.svg', description = 'Project one', link = '/path/jefflogo.svg')
        self.vote = Votes(design = '7', usability = '7', content = '6', user=self.user, project = '8')
        
    def test_save_vote(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        self.vote.save_review()
        vote = Votes.objects.all()
        self.assertTrue(len(vote) > 0)