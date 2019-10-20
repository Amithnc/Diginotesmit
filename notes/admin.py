from django.contrib import admin
from .models import Note
admin.site.register(Note)
admin.site.index_title="add notes"
admin.site.site_title="notes@mit"
admin.site.site_header="notes administration"




