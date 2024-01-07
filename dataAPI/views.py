from django.shortcuts import render
from adminpanel.models import complain_details

# appname/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from adminpanel.models import complain_details
from .serializers import ComplaintSerializer
from rest_framework.decorators import api_view

# class ComplaintDetailsView(APIView):
#     def get(self, request, complain_id):
#         # Query the database to get complaints with the specified complain_id
#         complaints = complain_details.objects.filter(complain_id=complain_id)

#         # Serialize the complaints
#         serializer = ItemSerializer(complaints, many=True)

#         # Return the serialized data as a response
#         return Response(serializer.data)
    

def get_complaint_details(complain_id):
    # Implement your logic to fetch complaint details from your model or database
    # Example: return a dictionary with complaint details
    
    complain_obj = complain_details.objects.filter(complain_id=complain_id)
    
    complains = []
    
    for complain_user in complain_obj:
        temp = {
        "complain_id": complain_user.complain_id,
        "category": complain_user.category,
        "query": complain_user.query,
        "other_query": complain_user.other_query
        }
        complains.append(temp)
    
    return complains
    
    
@api_view(['GET'])
def get_complaint(request):
    complain_id = request.GET.get('complain_id')

    if not complain_id:
        return Response({"error": "Complaint ID is required"}, status=400)

    complaint_details = get_complaint_details(complain_id)
    # complaint_details = complain_details.objects.filter(complain_id=complain_id)

    if not complaint_details:
        return Response({"error": "Complaint not found"}, status=404)

    serializer = ComplaintSerializer(complaint_details, many=True)
    
    response = Response(serializer.data)
    response['Custom-Header'] = 'Your Custom Value'
    response['Another-Header'] = 'Another Custom Value'
    
    return response