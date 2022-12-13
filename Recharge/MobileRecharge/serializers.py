from rest_framework import serializers
from .models import History

    
class PlanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    plan_status = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_operator = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_category = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_price = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_validity = serializers.CharField(required=False, allow_blank=True, max_length=100)
    plan_details = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    # def create(self, validated_data):
    #     return Plans.objects.create(**validated_data)
    

class OpratorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=False)
    oprator_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    oprator_code = serializers.CharField(required=False, allow_blank=True, max_length=100)
    oprator_type = serializers.CharField(required=False, allow_blank=True, max_length=100)
    oprator_state = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # oprator_image = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    # def create(self, validated_data):
    #     return Oprators.objects.create(**validated_data)


class HistorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=False)
    user_mobile = serializers.CharField(required=False, allow_blank=True, max_length=100)
    user_oprator = serializers.CharField(required=False, allow_blank=True, max_length=100)
    user_plan = serializers.CharField(required=False, allow_blank=True, max_length=100)
    user_state = serializers.CharField(required=False, allow_blank=True, max_length=100)
    amount = serializers.CharField(required=False, allow_blank=True, max_length=100)
    status = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return History.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_mobile = validated_data.get('user_mobile', instance.user_mobile)
        instance.user_oprator = validated_data.get('user_oprator', instance.user_oprator)
        instance.user_plan = validated_data.get('user_plan', instance.user_plan)
        instance.user_state = validated_data.get('user_state', instance.user_state)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
