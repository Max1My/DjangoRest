from pprint import pprint

import graphene
from graphene_django import DjangoObjectType
from authors.models import Book, Author


class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,birthday_year,id):
        author = Author.objects.get(pk=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)

class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType,id=graphene.Int(required=True))

    def resolve_author_by_id(self,info,id):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)