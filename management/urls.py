from django.urls import path
from management.views import *

urlpatterns = [
    path("about/", about, name="about"),
    path("reservation/", reservation, name="account"),
    path('Logout', Logout, name="Logout"),
    path('menu', menu, name='menu'),
    path('menu-single/<int:dishid>',menusingle,name="menusingle"),
    path('AdminPanel',AdminPanel,name="AdminPanel"),
    path('editCat',editCat,name='editCat'),
    path('editDish',editDish,name='editDish'),
    path('editTeams',editTeams,name='editTeams'),
    path('contactsUs',contactsUs,name='contactsUs')
]
