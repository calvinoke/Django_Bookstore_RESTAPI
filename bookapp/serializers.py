from rest_framework import serializers
from . models import Book
from django.forms import ValidationError

#class BookSerializer(serializers.Serializer):
  ##  title = serializers.CharField()
  #  number_of_pages = serializers.IntegerField()
  #  publish_date = serializers.DateField()
   # quantity = serializers.IntegerField()

  #  def create(self, data):
  #      return Book.objects.create(**data)

 #   def update(self, instance, data):
  #      instance.title = data.get('title', instance.title)
   #     instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
   #     instance.publish_date = data.get('publish_date', instance.publish_date)
   #     instance.quantity = data.get('quantity', instance.quantity)

   #     instance.save()
   #     return instance

#ClassBased way of creating serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = "__all__"

    #validating a specified object like title
    def validate_title(self, value):
        if value == "Diet Cook":
            raise ValidationError("No diet Cook Please")
        return value

    #validating all objects in the database..
    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
             raise ValidationError("Too heavy for Inventory")
        return data
