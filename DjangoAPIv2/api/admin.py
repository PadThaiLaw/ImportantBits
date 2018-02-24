from django.contrib import admin
from .models import Decision, Citation, Paragraph

# Register your models here.
admin.site.register(Decision)
admin.site.register(Citation)
admin.site.register(Paragraph)