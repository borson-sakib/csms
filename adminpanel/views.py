from django.http import HttpResponse
from django.shortcuts import render 

# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404

from .forms import RegistrationForm
from .forms import UploadCsvForm
from .forms import QueryForm
from .models import CustomerRepository
from .models import Frequest_query_set
from .models import SearchedEntry
from .models import complaints_info
from .models import complain_details
from django.contrib.auth import login
import csv
import json
from io import TextIOWrapper
from django.http import JsonResponse



def index(request):
    
    return render(request,'dashboard.html')


def dashboard(request):
    
    return render(request,'dashboard.html')

def raise_ticket(request):
    
    complained_through = request.GET.get('id')
    
    other_info = process_verify_entry(complained_through)
    
    print(other_info['info']['Customer ID'])
    
    form_data= {
        'complained_through' : complained_through,
        'customer_id': other_info['info']['Customer ID'],
        'mobile_no': other_info['info']['mobile'],
        'name': other_info['info']['Name'],
    }
    form = QueryForm(initial=form_data)
    # {'result': 'success', 'info': {'Customer ID': '15771873', 'Name': 'Buccho', 'DOB': datetime.date(1996, 1, 17), 'Card No.': '4520987475129160', 'Card Type': 'SILVER', 'mobile': '01842617777'}}
    return render(request,'ticket/raise_ticket.html',{'form':form})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your home page
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def init_tickt(request):
    form = QueryForm()
    user = 'test_user1'

    # Get the last searched entry for the same user
    last_entry = SearchedEntry.objects.filter(searched_by=user).order_by('-created_at').first()
    if last_entry:
        last_searched_value = last_entry
        # Use last_searched_value as needed
    else:
        last_searched_value = 'No Last Search...'    
        
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # Get the currently logged-in user

            # Handle the form submission as needed
            # For example, you can access the selected values using form.cleaned_data['category'] and form.cleaned_data['query']
            
            # Access the last searched value for the same user
            pass
            
                
    
    return render(request, 'ticket/init_tickets.html', {'form': form,'last_searched':last_searched_value})


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCsvForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'success.html')
    else:
        form = UploadCsvForm()

    return render(request, 'upload_csv.html', {'form': form})

def handle_uploaded_file(file):
    # Assuming the CSV file has a header row
    csv_file = TextIOWrapper(file, encoding='utf-8')  # Use the appropriate encoding for your CSV file
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Create an instance of YourModel and save it to the database
        # CustomerRepository.objects.create(**row)
        Frequest_query_set.objects.create(**row)
        
        
        
def verify_entry(request):
 
    input_value = request.GET.get('inputValue', '')

    response_data = process_verify_entry(input_value)
    
    return JsonResponse(response_data)

def process_verify_entry(id):
    
    input_value = id
    try:
        entry = CustomerRepository.objects.get(Mobile=input_value)  # Check if Mobile field matches
    except CustomerRepository.DoesNotExist:
        try:
            entry = CustomerRepository.objects.get(CardNo=input_value)  # Check if Card field matches
        except CustomerRepository.DoesNotExist:
            # If the entry doesn't exist, return an error message
            response_data = {'result': 'error', 'message': 'Entry not found'}
            return JsonResponse(response_data)
    SearchedEntry.objects.create(entry=entry, searched_value=input_value,searched_by='test_user1')


    # If the entry exists, return relevant information as JSON
    response_data = {'result': 'success', 'info': {'Customer ID': entry.CustomerId,'Name':entry.Surname,'DOB': entry.DOB, 'Card No.': entry.CardNo,'Card Type':entry.CardType,'mobile':entry.Mobile}}
    
    return response_data

def query_form(request):
    form = QueryForm()

    if request.method == 'POST':
        stored_queries_json = request.POST.get('stored_queries')
        
        # print(request.POST.get('urgency'))
        # print(request.POST.get('customer_id'))
        # print(request.POST.get('complained_through'))
        # print(request.POST.get('name'))
        # print(request.POST.get('remarks'))
        
        
        complaints_info.objects.create(
            urgency=request.POST.get('urgency'),
            customer_id=request.POST.get('customer_id'),
            complained_through=request.POST.get('complained_through'),
            name=request.POST.get('name'),
            mobile_no=request.POST.get('mobile_no'),
            remarks=str(request.POST.get('remarks'))
            )
        # # Convert the JSON data to a Python list
        stored_queries = json.loads(stored_queries_json)
        comp_id = complaints_info.objects.filter(complained_through=request.POST.get('complained_through')).order_by('-auto_id').first()
        
        print(comp_id.complain_id)

        # Process the stored_queries data (you can save it to the database, etc.)
        for query in stored_queries:
            # Perform actions with each query, e.g., save to the database
            complain_details.objects.create(
                complain_id=comp_id,
                category = query['category'],
                query= query['query'],
                other_query = query['other_query']
            )
            print(f"Category: {query['category']}, Query: {query['query']},Other Query : {query['other_query']}")
            
        complaint_info = get_object_or_404(complaints_info, complain_id=str(comp_id.complain_id))
        complaint_details_list = complain_details.objects.filter(complain_id=complaint_info)
        # Return a response or redirect to another page
        return render(request, 'ticket/single_report.html', {'complaint_info': complaint_info,'complaint_details_list': complaint_details_list,})
        # return HttpResponse(stored_queries)

    return render(request, 'raise_ticket.html', {'form': form})

def get_queries(request):
    category = request.GET.get('category', None)
    if category:
        queries = Frequest_query_set.objects.filter(category=category).values_list('query')
        data = {'queries': list(queries)}
        # print(data)
        return JsonResponse(data)
    return JsonResponse({'queries': []})


def readonly_report(request):
    # Retrieve data from the models and merge based on complain_id
    complaints = complaints_info.objects.all()
    details = complain_details.objects.all()

    # Create a dictionary to store merged data
    report_data = {}

    for complaint in complaints:
        report_data[complaint.complain_id] = {
            'complaint_info': complaint,
            'complaint_details': details.filter(complain_id=complaint)
        }

    # Pass the merged data to the template
    return render(request, 'ticket/report.html', {'report_data': report_data})