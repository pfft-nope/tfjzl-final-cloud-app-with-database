from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)

# Inline for Lesson inside Course
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


# Inline for Question inside Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Admin for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]


# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)