from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from chatcom.friends_chats.serializers import UserProfileSerializer 

class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.profile_picture.url') 

    profile = UserProfileSerializer()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'profile'
        )