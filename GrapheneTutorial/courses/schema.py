from graphene import AbstractType, Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Teacher, Course


class TeacherNode(DjangoObjectType):
    class Meta:
        model = Teacher
        filter_fields = ['name']
        interfaces = (Node,)

class CourseNode(DjangoObjectType):
    class Meta:
        model = Course
        filter_fields = {
            'name' : ['exact', 'icontains', 'istartswith'],
            'summary' : ['icontains', 'istartswith'],
            'teacher':['exact'],
            'teacher__name':['exact'],
        }

        interfaces = (Node,)


class Query(AbstractType):
    teacher = Node.Field(TeacherNode)
    all_teachers = DjangoFilterConnectionField(TeacherNode)

    course = Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)
