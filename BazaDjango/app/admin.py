from django.contrib import admin

# Register your models here.



from .models import icecream
admin.site.register(icecream)
from .models import iceshop
admin.site.register(iceshop)

from .models import Children
admin.site.register(Children)
from .models import Parent
admin.site.register(Parent)
