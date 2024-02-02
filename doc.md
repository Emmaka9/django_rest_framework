Authentication & Permissions
_________________________________
Set Permissions and restrictions on who can edit or delete code snippets. Add some advanced behavior to  make sure:
    1. code snippets are always associated with creator.
    2. only authenticated user may create snippets
    3. only the creator of a snippet may update or delete it
    4. unauthenticated requests should have full read-only access

```
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
```
The code snippet is a field in a django model definition. It is a ForeignKey field, it is related to another model called auth.User(django default
user model). It is used to create many-to-one relationships. That is many snippets created by one user.
 - First Argument (auth.User): auth.User is the default user model provided by django's Authentication system. That means the owner field 
 will reference an instance of the User model.

 - related_name='snippets': This Argument is used in the reverse relation. It allows us to access the set of all instances
 of this model related to a single user instance. E.g. if we have a User instance user1, we can access all related instances
 of this model using `user1.snippets`.

  - `on_delete:models.CASCADE` : This Argument defines the behavior when the referenced object is deleted (User).
     models.CASCADE means that when a User is deleted, all related instances of this model will also be deleted.  This is a way to 
     maintain referential integrity.

-----------------------------------------------------------------------------------------

```
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    queryset = Snippet.objects.all()

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
```
This code snippet defines a DRF serializer, UserSerializer, for the built-in django `User` model imported from Django's built-in
authentication system.
The serializer includes user's basic information and a relation to the snippets that the user might be associated with.

    -> The serializer extends the serializer.ModelSerializer class. serializer.ModelSerializer automatically generates a serializer
        that corresponds to the user model's fields.
    -> snippets = serializer.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all()) : 
        A field named snippets in the User class.
        The field is an instance of PrimaryKeyRelatedField. It will represent the related snippets by their primary key values.
        - many=True: indicates User can be associated with multiple snippets - one-to-many relationship between user and snippet.
    -> queryset = Snippet.objects.all(): specifies the queryset that will be used to populate the field. It effectively means any snippet instance can be associated 
        with a User, as it includes all Snippet instances
    -> The Meta class inside the serializer class contains metadata about the serializer. 
        - Here, it specifies that the serializer is for the User model.
        - fields = ['id', 'username', 'snippets'] : indicates which fields of the user model should be included in the serialized output.




