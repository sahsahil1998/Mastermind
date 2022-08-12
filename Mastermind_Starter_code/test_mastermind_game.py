
from mastermind_class import generate_answer, game_logic

COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'black']


def test_generate_answer():
    code = generate_answer()
    print(code)
    if len(code) != 4:
        print ('Function Error')
    else:
        print ('Length Check Passed')

    for i in code:
        if i in COLORS:
            print ('All Colors in COLORS')
        else:
            print('Color not in list')
    return code

def test_game_logic():
    

def main():

    test_generate_answer()

        
if __name__ == '__main__':
    main()
