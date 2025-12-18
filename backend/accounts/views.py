from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import UserData
import json

@csrf_exempt
def signup_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return JsonResponse({"error": "All fields required"}, status=400)

        if UserData.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        UserData.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        return JsonResponse({"message": "Signup successful"}, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from .models import UserData
import json

@csrf_exempt
def login_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({"error": "All fields required"}, status=400)

        try:
            user = UserData.objects.get(username=username)
        except UserData.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        if check_password(password, user.password):
            return JsonResponse({"message": "Login success"}, status=200)
        else:
            return JsonResponse({"error": "Invalid password"}, status=401)

    except Exception as e:
        # 🔥 THIS LINE HELPS DEBUG
        return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)


