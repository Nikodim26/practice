import json


def my_decorator(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        report = f'Было {len(result)} транзакции суммарной стоимостью {sum([i['amount'] for i in result])}'
        print(report)
        return result

    return wrapper


@my_decorator
def filters_transactions(currency):
    with open('data.json') as file:
        obj_filtered = list(filter(lambda x: x['currency'] == currency, json.load(file)))

    with open('data_filter.json', 'w') as file:
        json.dump(obj_filtered, file, indent=4)
    return obj_filtered


if __name__ == '__main__':
    filters_transactions('EUR')
