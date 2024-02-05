from search import views
from django.urls import path,include
app_name='search'
urlpatterns = [


  path('',views.search,name="search")

]