from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=True, max_length=200)
    note = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        create and return a todo instance based on given data
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # if the validated_data has a null field, return the current value
        instance.description = validated_data.get('description', instance.description)
        instance.note = validated_data.get('node', instance.note)
        instance.save()
        return instance