from django.shortcuts import render

# Create your views here.
def student(request):
    return render(request, "app/student.html")

def home(request):
    # stats = {
    #     'Total Students': 1250, 
    #     'Total Payments': 'Rs. 300000',
    #     'Pending Payments': 'Rs. 55000',
    #     'Active Classes': 34
    # }

    stats = [
        {
            'title': 'Total Students',
            'value': '1250',
            'text_color': 'text-primary'
        }, 
        {
            'title': 'Total Payments',
            'value': 'Rs. 300000',
            'text_color': 'text-green-600'
        }, 
        {
            'title': 'Pending Payments',
            'value': 'Rs. 55000',
            'text_color': 'text-red-600'
        }, 
        {
            'title': 'Active Classes',
            'value': '34',
            'text_color': 'text-secondary'
        }, 

    ]

    context = {
        'stats' : stats
    }

    return render(request, "app/dashboard.html", context)