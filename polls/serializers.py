from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Question.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance