from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('user','username','bio','image','token')

    def create(self,validated_data):
        print('creating')
        a = validated_data.get('user')
        print(a)
