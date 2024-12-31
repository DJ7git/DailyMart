from django.urls import path
from . import views
from .views import MyView

urlpatterns = [
    path('',views.defaultAdmin,name="defaultAdmin"),
    path('aindex',views.aindex,name="aindex"),
    path('add',views.add,name="add"),
    path('getdata',views.getdata,name="getdata"),
    path('view',views.view,name="view"),
    path('editdata/<int:id>',views.editdata,name="editdata"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('articles/',views.article_list),
    path('article_detail/<int:pk>/',views.article_details),
    path('api/my-view/', MyView.as_view(), name='my-view'),
]