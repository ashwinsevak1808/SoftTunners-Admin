from django.urls import path
from main import views

urlpatterns = [
    #  New pages level URL
    path("", views.home, name="home"),
        path("reportsMain", views.reportsMain, name="reportsMain"),

    # Emailer Urls
    path('emailer',views.emailer,name='emailer'),
    path('emailerView',views.emailerView,name='emailerView'),


    # For Authrization
    path('login',views.login,name='login'),

]

