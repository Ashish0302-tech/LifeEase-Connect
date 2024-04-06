from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    return render(request, 'users/home.html')


def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        print(email)
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        user = User.objects.create(name=name, age=age, gender=gender, height=height, weight=weight, email=email)
        bmi = user.calculate_bmi()

        email_subject = 'Your BMI Information'
        email_template = 'email_template.html'
        email_content = render_to_string(email_template, {'user': user})
        

        send_mail(
            email_subject,
            email_content,
            'ashishkalwar03@gmail.com',
            [email],
            html_message=email_content
            )
        return render(request, 'users/display_bmi.html', {'user': user, 'bmi': bmi})
    return render(request, 'users/create_user.html')



def display_users(request):
    users = User.objects.all()
    return render(request, 'users/display_users.html', {'users': users})

def remove_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('display_users')
    return render(request, 'users/remove_user.html', {'user': user})

def view_plan(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/view_plan.html', {'user': user})

def view_plan2(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/view_plan2.html', {'user': user})

def view_plan3(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/view_plan3.html', {'user': user})

def diet_plan(request):
    return render(request, 'users/diet_plan.html')

def exercise_plan(request):
    return render(request, 'users/exercise_plan.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def docters(request):
    return render(request, 'docters.html')