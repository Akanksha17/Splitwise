from src.constants import split_type as split_type_constant, output_messages
from src.helper import divide_amount_in_equal_share, divide_amount_by_percent_share
from src.model import split as split_model
from src.validation import is_exact_share_valid, is_percent_share_valid


def create_split(split_type, user_ids, share_division):
    user_share_map = {}
    for idx, user_id in enumerate(user_ids):
        user_share_map[user_id] = share_division[idx]

    split_obj = split_model.Split(split_type)
    split_obj.set_share(user_share_map)
    return split_obj


def create_equal_split(amount, num_users, user_ids):
    split_type = split_type_constant['EQUAL']
    total_amount = amount
    divider = num_users
    share_division = divide_amount_in_equal_share(total_amount, divider)
    split_obj = create_split(split_type, user_ids, share_division)
    return split_obj


def create_percent_split(amount, percent_share, user_ids):
    if not is_percent_share_valid(percent_share, len(user_ids)):
        return {
            'err_msg': output_messages['INVALID_PERCENT_SPLIT']
        }
    split_type = split_type_constant['PERCENT']
    total_amount = amount
    share_division = divide_amount_by_percent_share(total_amount, percent_share)
    split_obj = create_split(split_type, user_ids, share_division)
    return split_obj


def create_exact_split(amount, exact_share, user_ids):
    if not is_exact_share_valid(amount, exact_share, len(user_ids)):
        return {
            'err_msg': output_messages['INVALID_EXACT_SPLIT']
        }
    split_type = split_type_constant['EXACT']
    split_obj = create_split(split_type, user_ids, exact_share)
    return split_obj


def create_split_switch(split_type, total_amount, share, user_ids):
    split_switch = {
        split_type_constant['EQUAL']: create_equal_split,
        split_type_constant['PERCENT']: create_percent_split,
        split_type_constant['EXACT']: create_exact_split
    }
    func = split_switch.get(split_type.upper())
    return func(total_amount, share, user_ids)
