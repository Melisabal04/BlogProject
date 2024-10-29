from django.urls import path
from . import views

app_name='blog_app'

urlpatterns = [
    path ("",views.homepage,name='home'),
    path("addtoblog/",views.addtoblog,name='addtoblog'),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("delete//<int:id>",views.delete,name="delete")
]
