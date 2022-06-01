
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UrlsPatterns,name='url' ),
    path('all-students/',views.StudentAll,name='all_students'),
    path('student/<int:pk>',views.SingleStudent,name='student'),
    path('studentCreate/',views.StudentCreate,name='student-create'),
]