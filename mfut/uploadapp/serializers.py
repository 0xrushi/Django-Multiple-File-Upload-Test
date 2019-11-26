from rest_framework import serializers

from uploadapp.models import Blog, Image


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model =Blog
        fields = "__all__"
    def validate(self, data):
        title = data.get('title')
        if not title:
            raise serializers.ValidationError("Enter title ")
        return data
    def create(self, validated_data):
        title = validated_data.get('title')
        content = validated_data.get('content')
        instance = Blog.objects.create(title=title, content=content)

        request = self.context.get('request')
        files = request.FILES
        if files:
            for key, image in files.items():
                print('imagefound')
                Image.objects.create(blog=instance, image=image)
        return instance