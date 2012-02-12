from dss.recommendations.models import Recommendation
from django.contrib import admin

class RecommendationAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Recommendation', {'fields': ['recommendation']}),
    ]
    search_fields = ['recommendation']

admin.site.register(Recommendation, RecommendationAdmin)
