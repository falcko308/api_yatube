from rest_framework import routers
from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet

from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
