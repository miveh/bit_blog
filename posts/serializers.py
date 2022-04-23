from rest_framework import serializers

from accounts.models import CustomUser
from rating.models import Rating
from .exceptions import CreateRateException
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    your_rate = serializers.SerializerMethodField()

    class Meta:
        fields = ['title', 'calculate_rate', 'rate_counter', 'your_rate']
        model = Post

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data['calculate_rate'] = instance.calculate_rate
        return data

    def get_your_rate(self, obj):
        if self.context['request'].user.is_authenticated:
            rates = Rating.objects.filter(user_id=self.context['request'].user, post_id=obj.id)
            print(rates)
            if rates.exists():
                return rates[0].rate
            else:
                return None


class RateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['rate']
        model = Rating
        extra_kwargs = {
            'rate': {'required': True},
        }

    def create(self, validated_data):
        rate_value = validated_data.pop('rate', None)
        post = Post.objects.get_or_raise(id=self.context['request'].query_params.get('post_id'))
        user = self.context['request'].user

        # uniqueness is enforced at the database level.
        obj, created = Rating.objects.update_or_create(post_id=post, user_id=user, defaults={'rate': rate_value},)
        return obj
