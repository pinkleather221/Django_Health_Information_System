from rest_framework import serializers
from clients.models import Client, HealthProgram, Enrollment

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    program = HealthProgramSerializer()
    
    class Meta:
        model = Enrollment
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = '__all__'
    
    def get_programs(self, obj):
        enrollments = Enrollment.objects.filter(client=obj)
        return EnrollmentSerializer(enrollments, many=True).data