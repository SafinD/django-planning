from django.contrib import admin

# Register your models here.
from .models import Adherent
admin.site.register(Adherent)

from .models import Entraineur
admin.site.register(Entraineur)

from .models import Coach
admin.site.register(Coach)

from .models import Role
admin.site.register(Role)

from .models import Entrainement
admin.site.register(Entrainement)

