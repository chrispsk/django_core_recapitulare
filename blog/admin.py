from django.contrib import admin
from .models import PostModel
from django.utils.translation import gettext as _

admin.site.register(PostModel)
