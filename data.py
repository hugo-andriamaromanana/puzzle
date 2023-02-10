import json 

def get_data(name):
    with open("json/"+f"{name}.json") as f:
        data = json.load(f)
    return data

settings = get_data('settings')
scores = get_data('best_scores')