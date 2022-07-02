                                    #COPY ENTIRE CODE FROM first_site/urls.py


from django.urls import path        #Add include method
from . import views

urlpatterns = [
    path('',views.index,name="home"),          #Main page -> link to -> main\urls.py
    path('about',views.about,name="about"),
    path('contacts',views.contacts,name="contacts"),
    path('create',views.create,name="create"),
]
