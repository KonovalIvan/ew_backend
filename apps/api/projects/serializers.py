from rest_framework import serializers


class ProjectsShortInfoQuerySerializer(serializers.Serializer):
    is_archived = serializers.BooleanField()
