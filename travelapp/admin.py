from django.contrib import admin
from . models import Place
from . models import People
from . models import About_us
from . models import Footer

# Register your models here.
admin.site.register(Place)
admin.site.register(People)
admin.site.register(About_us)
admin.site.register(Footer)


