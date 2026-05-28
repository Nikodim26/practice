import json

str_json = '''[
    {
        "date": "2021-05-01",
        "amount": 1000,
        "currency": "USD",
        "description": "Salary"
    },
    {
        "date": "2021-05-02",
        "amount": -50,
        "currency": "EUR",
        "description": "Dinner"
    },
    {
        "date": "2021-05-03",
        "amount": -20,
        "currency": "USD",
        "description": "Coffee"
    },
    {
        "date": "2021-05-04",
        "amount": 200,
        "currency": "GBP",
        "description": "Gift"
    }
]'''


def my_decorator(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        print(len(result))
        return result

    return wrapper


@my_decorator
def filters_transactions(json_str, currency):
    str_filtered = list(filter(lambda x: x['currency'] == currency, json.loads(str_json)))
    return json.dumps(str_filtered, indent=4)


if __name__ == '__main__':
    print(filters_transactions(str_json, 'EUR'))
