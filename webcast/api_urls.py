# Third Party Stuff
from rest_framework.routers import DefaultRouter
from webcast.webcast_back.api import ConnectMeViewSet


# webcast Stuff
from webcast.base.api.routers import SingletonRouter
from webcast.users.api import CurrentUserViewSet
from webcast.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register("auth", AuthViewSet, basename="auth")
default_router.register("connect_me", ConnectMeViewSet, basename="connect_me")
singleton_router.register("me", CurrentUserViewSet, basename="me")

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
