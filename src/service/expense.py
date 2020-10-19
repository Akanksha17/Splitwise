from src.model import expense as expense_model
from src.service import split as split_service
from src.constants import output_messages


def create_expense(payer_id, amount, user_ids, split_type, rem_input, splitwise_instance):
    sample_users = splitwise_instance.users
    if len(rem_input) > 0:
        share_unit = rem_input[0:]
    else:
        # equal split, send num of users
        share_unit = [len(user_ids)]
    split_obj = split_service.create_split(split_type, amount, share_unit, user_ids)
    payer = list(filter(lambda u: u.get_id() == payer_id, sample_users))
    if len(payer) == 0:
        return {
            'err_msg': output_messages['INVALID_USER_ID']
        }
    expense_obj = expense_model.Expense(payer[0], amount, split_obj)
    splitwise_instance.set_expense(expense_obj)
    return splitwise_instance

