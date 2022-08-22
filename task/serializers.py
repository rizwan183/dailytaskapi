from .models import TaskModel
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
