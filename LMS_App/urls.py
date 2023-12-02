from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('books',views.books, name='books'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),

]
