from django.test import TestCase
from blog.models import PostModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# Create your tests here.


class ViewTestCase(TestCase):
    def create_post(self, title=None):
        return PostModel.objects.create(title=title)

    # TEST DETAIL
    def test_detail_view(self):
        obj = self.create_post(title="Another new title test")
        edit_url = reverse('detail', kwargs={'id':obj.id}) # pattern name
        print(edit_url) # /blog/1/
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)

    # TEST EDIT
    def test_edit_view(self):
        obj = self.create_post(title="Another new title test")
        edit_url = reverse('update', kwargs={'id':obj.id}) # pattern name
        print(edit_url) # /blog/1/edit/
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)

    # TEST DELETE
    def test_delete_view(self):
        obj = self.create_post(title="Another new title test")
        edit_url = reverse('delete', kwargs={'id':obj.id}) # pattern name
        print(edit_url) # /blog/1/edit/
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)

    # TEST LIST VIEW (NOT NECESSARY)
    def test_list_view(self):
        edit_url = reverse('list1') # pattern name
        print(edit_url) # /blog/1/edit/
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
