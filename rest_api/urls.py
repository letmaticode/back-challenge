from django.urls import path

from .views import (
    UserFriendsView,
    UserListView,
    FriendListView,
    LessonsListView
)

urlpatterns = [
    path('', UserListView.as_view()),
    path('users', UserListView.as_view()),
    path('friends', FriendListView.as_view()),
    path('userfriends/', UserFriendsView.as_view()),
    path('userfriends/<int:id>', UserFriendsView.as_view()),
    path('lessons/<int:id>', LessonsListView.as_view()),
]