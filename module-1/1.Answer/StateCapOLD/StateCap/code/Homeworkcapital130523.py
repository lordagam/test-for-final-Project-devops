STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}

#1
"""
def find_capital(state):
    if state in STATES_CAPITALS:
        return STATES_CAPITALS[state]
    else:
        return "Capital not found for the given state."
"""
"""
1
# Example usage:
state_name = 'Idaho'
capital_name = STATES_CAPITALS[state_name]
print(f"The capital of {state_name} is {capital_name}.")
"""


#2
print("The states are: ")
for state in STATES_CAPITALS.keys():
    print(state)

print("End of states list")


#3
print("The capitals in the states list are: ")
for capital in STATES_CAPITALS.values():
    print(capital)

print("End of capitals list")

print("The States & Capitals are :")
state_capital_pairs = []
for state, capital in STATES_CAPITALS.items():
    state_capital_pairs.append(f'{state} -> {capital}')

print(state_capital_pairs)
print("End list of States & Capitals ")


print("The sorted States & Capitals are :")
state_capital_pairs = []
for state, capital in sorted(STATES_CAPITALS.items()):
        state_capital_pairs.append(f'{state} -> {capital}')

print(state_capital_pairs)
print("End list of sorted States & Capitals ")

def get_state(capital):
    for state, capital_name in STATES_CAPITALS.items():
        if capital_name == capital:
            return state
    return "No state found for the given capital."

# Example usage:
capital_name = 'Montgomery'
state_name = get_state(capital_name)
print(f"The state corresponding to the capital {capital_name} is {state_name}.")


def get_state(capital):
    matching_states = []
    for state, capital_name in STATES_CAPITALS.items():
        if capital_name == capital:
            matching_states.append(state)
    if matching_states:
        return matching_states
    else:
        return "No state found for the given capital."

def get_state_by_capital(capital):
    states = get_state(capital)
    if isinstance(states, list):
        return f"The capital {capital} is associated with the following state(s): {', '.join(states)}."
    else:
        return states

# Example usage:
capital_name = 'Montgomery'
state = get_state_by_capital(capital_name)
print(state)

def get_state(capital):
    matching_states = []
    for state, capital_name in STATES_CAPITALS.items():
        if capital_name == capital:
            matching_states.append(state)
    if matching_states:
        return matching_states
    else:
        return "No state found for the given capital."

# Example usage:
capital_name = 'Washington, D.C.'
states = get_state(capital_name)
if isinstance(states, list):
    print(f"The capital {capital_name} is associated with the following states: {', '.join(states)}.")
else:
    print(states)


