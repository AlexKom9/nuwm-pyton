from PyInquirer import prompt

month_hash = {
    'january': 31,
    'february': '28 or 29',
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}

select_month_question = {
    'type': 'list',
    'name': 'month',
    'message': 'Please choose month to check days amount',
    'choices': month_hash.keys()
}

selected_month_query = prompt(select_month_question)
month = selected_month_query['month']

print(f"{month.capitalize()} has {month_hash[month]} days")
