from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MobileRecharge import views
urlpatterns = [
    path('', views.SnippetPage.as_view()),
    path('api/snippet/', views.SnippetList.as_view()),
    path('api/snippet/<int:pk>/', views.SnippetDetail.as_view()),
    # PlanList
    path('api/plan', views.PlanList.as_view()),
    path('api/state', views.StateList.as_view()),
    path('api/operator', views.OpratorsList.as_view()),
    # HistoryList
    path('api/history', views.HistoryList.as_view()),
    path('api/history/<int:pk>', views.HistoryDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)