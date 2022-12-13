from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MobileRecharge import views
urlpatterns = [
    # PlanList
    path('api/plan', views.PlanList.as_view()),
    # StateList
    path('api/state', views.StateList.as_view()),
    # OpratorsList
    path('api/operator', views.OpratorsList.as_view()),
    # HistoryList
    path('api/history', views.HistoryList.as_view()),
    # HistoryDetail
    path('api/history/<int:pk>', views.HistoryDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)