# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, serializers
from .models import Profile, Post, Like, Follow
from .serializers import ProfileSerializer, PostSerializer, LikeSerializer, FollowSerializer, RegisterSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao minitwitter!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def feed(self, request):
        user = request.user
        following_profiles = user.profile.following.all().values_list('id', flat = True)
        feed_posts = Post.objects.filter(author__profile__id__in=following_profiles).order_by('-created_at')
        page = self.paginate_queryset(feed_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(feed_posts, many=True)
        return Response(serializer.data)
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if Like.objects.filter(user=self.request.user, post=serializer.validated_data['post']).exists():
            raise serializers.ValidationError('Você já curtiu esse post')
        serializer.save(user=self.request.user)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]