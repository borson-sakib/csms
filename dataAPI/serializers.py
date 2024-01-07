from rest_framework import serializers
from adminpanel.models import complain_details


# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = complain_details
#         fields = ['complain_id', 'category', 'query','other_query']
        
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         # Filter out items with values set to "None"
#         # return {key: value for key, value in data.items() if value != "None"}
        
#         instances = complain_details.objects.filter(complain_id=instance.complain_id)

#         # Create a list to store representations of each complaint
#         complaints_data = []

#         for complain_instance in instances:
#             data = super().to_representation(complain_instance)
#             # Filter out items with values set to "None"
#             filtered_data = {key: value for key, value in data.items() if value != "None"}
#             complaints_data.append(filtered_data)

#         return complaints_data
    

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = complain_details
        fields = '__all__'