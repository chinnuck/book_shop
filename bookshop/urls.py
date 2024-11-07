from django.contrib import admin
from django.urls import path
from bookapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('add', views.add),
    path('view', views.view),
    path('update/<int:id>', views.update),
    path('books', views.books),
    path('book/<int:id>', views.book),
    path('delete/<int:id>', views.delete),
    path('addcart/<int:id>', views.add_to_cart),
    path('delete_cart/<int:id>', views.delete_cart),
    path('cart', views.view_cart),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('search', views.search),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
