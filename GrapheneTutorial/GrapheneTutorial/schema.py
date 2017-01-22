import graphene
from graphene_django.debug import DjangoDebug

import courses.schema

class Query(courses.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(query=Query)
