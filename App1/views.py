import json

from django.http import JsonResponse
from django.views import View

from App1.models import User


class SignUpView(View):
    def post(self, request):

        data = json.load(request.body)

        User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = data['phone_number']
        )

        return JsonResponse({"message":"Created"},status=201)

