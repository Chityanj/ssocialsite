from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import User, Post, Comment
from .serializers import (
    UserSerializer,
    CommentSerializer,
    PostSerializer,
    PostDetailSerializer,
    UserDetailSerializer,
)

@api_view(['POST'])
def authenticate_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.filter(email=email).first()
    
    if user is None:
        # User doesn't exist, create a new user
        user = User.objects.create_user(email=email, username=email, password=password)
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    
    return Response({'access_token': access_token})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)
    request.user.following.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    title = request.data.get('title')
    description = request.data.get('description')
    
    if not title or not description:
        return Response({'error': 'Title and description are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    post = Post.objects.create(title=title, description=description, author=request.user)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post.delete()
    return Response({'message': 'Post deleted successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes.add(request.user)
    return Response({'message': f'You liked the post "{post.title}"'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes.remove(request.user)
    return Response({'message': f'You unliked the post "{post.title}"'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    content = request.data.get('content')
    
    if not content:
        return Response({'error': 'Comment content is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    comment = Comment.objects.create(post=post, author=request.user, content=content)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostDetailSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# Add more views as needed for your other actions...

