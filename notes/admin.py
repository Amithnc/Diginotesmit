from django.contrib import admin
from .models import Note
admin.site.index_title="add notes"
admin.site.site_title="notes@mit"
admin.site.site_header="notes administration"

class NoteAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)
admin.site.register(Note,NoteAdmin)



