from rest_framework import serializers

from rating.models import Rating
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
