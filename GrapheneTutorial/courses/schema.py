import graphene
from graphene import relay, AbstractType, Node, InputObjectType, InputField
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Teacher, Course


class TeacherNode(DjangoObjectType):
    class Meta:
        model = Teacher
        filter_fields = ['name', 'email']
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


class CreateTeacher(graphene.Mutation):
    class Input:
        name = graphene.String()
        email = graphene.String()

    teacher = graphene.Field(TeacherNode)

    @classmethod
    def mutate(self, cls, input, context, info):
        name = input.get('name')
        email = input.get('email')

        teacher = Teacher(name=name, email=email)
        teacher.save()
        return CreateTeacher(teacher=teacher)


class CreateCourse(graphene.ClientIDMutation):
    class Input:
        name = graphene.String()
        summary = graphene.String()
        teacher_id = graphene.String(required=True)

    course = graphene.Field(CourseNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        name = input.get('name')
        summary = input.get('summary')
        teacher_id = input.get("teacher_id")
        try:
            teacher_id = int(teacher_id)
        except ValueError:
            try:
                _type, teacher_id = Node.from_global_id(input.get("teacher_id"))
                assert _type == 'TeacherNode', 'Found {} instead of teacher'.format(_type)
                teacher_id = int(teacher_id)
            except:
                raise Exception("Received Invalid Teacher id: {}".format(teacher_id))

        teacher = Teacher._meta.model.objects.get(id=teacher_id)
        course = Course(name=name, summary=summary, teacher=teacher)
        course.save()
        return CreateCourse(course=course)


class UpdateTeacher(graphene.Mutation):
    class Input:
        name = graphene.String()
        email = graphene.String()
        id = graphene.String()

    teacher = graphene.Field(TeacherNode)

    @classmethod
    def mutate(self, cls, input, context, info):
        id = input.get("id")
        try:
            id = int(id)
        except ValueError:
            try:
                _type, id = Node.from_global_id(input.get("id"))
                assert _type == 'TeacherNode', 'Found {} instead of teacher'.format(_type)
                id = int(id)
            except:
                raise Exception("Received Invalid Teacher id: {}".format(id))
        teacher = Teacher._meta.model.objects.get(id=id)
        name = input.get("name")
        email = input.get("email")
        if name is not None:
            teacher.name = name
        if email is not None:
            teacher.email = email
        teacher.save()
        return UpdateTeacher(teacher=teacher)

class DeleteCourse(graphene.Mutation):
    class Input:
        name = graphene.String()
        id = graphene.String()

    course = graphene.Field(CourseNode)


    @classmethod
    def mutate(self, cls, input, context, info):
        id = input.get("id")
        try:
            id = int(id)
        except ValueError:
            try:
                _type, id = Node.from_global_id(input.get("id"))
                assert _type == 'CourseNode', 'Found {} instead of course'.format(_type)
                id = int(id)
            except:
                raise Exception("Received Invalid Course id: {}".format(id))
        course = Course._meta.model.objects.get(id=id)
        if course is not None:
            course.delete()
        return DeleteCourse(course=course)



class CourseMutations(AbstractType):
    create_teacher = CreateTeacher.Field()
    create_course = CreateCourse.Field()
    update_teacher = UpdateTeacher.Field()
    delete_course = DeleteCourse.Field()


class Query(AbstractType):
    teacher = Node.Field(TeacherNode)
    all_teachers = DjangoFilterConnectionField(TeacherNode)

    course = Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)
