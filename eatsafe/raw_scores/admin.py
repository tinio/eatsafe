from django.contrib import admin

from raw_scores.models import RawScore

class RawScoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'inspect_date')
    search_fields = ('name',)

admin.site.register(RawScore, RawScoreAdmin)
