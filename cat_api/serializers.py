from rest_framework import serializers

from .models import Cat, Target, Mission
from .validators import ValidBreedValidator


class CatSerializer(serializers.ModelSerializer):
    breed = serializers.CharField(validators=[ValidBreedValidator()])

    class Meta:
        model = Cat
        fields = ['id', 'name', 'years_of_exp', 'breed', 'salary']


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('name', 'country', 'notes', 'complete')


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ('id', 'cat', 'complete', 'targets')

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', None)
        instance.cat = validated_data.get('cat', instance.cat)
        instance.is_completed = validated_data.get('icomplete', instance.is_completed)
        instance.save()

        if targets_data is not None:
            instance.targets.all().delete()
            for target_data in targets_data:
                Target.objects.create(mission=instance, **target_data)

        return instance