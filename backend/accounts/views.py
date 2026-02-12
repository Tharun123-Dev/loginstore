from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json

@csrf_exempt
def signup(request):

    if request.method != "POST":
        return JsonResponse({"message": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"message": "Invalid JSON data"}, status=400)

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 🔹 Field validations
    if not username or not email or not password:
        return JsonResponse(
            {"message": "All fields are required"},
            status=400
        )

    # 🔹 Username length check
    if len(username) < 3:
        return JsonResponse(
            {"message": "Username must be at least 3 characters"},
            status=400
        )

    # 🔹 Password validation
    if len(password) < 6:
        return JsonResponse(
            {"message": "Password must be at least 6 characters"},
            status=400
        )

    # 🔹 Email format validation
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse(
            {"message": "Invalid email format"},
            status=400
        )

    # 🔹 Duplicate username check
    if User.objects.filter(username=username).exists():
        return JsonResponse(
            {"message": "Username already exists"},
            status=400
        )

    # 🔹 Duplicate email check
    if User.objects.filter(email=email).exists():
        return JsonResponse(
            {"message": "Email already registered"},
            status=400
        )

    # 🔹 Create user
    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return JsonResponse(
        {"message": "Signup successful"},
        status=201
    )

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def user_login(request):

    if request.method != "POST":
        return JsonResponse(
            {"message": "Invalid request method"},
            status=405
        )

    # 🔹 Check valid JSON
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse(
            {"message": "Invalid JSON data"},
            status=400
        )

    username = data.get("username")
    password = data.get("password")

    # 🔹 Empty field validation
    if not username or not password:
        return JsonResponse(
            {"message": "Username and password are required"},
            status=400
        )

    # 🔹 Authenticate user
    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is None:
        return JsonResponse(
            {"message": "Invalid username or password"},
            status=401
        )

    # 🔹 Check if user is active
    if not user.is_active:
        return JsonResponse(
            {"message": "Account is disabled"},
            status=403
        )

    # 🔹 Create session
    login(request, user)

    return JsonResponse(
        {
            "message": "Login successful",
            "username": user.username,
            "email": user.email
        },
        status=200
    )


from django.http import JsonResponse

from django.http import JsonResponse
from django.http import JsonResponse

def profile(request):
    if not request.user.is_authenticated:
        return JsonResponse({"message": "Not logged in"}, status=401)

    user = request.user

    return JsonResponse({
        "username": user.username,
        "email": user.email,
    })
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})

from .models import Train
from django.http import JsonResponse

def search_trains(request):
    source = request.GET.get("source")
    destination = request.GET.get("destination")

    trains = Train.objects.filter(
        source__icontains=source,
        destination__icontains=destination
    )

    data = []

    for train in trains:
        data.append({
            "train_number": train.train_number,
            "train_name": train.train_name,
            "source": train.source,
            "destination": train.destination,
            "departure_time": train.departure_time,
            "arrival_time": train.arrival_time,
        })

    return JsonResponse(data, safe=False)
