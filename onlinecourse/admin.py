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

# Inline editing for Lesson within Course
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


# Inline editing for Question within Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Inline editing for Choice within Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Admin configuration for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]


# Admin configuration for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)