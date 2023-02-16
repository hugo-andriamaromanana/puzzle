import json


def get_data(name):
    with open("json/"+f"{name}.json") as f:
        data = json.load(f)
    return data

def dump_data(name, data):
    with open("json/"+f"{name}.json", 'w') as f:
        json.dump(data, f,indent=4)


settings = get_data('settings')
scores = get_data('best_scores')

