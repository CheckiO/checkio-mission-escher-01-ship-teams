"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": {'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19},
            "answer": [['Abrahams', 'Coleman'], ['Smith', 'Wesson']]
        },
        {
            "input": {'Fernandes': 18, 'Johnson': 22, 'Kale': 41, 'McCortney': 54},
            "answer": [['Fernandes', 'Kale', 'McCortney'], ['Johnson']]
        }
    ],
    "Extra": [
        {
            "input": {'Samuelson': 19.99, 'Besson': 28, 'Rick': 39.95, 'Wayfarer': 40.1},
            "answer": [['Samuelson', 'Wayfarer'], ['Besson', 'Rick']]
        },
        {
            "input": {'Alonso': 18.5, 'Batista': 31, 'Rurk': 42.5, 'Lincoln': 56},
            "answer": [['Alonso', 'Lincoln', 'Rurk'], ['Batista']]
        },
        {
            "input": {'Pitty': 19, 'Wolf': 40.005, 'Doberman': 42, 'Bobber': 18},
            "answer": [['Bobber', 'Doberman', 'Pitty', 'Wolf'], []]
        },
        {
            "input": {'Carlos': 34, 'Richardson': 20, 'Dow': 40},
            "answer": [[], ['Carlos', 'Dow', 'Richardson']]
        },
        {
            "input": {'Dave': 24},
            "answer": [[], ['Dave']]
        },
        {
            "input": {'Hubert': 38.3, 'Barney': 31, 'Kirk': 42.5, 'Lion': 56},
            "answer": [['Kirk', 'Lion'], ['Barney', 'Hubert']]
        },
        {
            "input": {'Sam': 19},
            "answer": [['Sam'], []]
        },
        {
            "input": {'Karl': 17, 'Richard': 20, 'Dantes': 39, 'Fargo': 19},
            "answer": [['Fargo', 'Karl'], ['Dantes', 'Richard']]
        }
    ]
}
