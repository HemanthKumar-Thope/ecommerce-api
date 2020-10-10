from django.urls import path

from project_apis import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
