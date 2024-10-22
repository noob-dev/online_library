from django.urls import path
from .views import BookListView, AddBookView, BookDetailView, UpdateBookView, DeleteBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('update_book/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book')
]
