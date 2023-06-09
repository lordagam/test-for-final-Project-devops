"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys

import pytest

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


def capital_of_Idaho():
    #-1- Your code here
    state_name = 'Idaho'
    capital_name = STATES_CAPITALS[state_name]
    print(f"The capital of {state_name} is {capital_name}.")

    pass

def all_states():
    #-2- Your code here
    print("The states are: ")
    for state in STATES_CAPITALS.keys():
        print(state)
    print("End of states list")

    pass

def all_capitals():
    #-3- Your code here
    print("The capitals in the states list are: ")
    for capital in STATES_CAPITALS.values():
        print(capital)
    print("End of capitals list")

    pass

def states_capitals_string():
    #-4- Your code here
    print("The States & Capitals are :")
    state_capital_pairs = []
    for state, capital in STATES_CAPITALS.items():
        state_capital_pairs.append(f'{state} -> {capital}')

    print(state_capital_pairs)
    print("End list of States & Capitals ")

   #-5- Sorted States & Capitals
    print("The sorted States & Capitals are :")
    state_capital_pairs = []
    for state, capital in sorted(STATES_CAPITALS.items()):
        state_capital_pairs.append(f'{state} -> {capital}')

    print(state_capital_pairs)
    print("End list of sorted States & Capitals ")

    pass



def get_state(capital):
    for state, capital_name in STATES_CAPITALS.items():
        if capital_name == capital:
            return state

    return "No state found for the given capital."

pass
#to check the code of case the capital is worng
#GOTCHAS: What happens if two states have the same capital name
"""
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

            
"""




def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
