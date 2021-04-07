from django.test import TestCase
from .models import Projects, Profile, Comments
from django.contrib.auth.models import User


class ProjectTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    def setUp(self):
        self.user_one = User(username = 'John Doe', email = 'johndoe@gmail.com', password = '123456')
        self.profile_one = Profile(image = '/path/jefflogo.svg' ,user = self.user_one, bio = "I love coding")
        self.project_one = Projects(name = 'GithubSearch', description = 'Project one', link = '/path/jefflogo.svg', profile_one = self.user_one)
        
        
    def test_save_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()
        
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)
    
    def test_search_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()
        
        projects = self.project_one.search_by_project('GithubSearch')
        self.assertTrue(len(projects) > 0)
    def test_get_project_id(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_proj_id(self.project_one.id)
        projects = Projects.objects.all()
        self.assertTrue(len(projects)> 0)
        
    def test_update_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_proj_id(self.project_one.id)
        self.project_one.update_project('GithubSearchAPI')
        self.assertTrue(self.project_one.project_title=='GithubSearchAPI')
    
    def test_delete_project(self):
        self.user_one.save()
        self.profile_one.save_profile()
        self.project_one.save_project()
        self.project_one.delete_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)== 0)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user_john = User(username = 'janedoe' ,email = 'janedoe@gmail.com', password = 'abcdef')
        self.profile_two = Profile(image = '/path/jefflogo.svg', user=self.user_john, bio ='Talk is cheap, show me the code',)
        
        
    def test_save_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)
        
    def test_update_bio(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        self.profile_two.update_profile('This is an updated bio')
        self.assertTrue(self.profile_two.bio=='This is an updated bio')
        
    def test_get_profile_id(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        

class CommentsTestCase(TestCase):
    def setUp(self):
        self.user_one = User(username = 'John Doe', email = 'johndoe@gmail.com', password = '123456')
        self.profile_one = Profile(image = '/path/jefflogo.svg' ,user = self.user_one, bio = "I love coding")
        self.project_one = Projects(name = 'GithubSearch', description = 'Project one', link = '/path/jefflogo.svg', profile_one = self.user_one)
        self.review_one = Comments(design='1',usability='7',content='6',user=self.user_one, project = self.project_one)
        
    def test_save_review(self):
        self.user_jane.save()
        self.profile_jane.save()
        self.project_three.save()
        self.review_one.save_review()
        reviews = Comments.objects.all()
        self.assertTrue(len(reviews) > 0)