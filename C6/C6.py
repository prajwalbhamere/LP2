# Implement any one of the following Expert System 
# I	    Information management 
# II	Hospitals and medical facilities 
# III	Help desks management 
# IV	Employee performance evaluation 
# V	    Stock market trading 
# VI	Airline scheduling and cargo schedules 

def rule1(sym):
    if 'fever' in sym and 'cough' in sym and 'fatigue' in sym:
        return 'You may have the flu'
    return None

def rule2(sym):
    if 'fever' in sym and 'rash' in sym and 'headache' in sym:
        return 'You may have meningitis'
    return None

def rule3(sym):
    if 'pain' in sym and 'swelling' in sym and 'bruising' in sym:
        return 'You may have a fracture'
    return None

def rule4(sym):
    if 'abdominal pain' in sym and 'diarrhoea' in sym and 'nausea' in sym:
        return 'You may have food poisoning'
    return None

def rule5(sym):
    if 'shortness of breath' in sym and 'chest pain' in sym and 'dizziness' in sym:
        return 'You may be having a heart attack. Please seek medical attention'
    return None

def diagnose(sym):
    rules = [rule1, rule2, rule3, rule4, rule5]
    results = []
    for rule in rules:
        result = rule(sym)
        if result:
            results.append(result)
    if len(results) == 0:
        return "Sorry, we couldn't diagnose your medical condition"
    elif len(results) == 1:
        return results[0]
    else:
        return "You may have multiple conditions: " + ",".join(results)
    
sym = ['fever', 'rash', 'headache', 'swelling', 'bruising', 'pain']
result = diagnose(sym)
print(result)