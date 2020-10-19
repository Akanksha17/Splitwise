# add expense: u1 1200 4 u1 u2 u3 u4 exact 10 20 30 40
# settle up u1 u2 300

from src.controller import expense as expense_controller
from src.validation import is_action_valid
from src.constants import output_messages, valid_actions


def process_expense_addition_input(input_cmd):
    payer_id = input_cmd[0]
    amount = int(input_cmd[1])
    number_of_users_involved = int(input_cmd[2])
    user_ids = []
    for idx in range(number_of_users_involved):
        u_id = input_cmd[3 + idx]
        user_ids.append(u_id)
    cur_idx = 2 + number_of_users_involved + 1
    split_type = input_cmd[cur_idx]
    return payer_id, amount, user_ids, split_type, cur_idx


def execute_expense_addition(input_list, splitwise_instance):
    payer_id, amount, user_ids, split_type, current_idx = process_expense_addition_input(input_list)
    if current_idx == len(input_list) - 1:
        rem_input = []
    else:
        rem_input = input_list[current_idx+1:]
    execution_result = expense_controller.create_expense(
        payer_id, amount, user_ids, split_type, rem_input, splitwise_instance)
    return execution_result


def execute(user_input, splitwise_instance):
    action = user_input[0]
    if not is_action_valid(action):
        return {
            'error_message': output_messages['INVALID_ACTION']
        }

    if action.upper() == valid_actions['ADD_EXPENSE']:
        added_expense_result = execute_expense_addition(user_input[1:], splitwise_instance)

        return added_expense_result
