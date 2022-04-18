
from django.conf.urls import url
from connections.views import view_friends, friendship_add_friend,friend_remove, friendship_accept, \
    friendship_reject, friendship_cancel, friendship_request_list, \
    friendship_request_list_rejected, friendship_requests_detail, followers,\
    following, follower_add, follower_remove, all_users

app_name = 'connections'

urlpatterns = [
    url(
        regex=r'^users/$',
        view=all_users,
        name='friendship_view_users',
    ),
    url(
        regex=r'^friends/$',
        view=view_friends,
        name='friendship_view_friends',
    ),
    url(
        regex=r'^friends/(?P<username>[\w-]+)/$',
        view=view_friends,
        name='friendship_view_friends',
    ),

    url(
        regex=r'^friend/add/(?P<to_username>[\w-]+)/$',
        view=friendship_add_friend,
        name='friendship_add_friend',
    ),
    url(
        regex=r'^friend/remove/(?P<to_username>[\w-]+)/$',
        view=friend_remove,
        name='friend_remove',
    ),
    url(
        regex=r'^friend/accept/(?P<friendship_request_id>\d+)/$',
        view=friendship_accept,
        name='friendship_accept',
    ),
    url(
        regex=r'^friend/reject/(?P<friendship_request_id>\d+)/$',
        view=friendship_reject,
        name='friendship_reject',
    ),
    url(
        regex=r'^friend/cancel/(?P<friendship_request_id>\d+)/$',
        view=friendship_cancel,
        name='friendship_cancel',
    ),
    url(
        regex=r'^friend/requests/$',
        view=friendship_request_list,
        name='friendship_request_list',
    ),
    url(
        regex=r'^friend/requests/rejected/$',
        view=friendship_request_list_rejected,
        name='friendship_requests_rejected',
    ),
    url(
        regex=r'^friend/request/(?P<friendship_request_id>\d+)/$',
        view=friendship_requests_detail,
        name='friendship_requests_detail',
    ),
]