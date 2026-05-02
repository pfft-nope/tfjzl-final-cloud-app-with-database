from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Course pages
    path('', views.CourseListView.as_view(), name='index'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enrollment
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Authentication
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('registration/', views.registration_request, name='registration'),

    # ✅ REQUIRED EXAM ROUTES
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]