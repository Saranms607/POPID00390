from django.urls import path
from hosapp import views


urlpatterns=[
    path('',views.new,name='new'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('departments/',views.departments,name='departments'),
    path('contact/',views.contact,name='contact'),
    path('medicine/',views.medicine,name='medicine'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    
    
]

