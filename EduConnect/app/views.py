from django.shortcuts import render , redirect
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


 
def homepage_view(request):
    return render(request, "app/homepage.html")

@login_required
def dashboard(request):
    return render(request,"app/dashboard.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) #Initialize the form with POST data.
        if form.is_valid(): #validte the form
            form.save()  # Save the new user to the database.
            return redirect('login')   # Redirect to the login page.
        
    else :
        form = CustomUserCreationForm() #Show the blank form for GET requests. for the user to fill in.

    return render(request ,  "registration/signup.html" , {"form": form}) #render the form