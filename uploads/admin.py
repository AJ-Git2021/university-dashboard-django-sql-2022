from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin
from .models import *

# from .models import Task
class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["name", "description"]


class StudentAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ["sap", "student_name", "course_number"]


class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["course_number", "course_name", "course_duration"]


class SubjectsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["subject_number", "subject_name", "credits"]


class QuestionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["qp", "question_no", "co", "so", "bl", "marks"]


class AnswerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["sap", "qp", "answer", "question_no"]


class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ["qp_id", "total_marks"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionPaper, QuestionPaperAdmin)

admin.site.register(Task, TaskAdmin)
