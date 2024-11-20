# backward chaining

knowledge_base = {
    'type' : {
        'croaks&eats flies' : 'frog',
        'chirps&sings' : 'canary'
    },
    'color' : { 
        'frog' : 'green',
        'canary' : 'yellow'
    },
    'rgb' : {
        'yellow' : '(255,255,0)',
        'green' : '(0,255,0)'
    }
}

facts = set()

def answer(query:str, name:str) -> str:
    # push first concludes
    goals = set()
    for key in knowledge_base[query]:
        goals.add(key)
    
    # search in one iterate
    for key in knowledge_base:
        for key_ in knowledge_base[key]:
            if key_ in facts and knowledge_base[key][key_] in goals:
                facts.add(knowledge_base[key][key_])
            if key_ in facts:
                facts.add(knowledge_base[key][key_])
            if key == query and key_ in facts:
                return(f'{name} {query} is {knowledge_base[key][key_]}')

    return(f'{name} {query} is Unkown')


facts.add('chirps&sings')

print(answer('type', 'Fritz'))