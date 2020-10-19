from src.constants import split_type as split_type_constant, valid_actions


def is_split_type_valid(split_type):
    if split_type.upper() in split_type_constant.values():
        return True
    return False


def is_action_valid(action):
    if action.upper() in valid_actions.values():
        return True
    else:
        return False
