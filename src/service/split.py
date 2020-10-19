from src.constants import split_type as split_type_constant
from src.helper import divide_amount_equally
from src.model import split as split_model


def create_equal_split(amount, num_users, user_ids):
    split_type = split_type_constant['EQUAL']
    total_amount = amount
    divider = num_users
    share_division = divide_amount_equally(total_amount, divider)
    user_share_map = {}
    for idx, user_id in enumerate(user_ids):
        user_share_map[user_id] = share_division[idx]
    split_obj = split_model.Split(split_type)
    split_obj.set_share(user_share_map)
    return split_obj
