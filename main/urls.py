from django.urls import path
from main import views

# Define URL patterns for the main application views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/home/', views.dashboard_home, name='dashboard-home'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('dashboard/courses-enrolled/', views.courses_enrolled, name='courses-enrolled'),
    path('dashboard/courses-uploaded/', views.courses_uploaded, name='courses-uploaded'),
    path('dashboard/upload/', views.upload, name='uploade'),
    path('dashboard/<slug:slug>/course-edit/', views.course_edit, name='course-edit'),
    path('dashboard/<slug:slug>/delete/', views.delete_course, name='delete-course'),
    path('<str:instructor>/course/<slug:slug>/', views.course_details, name='course_details'),
    path('courses/<str:category>/', views.category, name='category'),
    path('search/', views.search_courses, name='search_courses'),
    path('dashboard/course-search/', views.course_search, name='course_search'),
    path('instructor/',views.instructor,name='instructor')

]
