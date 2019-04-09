from django.urls import path
from . import views
from . import gviews

app_name='polls'

urlpatterns = [ 
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('v2/', gviews.IndexView.as_view(), name='index'),
    path('v2/<int:pk>/', gviews.DetailView.as_view(), name='detail'),
    path('v2/<int:pk>/results/', gviews.ResultsView.as_view(), name='results'),
    path('v2/<int:question_id>/vote/', gviews.vote, name='vote'),
]