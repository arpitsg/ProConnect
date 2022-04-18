from django.contrib.auth.decorators import login_required
from django.conf import settings
try:
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = User

from django.shortcuts import render, get_object_or_404, redirect

from .models import Connection,  Connection_Request

get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')
get_friendship_context_object_list_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME', 'users')


# def view_friends(request, username, template_name='friendship/friend/user_list.html'):
#     """ View the friends of a user """
#     user = get_object_or_404(user_model, username=username)
#     friends = Friend.objects.friends(user)
#     return render(request, template_name, {
#         get_friendship_context_object_name(): user,
#         'friendship_context_object_name': get_friendship_context_object_name()
#     })
def view_connections(request, username=None, template_name='friendship/friend/user_list.html'):
    """ View the friends of a user """
    if username:
        user = get_object_or_404(user_model, username=username)
    else:
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, username=request.user.username)
    friends = Connection.objects.friends(user)
    return render(request, template_name, {
        get_friendship_context_object_name(): user,
        'friendship_context_object_name': get_friendship_context_object_name()
    })

@login_required
def add_connection(request, to_username, template_name='friendship/friend/add.html'):
    """ Create a Connection Request """
    ctx = {'to_username': to_username}

    if request.method == 'POST':
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        Connection.objects.add_connection(from_user, to_user)
        return redirect('friendship:friendship_request_list')



    return render(request, template_name, ctx)
@login_required
def connection_remove(request, to_username, template_name='friendship/friend/remove_friend.html'):
    """ Remove a friend relationship """
    if request.method == 'POST':
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        Connection.objects.remove_friend(from_user, to_user)
        return redirect('friendship:friendship_view_friends')

    return render(request, template_name, {'to_username': to_username})



@login_required
def connection_accept(request, friendship_request_id):
    """ Accept a friendship request """
    if request.method == 'POST':
        f_request = get_object_or_404(
            request.user.connection_requests_received,
            id=friendship_request_id)
        f_request.accept()
        return redirect('friendship:friendship_view_friends', username=request.user.username)

    return redirect('friendship:friendship_requests_detail', friendship_request_id=friendship_request_id)


@login_required
def connection_reject(request, friendship_request_id):
    """ Reject a friendship request """
    if request.method == 'POST':
        f_request = get_object_or_404(
            request.user.friendship_requests_received,
            id=friendship_request_id)
        f_request.reject()
        return redirect('friendship:friendship_request_list')

    return redirect('friendship:friendship_requests_detail', friendship_request_id=friendship_request_id)


@login_required
def connection_cancel(request, friendship_request_id):
    """ Cancel a previously created friendship_request_id """
    if request.method == 'POST':
        f_request = get_object_or_404(
            request.user.connection_requests_sent,
            id=friendship_request_id)
        f_request.cancel()
        return redirect('friendship:friendship_request_list')

    return redirect('friendship:friendship_requests_detail', friendship_request_id=friendship_request_id)


@login_required
def connection_request_list(request, template_name='connections/connections/requests_list.html'):
    """ View unread and read friendship requests """
    friendship_requests_from_others = Connection.objects.unread_requests(user=request.user)
    friendship_requests_sent = Connection.objects.sent_requests(user=request.user)
    # friendship_requests_from_others = FriendshipRequest.objects.filter(rejected__isnull=True,to_user=request.user)

    return render(request, template_name, {'friendship_requests_from_others': friendship_requests_from_others},{'friendship_requests_sent': friendship_requests_sent})


@login_required
def connection_request_list_rejected(request, template_name='connections/connections/requests_rejected_list.html'):
    """ View rejected friendship requests """
    friendship_requests=Connection.objects.rejected_requests(user=request.user)
    # friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True)

    return render(request, template_name, {'requests': friendship_requests})


@login_required
def connection_requests_detail(request, friendship_request_id, template_name='connections/connections/request.html'):
    """ View a particular friendship request """
    f_request = get_object_or_404(Connection_Request, id=friendship_request_id)

    return render(request, template_name, {'friendship_request': f_request})



def all_users(request, template_name="friendship/user_actions.html"):
    users = user_model.objects.all()

    return render(request, template_name, {get_friendship_context_object_list_name(): users})