from django.urls import path
from . import views
from .views import *  # Import the view here


urlpatterns = [
    path('defaultuser',views.defaultuser,name="defaultuser"),
    path('uindex',views.uindex,name="uindex"),
    path('viewsingledata/<int:id>',views.viewsingledata,name="viewsingledata"),
    # path('add',views.add,name="add"),
    # path('getdata',views.getdata,name="getdata"),
    path('viewuser',views.viewuser,name="viewuser"),
    # path('edit/<int:id>',views.edit,name="edit"),
    # path('update/<int:id>',views.update,name="update"),
    # path('delete/<int:id>',views.delete,name="delete"),
    path('mymodel/', views.article_list),
]