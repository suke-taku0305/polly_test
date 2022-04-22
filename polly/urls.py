from django.urls import path
from . import views

app_name = "polly"
urlpatterns = [
  path("create/", views.PollyCreateView.as_view(),name="create"),
  path("", views.PollyListView.as_view(),name="list"),
  path("<str:pk>/", views.PollyDetailView.as_view(),name="detail"),
]