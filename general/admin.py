from django.contrib import admin
from general.models import Feedback

class FeedbackModelAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [
        'fullname'
       ]

admin.site.register(Feedback, FeedbackModelAdmin)