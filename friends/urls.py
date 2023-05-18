from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('send_friend_request/', views.SendFriendRequest.as_view(), name='send_friend_request'),
    path('accept_friend_request/', views.AcceptFriendRequest.as_view(), name='accept_friend_request'),
    path('reject_friend_request/', views.RejectFriendRequest.as_view(), name='reject_friend_request'),
    path('cancel_friend_request/', views.CancelFriendRequest.as_view(), name='cancel_friend_request'),
    path('remove_friend/', views.RemoveFriend.as_view(), name='remove_friend'),
    path('friends_list/', views.FriendsList.as_view(), name='friends_list'),
    path('friend_requests/', views.FriendRequests.as_view(), name='friend_requests'),
]
