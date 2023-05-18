from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import FriendRequest


class SendFriendRequest(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        from_user = request.user
        target_user_email = request.POST.get("target_user_email")
        to_user = User.objects.get(username=target_user_email)
        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=from_user,
            to_user=to_user
        )
        return redirect("user:profile", pk=target_user_email)


class AcceptFriendRequest(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_request_id = request.POST.get("friend_request_id")
        friend_request = FriendRequest.objects.get(id=friend_request_id)
        if friend_request.to_user == request.user:
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=401)


class RejectFriendRequest(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_request_id = request.POST.get("friend_request_id")
        friend_request = FriendRequest.objects.get(id=friend_request_id)
        if friend_request.to_user == request.user:
            friend_request.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=401)


class CancelFriendRequest(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_request_id = request.POST.get("friend_request_id")
        friend_request = FriendRequest.objects.get(id=friend_request_id)
        if friend_request.from_user == request.user:
            friend_request.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=401)


class RemoveFriend(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_id = request.POST.get("friend_id")
        friend = User.objects.get(id=friend_id)
        if friend in request.user.friends.all():
            request.user.friends.remove(friend)
            friend.friends.remove(request.user)
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=401)


class FriendRequestListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        friend_requests_to_user = FriendRequest.objects.filter(to_user=request.user)
        friend_requests_from_user = FriendRequest.objects.filter(from_user=request.user)
        context = {'friend_requests_to_user': friend_requests_to_user,
                   'friend_requests_from_user': friend_requests_from_user, 'user': user}
        return render(request, "friends/friend_request_list.html", context)


class FriendListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        friends = request.user.friends.all()
        context = {'friends': friends, 'user': user}
        return render(request, "friends/friend_list.html", context)
