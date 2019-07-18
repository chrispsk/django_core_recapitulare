from django.test import TestCase
from blog.models import PostModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your tests here.


class PostModelTestCase(TestCase):
    # setUp create a fictive record
    def setUp(self):
        PostModel.objects.create(title='A new title', slug='some-prob-unique-slug-by-this-test')

    # Test based on that record
    def test_post_title(self):
        obj = PostModel.objects.get(slug='some-prob-unique-slug-by-this-test')
        self.assertEqual(obj.title, 'A new title')
        self.assertTrue(obj.content != "") # maybe I want to change

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'cristi123',
            'test@gmail.com',
            'pass1'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # TEST SLUG
    def create_post(self, title=None):
        return PostModel.objects.create(title=title)

    def test_post_slug(self):
        # Reminder: title is set as unique so slugify the same title won't work
        title1 = "titlu 1"
        title2 = "titlu 2"
        slug1 = slugify(title1)
        slug2 = slugify(title2)
        obj1 = self.create_post(title=title1)
        obj2 = self.create_post(title=title2)
        self.assertEqual(obj1.slug, slug1)
        self.assertEqual(obj2.slug, slug2)
