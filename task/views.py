from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import TaskModel
from .serializers import TaskSerializers
from django.utils import timezone
import datetime

class TaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the  items for given requested user
        '''
        date_filter=7
        if date_filter!=0:
            min_date =datetime.datetime.today() - datetime.timedelta(days=7)
        else:
            min_date = datetime.datetime.combine(timezone.now().date(), datetime.datetime.today().time().min)
        today_max = datetime.datetime.combine(timezone.now().date(), datetime.datetime.today().time().max)
        print("today_min",min_date)
        print("today_max",today_max)
        todos = TaskModel.objects.filter(date__range=(min_date, today_max))
        serializer = TaskSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "general_task": request.data['general_task'],
            "project_management": request.data['project_management'],
            "quality_analyst": request.data['quality_analyst'],
            "ui_or_ux": request.data['ui_or_ux'],
            "meeting": request.data['meeting'],
            "development": request.data['development'],
            "blockers": request.data['blockers'],
            "comments": request.data['comments'],
            "user": request.user.id
        }
        serializer = TaskSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
