from rest_framework import serializers
from .models import Project
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner', 'members', 'member_ids', 'status', 'created_at', 'updated_at')

    def create(self, validated_data):
        member_ids = validated_data.pop('member_ids', [])
        project = Project.objects.create(**validated_data)
        if member_ids:
            members = User.objects.filter(id__in=member_ids)
            project.members.set(members)
        return project

    def update(self, instance, validated_data):
        member_ids = validated_data.pop('member_ids', None)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        if member_ids is not None:
            members = User.objects.filter(id__in=member_ids)
            instance.members.set(members)
        return instance
