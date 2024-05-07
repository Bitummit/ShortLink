from rest_framework import serializers, status
from .models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'

    def create(self, validated_data):
        full_link = validated_data["full_link"]
        link, created = Link.objects.get_or_create(full_link=full_link)
        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK

        return link, status_code