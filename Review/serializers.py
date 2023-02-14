from rest_framework import fields,serializers
from .models import Review
from Review.models import CAFE_KEYWORDS

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    # class Meta:
    #     model=Review
    #     fields='__all__'
   
    keywords=fields.MultipleChoiceField(choices=CAFE_KEYWORDS)
    