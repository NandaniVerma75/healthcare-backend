from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    age = serializers.ReadOnlyField()
    
    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'email', 'phone', 'date_of_birth', 
            'gender', 'blood_group', 'address', 'emergency_contact',
            'emergency_phone', 'medical_history', 'allergies', 
            'current_medications', 'created_by', 'age',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'age']
    
    def validate_email(self, value):
        patient_id = self.instance.id if self.instance else None
        if Patient.objects.filter(email=value).exclude(id=patient_id).exists():
            raise serializers.ValidationError("Patient with this email already exists")
        return value
    
    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must start with country code (+)")
        return value

class PatientListSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()
    
    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'email', 'phone', 'gender', 
            'age', 'created_at'
        ]