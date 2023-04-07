from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>',views.detail,name='detail'),
    path('blog/new',views.new,name='new'),
    path('blog/create',views.create,name='create'),
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),
    path('bolg/delete/<int:blog_id>', views.delete, name='delete'),
    path('blog/comment/<int:blog_id>', views.add_comment_to_post, name='add_comment_to_post'),
]