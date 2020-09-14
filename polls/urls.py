from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('comments/', views.CommentsView.as_view(), name='comments'),
    path('comments/list/', views.CommentsListView.as_view(), name='comment list'),
    path('comments/showform/list/', views.CommentsListView.as_view(), name='comment list'),
    path('comments/showform/', views.showform, name = "show form"),
]
