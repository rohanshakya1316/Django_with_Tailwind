from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, StudentForm

# For model form
def student_register(request):
    if request.method == "POST":
        print("POST Data: ", request.POST)
        form = StudentForm(request.POST)

        if not form.is_valid():
            print("------- Invalid Form ------", form.errors)
            context = {'new_form': form}
            return render(request, "app/student_register.html", context)
        print("Form is fine")
        # save in the database
        form.save()

        return redirect("student_register")
    
    form = StudentForm()
    context = {
        "new_form" : form
    }
    return render(request, "app/student_register.html", context)


# For General Form
# def student_register(request):
#     if request.method == "POST":
#         print("POST Data: ", request.POST)
#         form = StudentRegisterForm(request.POST)

#         if not form.is_valid():
#             print("------- Invalid Form ------", form.errors)
#             context = {'form': form}
#             return render(request, "app/student_register.html", context)
#         print("Form is fine")
#         # save in the database

#         return redirect("student_register")
    
#     form = StudentRegisterForm()
#     context = {
#         "form" : form
#     }
#     return render(request, "app/student_register.html", context)

# def student_register(request):
#     print(f"------------------ {request.method} ------------------")

#     if request.method == 'POST':
#         print("Post data: ", request.POST)

#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         address = request.POST.get("address")
#         phone = request.POST.get("phone")

#         print(f"Name: ", first_name, last_name)
#         print(f"Address: ", address)
#         print(f"Phone: ", phone)

#         errors = {}
#         # Save in database
#         if not len(phone) == 10: 
#             errors['phone'] = "Phone number must be exactly 10 digits."
        
#         if len(errors.keys()) > 0: 
#             form_data = {
#                 'first_name' : first_name,
#                 'last_name' : last_name,
#                 'address' : address,
#                 'phone' : phone, 
#             }

#             context = {
#                 'errors' : errors,
#                 'form_data' : form_data,
#             }
#             return render(request, 'app/student_register.html', context)
    
#     return render(request, 'app/student_register.html')

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