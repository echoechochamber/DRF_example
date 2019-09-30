from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # using the ModelSerializer class is a syntactic sugar for the basick create and update methods
    class Meta:
        model = Todo
        fields = ['id', 'description', 'note']
