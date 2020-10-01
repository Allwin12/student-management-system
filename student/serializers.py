from rest_framework import serializers
from student.models import School, Student


class SchoolListSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('id', 'name', 'email', 'address')


class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    school = SchoolListSerializer(required=True)

    class Meta:
        model = Student
        fields = '__all__'


class AddStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'name', 'grade', 'section', 'school', 'blood_group', 'mobile', 'address')


class AddSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('id', 'name', 'email', 'address')
