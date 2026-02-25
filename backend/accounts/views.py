from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Train


# 🔹 SIGNUP VIEW
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

    if not username or not email or not password:
        return JsonResponse({"message": "All fields are required"}, status=400)

    if len(username) < 3:
        return JsonResponse({"message": "Username must be at least 3 characters"}, status=400)

    if len(password) < 6:
        return JsonResponse({"message": "Password must be at least 6 characters"}, status=400)

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"message": "Invalid email format"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"message": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"message": "Email already registered"}, status=400)

    User.objects.create_user(username=username, email=email, password=password)

    return JsonResponse({"message": "Signup successful"}, status=201)


# 🔹 JWT LOGIN VIEW
@csrf_exempt
def jwt_login(request):

    if request.method != "POST":
        return JsonResponse({"message": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"message": "Invalid JSON data"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"message": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"message": "Invalid credentials"}, status=401)

    if not user.is_active:
        return JsonResponse({"message": "Account disabled"}, status=403)

    # 🔥 Generate JWT Tokens
    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        "message": "Login successful",
        "access": str(refresh.access_token),   # ✅ FIXED KEY
        "refresh": str(refresh),               # ✅ FIXED KEY
        "username": user.username,
        "email": user.email
    }, status=200)


# 🔹 JWT PROFILE (USE THIS ONLY)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jwt_profile(request):

    user = request.user

    return JsonResponse({
        "username": user.username,
        "email": user.email
    })


# 🔹 PROFILE (MODIFIED TO USE JWT AUTH)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):

    user = request.user

    return JsonResponse({
        "username": user.username,
        "email": user.email,
    })


# 🔹 LOGOUT
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})


# 🔹 SEARCH TRAINS (PROTECTED)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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