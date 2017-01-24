import graphene
from graphene_django.debug import DjangoDebug

import courses.schema

class Query(courses.schema.Query, graphene.ObjectType):
    pass

class AllMutations(courses.schema.CourseMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=AllMutations)
