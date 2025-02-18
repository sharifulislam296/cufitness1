import json, random
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
    """Renders the home page with a motivational quote."""
    # Define a list of motivational quotes
    motivational_quotes = [
        "The only bad workout is the one that didn't happen.",
        "Sweat is just fat crying.",
        "The body achieves what the mind believes.",
        "Push yourself, because no one else is going to do it for you.",
        "Fitness is not about being better than someone else; it's about being better than you used to be.",
        "Don't limit your challenges—challenge your limits.",
        "The pain you feel today will be the strength you feel tomorrow."
    ]
    # Pick a random quote
    quote = random.choice(motivational_quotes)
    # Pass the quote to the template
    context = {
        'motivational_quote': quote
    }
    return render(request, 'users/home.html', context)


def user_logout(request):
    """Logs out the user and redirects to the home page."""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')


def register(request):
    """Handles user registration and sends a confirmation email."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        subject = 'Registration Confirmation'
        message = (
            f'Hi {username},\n\n'
            'Thank you for signing up at CUFitness! Your registration was successful.'
        )
        from_email = settings.EMAIL_HOST_USER if hasattr(settings,
                                                         'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER else 'no-reply@cufitness.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, "Registration successful! A confirmation email has been sent.")
        return redirect('home')

    return render(request, 'users/register.html')


@login_required
def profile(request):
    """Displays the user's profile."""
    return render(request, 'users/profile.html')

