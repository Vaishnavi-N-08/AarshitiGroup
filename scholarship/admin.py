from django.contrib import admin
from scholarship.models import Scholar,counselor

class ScholarModelAdmin(admin.ModelAdmin):
    model = Scholar
    list_display = [
        'fullname',
        'email',
        'secemail',
        'number',
        'address',
        'collegename',
        'grno',
        'marksheet',
        'feereceipt']


admin.site.register(Scholar, ScholarModelAdmin)

class counselorModelAdmin(admin.ModelAdmin):
    model = counselor
    list_display = [
        'email',
        'fullname',
        'course',
        'number'
       ]

admin.site.register(counselor, counselorModelAdmin)