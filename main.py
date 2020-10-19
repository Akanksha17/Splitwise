import initialise_script
from src.constants import valid_actions
from src.action import execute

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Splitwise Application', '\n')
    sample_users = initialise_script.generate_sample_users()
    print('Available user ids:')

    for user in sample_users:
        print(user.get_id(), end=', ')
    print('\n')
    print('Available commands:')

    for key, value in valid_actions.items():
        print(value, end=', ')
    print('\n')
    user_input = input('Enter command:')
    result = execute(user_input, sample_users)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
