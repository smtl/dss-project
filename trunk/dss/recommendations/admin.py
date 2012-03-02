from dss.recommendations.models import Recommendation, RecommendationProfile, MultipleFacts
from dss.recommendations.models import UploadedFile
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


class UploadedFileAdmin(admin.ModelAdmin):
    fieldsets = [
       ("UploadedFile", {"fields": ["files"]}),
    ]
    search_fields = ["files"]


class MultipleFactsInline(admin.TabularInline):
    model = RecommendationProfile
    extra = 0
    fieldsets = [
        (RecommendationProfile, {
            'fields': ('recommendation', 'profile',)
        })
    ]


class MultipleFilesAdmin(admin.ModelAdmin):
    fieldsets = [
       ("Multiple Fact", {"fields": ["recommendation"]}),
    ]
    search_fields = ["recommendation"]


admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)

