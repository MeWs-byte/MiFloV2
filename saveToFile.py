import json


with open('score.json', 'r') as fp:
    score = json.load(fp) 
    # @TODO: handle errors if the file doesn't exist or is empty

    print(type(score))

score = score + 24
with open('score.json', 'w') as fp:
    json.dump(score, fp)


    
with open('score.json', 'r') as fp:
    printed_ids = json.load(fp) 
    # @TODO: handle errors if the file doesn't exist or is empty

    print(printed_ids)