from rest_framework import serializers

from avtosalon.models import Buyer


class  AutosalonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Buyer
        fields = "__all__"