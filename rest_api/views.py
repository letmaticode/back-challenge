from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Friends, Lessons
from .serializers import UserSerializer, FriendSerializer, LessonsSerializer


class UserListView(APIView):
    def get(self, request):
        """List all users"""
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)    


class FriendListView(APIView):
    def get(self, request): 
        """List all friends"""
        try:
            friends = Friends.objects.all()
            serializer = FriendSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)    


class UserFriendsView(APIView):
    def get(self, request, id):
        """List all friends of a specific user"""
        try:
            friends = Friends.objects.filter(user_id=id)
            serializer = FriendSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LessonsListView(APIView):
    def get(self, request, id):
        """List all friends of a specific user"""
        try:
            lessons = Lessons.objects.filter(student_id=id)
            serializer = LessonsSerializer(lessons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
