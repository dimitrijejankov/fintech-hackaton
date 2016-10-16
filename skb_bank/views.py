import json
from django.http import JsonResponse
from django.views.generic import View
from skb_bank.utils import get_matching_loans
from django.views.decorators.csrf import csrf_exempt


class RestView(View):
    def post(self, request):
        try:
            json_values = json.loads(request.body)
            return JsonResponse(get_matching_loans(json_values), status=200, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'Bad request'}, status=400)
