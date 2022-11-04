from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개 URL 을 만들어줌

urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('', include(router.urls)),
    # path('public/', views.public_post_list),
]