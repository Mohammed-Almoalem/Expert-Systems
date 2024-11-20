# Expert System cf from the user

knowledgeBase = {
    'lights weak cf=100' : 'battery bad cf=50',
    'radio weak cf=100' : 'battery bad cf=50',
    'not turn over cf=100&battery bad cf=50&battery bad cf=50' : 'Problem is battery cf=100',
    'turn over cf=100&smell gas cf=100' : 'Problem is flooded cf=80',
    'turn over cf=100&gas gauge is empty cf=100' : 'Problem is out of gas cf=90',
    'turn over cf=100&gas gauge is low cf=100' : 'Problem is out of gas cf=30'
}

# in rule 3, we put 2 of battery bad with cf=50, because the rule
# didn't include the cf for the battery bad, which means it is 100 or 1.0,
# and that leads to the both rules to be executed

facts = set()
problems = set()

def set_cf(var:str, val:int) -> str :

    try:
        var = var[:var.index('=')+1] + f'{val}'
        return var

    except:
        print('Error while setting the CF')

def get_cf(var:str) -> int :
    
    try:
        val = var[var.index("=")+1:]
        return int(val)
        
    except:
        print('Error while getting the CF')

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
        
        cf = int(input("Cf > "))

        if cf > 100 or cf < 1:
            raise ValueError
        
        facts.add(f'{options[choice-1]} cf={cf}')
        print(f'{options[choice-1]} cf={cf}')
    
    except:
        print('\ntry again\n')
        ask(q=q,options=options)    
    
    print('\n')
    
def sol() -> None:

    for key in knowledgeBase:

        temp = key.split('&')
        
        flage = True # all true 

        CFs = []
        
        for holder in temp:
            if holder not in facts: # first search
                flage_ = False # the second search
                for fact in facts:
                    if (fact[:fact.find('cf=')]) == (holder[:holder.find('cf=')]):
                        holder = fact
                        CFs.append(holder)
                        flage_ = True
                        break
                
                if not flage_:
                    flage = False
                break

            else:
                CFs.append(holder)
        
        if not flage: # one of the rules in the if statement is not true
            continue # main loop

        else:
            min_cf = 9999
            for cf in CFs:
                if get_cf(cf) < min_cf :
                    min_cf = get_cf(cf)
            knowledgeBase[key] = set_cf(knowledgeBase[key], int( min_cf * get_cf(knowledgeBase[key]) / 100)) # RuleCF * conclusionCF / 100
            facts.add(knowledgeBase[key])
            problems.add(knowledgeBase[key])

    print("Problems\n")

    for p in problems:
        print(f'{p}\n')

    print("Problem done\n")

# Combining Rule CF and conclusion CF

# if x cf=n && y cf=m then z cf=q

# 1. take the minimum between ( n and m )
# 2. compute the CF for the conclusion : Rule CF(minimum if many) * conclusion CF / 100

ask('Does the engine turn over ?', ['turn over', 'not turn over'])
ask('Do you smell gas ?', ['smell gas', 'not smell gas'])
ask('What does the gas gauge say ?', ['gas gauge is low', 'gas gauge is empty', 'gas gauge is full'])

sol()