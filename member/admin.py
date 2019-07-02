from django.contrib import admin
from .models import Member,MemberAssigment

# Register your models here.
# admin.site.register(Comment)
admin.site.register(Member)
admin.site.register(MemberAssigment)



#@admin.register(Member)
#class MemberAdmin(admin.ModelAdmin):
#   list_display = [ "gender", "created_date","birthday"]
#    list_filter = ["gender"]

#    class Meta:
#        model = Member