from shop import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
app_name='shop'

urlpatterns = [
    path('',views.allcategories,name="allcategories"),
    path('allprod/<p>',views.allproducts,name="allprod"),
    path('details/<p>',views.details,name="details"),
    path('register',views.register,name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)