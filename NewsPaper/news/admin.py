from django.contrib import admin
from news.models import *


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)