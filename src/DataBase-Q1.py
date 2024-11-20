# Expert System cf withing the knowledgebase

knowledgeBase = {
    'lights weak' : 'battery bad cf=50',
    'radio weak' : 'battery bad cf=50',
    'not turn over&battery bad cf=50&battery bad cf=50' : 'Problem is battery',
    'turn over&smell gas' : 'Problem is flooded cf=80',
    'turn over&gas gauge is empty' : 'Problem is out of gas cf=90',
    'turn over&gas gauge is low' : 'Problem is out of gas cf=30'
}

facts = set()
problems = set()

def ask(q:str, options:list) -> None: 

    i = 1
    
    print(f'\n> {q}\n')

    for op in options:
        print(f'{i} . {op}\n')
        i=i+1
    
    try:
        choice = int(input('choice number > '))
        
        if choice not in range(1,len(options)+1):
            raise ValueError
        
        facts.add(options[choice-1])
        print(options[choice-1])
    
    except:
        print('\ntry again\n')
        ask(q=q,options=options)    
    
    print('\n')
    
def sol() -> None:
    
    for key in knowledgeBase:

        temp = key.split('&')
        
        flage = True # all true 
        
        for holder in temp:
            if holder not in facts:
                flage = False
                break
        
        if not flage:
            continue # main loop

        else:
            facts.add(knowledgeBase[key])
            problems.add(knowledgeBase[key])

    print("Problems\n")

    for p in problems:
        print(f'{p}\n')

    print('problem done\n')

ask('Does the engine turn over ?', ['turn over', 'not turn over'])
ask('Do you smell gas ?', ['smell gas', 'not smell gas'])
ask('What does the gas gauge say ?', ['gas gauge is low', 'gas gauge is empty', 'gas gauge is full'])

sol()