# coding=utf-8
# returns list of 3 items with title, description and lack message
def get_matching_loans(client_data):
    # initialize loans
    conditions, titles, descriptions, links = initialize_loans()

    similarity_dict = {}
    for i in range(0, 8):
        similarity_dict[i] = compare_loans(conditions[i], client_data)

    # sorting similarity dict
    sorted_dict = [(k, similarity_dict[k]) for k in sorted(similarity_dict, key=similarity_dict.get, reverse=True)]
    ret_val = []
    for i in range(4):
        temp_item = {}
        this_index = sorted_dict[i][0]
        temp_item['title'] = titles[this_index]
        temp_item['description'] = descriptions[this_index]
        temp_item['link'] = links[this_index]
        temp_item['lack'] = sorted_dict[this_index][1][1]
        ret_val.append(temp_item)

    return ret_val


# initialization of all possible loans
def initialize_loans():
    conditions = []
    titles = []
    descriptions = []
    links = []

    # create for every
    titles.append('Housing loan for EU Citizens')
    descriptions.append('Life is like a team sport – housing loans tailor-made for you')
    conditions.append(create_loan('Loan', intention='house', insurance='mortgage', citizenship='EU'))
    links.append('http://www.skb.si/en/personal-banking/loans/housing-loan-for-eu')

    titles.append('Housing loan')
    descriptions.append('Life is like a team sport – housing loans tailor-made for you')
    conditions.append(create_loan('Loan', intention='house', citizenship='Slo', income=1,
                                  interest='Fixed'))
    links.append('http://www.skb.si/en/personal-banking/loans/housing-loan')

    titles.append('Quick Housing loan')
    descriptions.append('The quickest way to giving your home a new look.')
    conditions.append(create_loan('Loan', intention='house', citizenship='Slo', income=1, interest='Fixed',
                                 buy_insurance=True, urgency=3))
    links.append('http://www.skb.si/en/personal-banking/loans/quick-housing-loan')

    titles.append('Cash loan')
    descriptions.append('Quick solution for unexpected financial expenses')
    conditions.append(create_loan('Loan', intention='other', citizenship='Slo', income=1, interest='Fixed'))
    links.append('http://www.skb.si/en/personal-banking/loans/cash-loan')

    titles.append('Quick cash loan')
    descriptions.append('First aid for unexpected financial expenses')
    conditions.append(create_loan('Loan', intention='other', urgency=3, bank='SKB', insurance='no'))
    links.append('http://www.skb.si/en/personal-banking/loans/quick-cash-loan')

    titles.append('Car loan')
    descriptions.append('Are you looking for favourable financing for purchasing a new car?')
    conditions.append(create_loan('Loan', intention='car', bank='SKB'))
    links.append('http://www.skb.si/en/personal-banking/loans/car-loan')

    titles.append('Lombard loan')
    descriptions.append('Lombard loan enables you to acquire a loan by pledging your own assets (term deposit).')
    conditions.append(create_loan('Loan', citizenship='Slo', bank='SKB', insurance='loan', interest='Fixed'))
    links.append('http://www.skb.si/en/personal-banking/loans/lombard-loan')

    titles.append('1-hour loan')
    descriptions.append('Favourable loan at the last moment')
    conditions.append(create_loan('Loan', urgency=1))
    links.append('http://www.skb.si/en/personal-banking/loans/1-hour-loan')

    return conditions, titles, descriptions, links

default_key_set = ['type', 'intention', 'age', 'income', 'urgency', 'insurance', 'citizenship', 'interest',
                   'buy_insurance', 'bank']


# help method for creating loans based on their attributes
def create_loan(loan_type, intention=None, age=None, income=None, urgency=None, insurance=None,
                citizenship=None, interest=None, buy_insurance=None, bank=None):
    # create empty dictionary
    conditions = {}

    # prepare all fields
    conditions['type'] = loan_type
    conditions['intention'] = intention
    conditions['age'] = age
    conditions['income'] = income
    conditions['urgency'] = urgency
    conditions['insurance'] = insurance
    conditions['citizenship'] = citizenship
    conditions['interest'] = interest
    conditions['buy_insurance'] = buy_insurance
    conditions['bank'] = bank

    return conditions


def compare_loans(loan, client):
    message = "Disproportion with these attributes: "
    ret_val = 0
    for key in default_key_set:

        if loan[key] is None and client[key] is None:
            ret_val += 1

        elif loan[key] is not None and client[key] is not None:
            if key == 'urgency':
                if client['urgency'] <= loan['urgency']:
                    ret_val += 100
            elif key == 'income':
                if client['income'] > 0:
                    ret_val += 100
            else:
                if loan[key] == client[key]:
                    ret_val += 100
                else:
                    message += str(key) + ', '

    if message.endswith(', '):
        message = message[:-2]

    return ret_val, message
