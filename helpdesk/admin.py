from django.contrib import admin

"""from .models import Choice, Question

# Here you can modify the form
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [ (group_name, {fields:[@fields]})]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

"""

from .models import Pdi, Pas, Student, Department, Topic, Comment, Subject


admin.site.register(Pdi)
admin.site.register(Pas)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Subject)
