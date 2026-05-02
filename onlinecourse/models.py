from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course_images/', blank=True)
    description = models.TextField()
    pub_date = models.DateField()
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"


# ======================
# EXAM MODELS
# ======================

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    grade = models.IntegerField(default=1)

    def is_get_score(self, selected_ids):
        correct_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(
            is_correct=True,
            id__in=selected_ids
        ).count()
        return correct_answers == selected_correct

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return str(self.enrollment)