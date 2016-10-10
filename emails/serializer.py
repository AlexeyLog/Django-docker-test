from .models import Email
from rest_framework import serializers


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('email_id', 'from_address', 'to_address', 'body', 'timestamp')
