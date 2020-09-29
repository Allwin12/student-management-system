from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import School, Student
from student.serializers import SchoolListSerializer, StudentListSerializer, StudentDetailSerializer


class SchoolView(APIView):
    def get(self, request):
        schools = School.objects.all()
        school_serializer = SchoolListSerializer(schools, many=True)
        return Response(school_serializer.data)


class SchoolDetailView(APIView):
    def get(self, request, school_id):
        school = School.objects.get(pk=school_id)
        school_serializer = SchoolListSerializer(school)
        return Response(school_serializer.data)


class StudentView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        students = Student.objects.all()

        # case insensitive query param filter
        if name is not None:
            students = students.filter(name__icontains=name)
        student_serializer = StudentListSerializer(students, many=True)
        return Response(student_serializer.data)


class StudentDetailView(APIView):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        return Response(StudentDetailSerializer(student).data)
