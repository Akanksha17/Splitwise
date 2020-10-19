import initialise_script
from src.constants import valid_actions
from src.action import execute

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Splitwise Application', '\n')
    splitwise_instance = initialise_script.initialise_app()

    print('Available user ids:')

    for user in splitwise_instance.users:
        print(user.get_id(), end=', ')
    print('\n')
    print('Available commands:')

    for key, value in valid_actions.items():
        print(value, end=', ')
    print('\n')
    user_input = input('Enter command:')
    result = execute(user_input, splitwise_instance)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
