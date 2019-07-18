from django.test import TestCase
from blog.models import PostModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from blog.forms import PostModelForm
from django.utils import timezone
# Create your tests here.


class PostFormTestCase(TestCase):
    # setUp create a fictive record

    def test_form(self):
        title = 'As h'
        content = 'as ad'
        # obj = PostModel.objects.create(title=title, publish=timezone.now(), content=content)

        form = PostModelForm(data={'title':title, 'content':content}) #PostModelForm(request.POST)
        form.save()
        self.assertTrue(form.is_valid())
        PostModel.objects.get(title=form.cleaned_data.get('title'))
        self.assertEqual(form.cleaned_data.get('title'), title)
        self.assertNotEqual(form.cleaned_data.get('content'), "Another content")
