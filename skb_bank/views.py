import json
from django.http import JsonResponse
from django.views.generic import View
from skb_bank.utils import get_matching_loans
from .models import Clients


class RestView(View):
    def post(self, request):
        try:
            json_values = json.loads(request.body.decode("utf-8"))

            this_age = json_values['age']
            age = 5
            if this_age == '18-27':
                age = 1
            elif this_age == '28-40':
                age = 2
            elif this_age == '41-55':
                age = 3
            elif this_age == '56-65':
                age = 4

            this_bank = json_values['bank']
            bank = 3
            if this_bank == 'SKB':
                bank = 1
            elif this_bank == 'other':
                bank = 2

            this_buy_insurance = json_values['buy_insurance']
            buy_insurance = 1
            if this_buy_insurance is False:
                buy_insurance = 0

            this_citizenship = json_values['citizenship']
            citizenship = 3
            if this_citizenship == 'Slo':
                citizenship = 1
            elif this_citizenship == 'EU':
                citizenship = 2

            this_income = json_values['income']

            this_insurance = json_values['insurance']
            insurance = 4
            if this_insurance == 'mortgage':
                insurance = 1
            elif this_insurance == 'loan-insurance':
                insurance = 2
            elif this_insurance == 'guarantee':
                insurance = 3

            this_intention = json_values['intention']
            intention = 3
            if this_intention == 'car':
                intention = 1
            elif this_intention == 'house':
                intention = 2

            this_interest = json_values['interest']
            interest = 2
            if this_interest == 'Fixed':
                interest = 1

            this_type = json_values['type']
            tip = 3
            if this_type == 'Loan':
                tip = 1
            elif this_type == 'Insurance':
                tip = 2

            this_urgency = json_values['urgency']

            client = Clients.objects.create(age=age, bank=bank, buy_insurance=buy_insurance, citizenship=citizenship,
                                            income=this_income, insurance=insurance, intention=intention,
                                            interest=interest, type=tip, urgency=this_urgency)
            client.save()

            return JsonResponse(get_matching_loans(json_values), status=200, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'Bad request'}, status=400)
