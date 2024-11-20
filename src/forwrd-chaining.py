# forward chaining

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
    
    flage = True # for while loop
    while flage:
        flage = False
        for key in knowledge_base:
            for key_ in knowledge_base[key]:
                if key_ in facts:
                    flage = True
                    facts.add(knowledge_base[key][key_])
                    if query == key:
                        return f'{name} {query} is {knowledge_base[key][key_]}'
    return f'{name} {query} is Unknown'

facts.add('chirps&sings')

print(answer('color', 'Fritz'))
print(facts)
