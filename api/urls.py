from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import Snippets,Tags


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("snippet/", Snippets.as_view(), name="snippets"),
    path("snippet/<int:snippet_id>", Snippets.as_view(), name="get_specific_snippetI"),
    path("tag/", Tags.as_view(), name="get_tags"),
    path("tag/<str:tag_title>", Tags.as_view(), name="get_snippets_of_specific_tag"),
]
