from dss.recommendations.models import Recommendation, RecommendationProfile
from django.contrib import admin


class RecommendationProfileInline(admin.TabularInline):
    model = RecommendationProfile
    extra = 0
    fieldsets = [
        (RecommendationProfile, {
            'fields': ('recommendation', 'profile',)
        })
    ]

class RecommendationAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Recommendation', {'fields': ['recommendation']}),
    ]
    inlines = [RecommendationProfileInline] 
    search_fields = ['recommendation']


admin.site.register(Recommendation, RecommendationAdmin)
