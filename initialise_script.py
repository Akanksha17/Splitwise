from sample_data import test_users
from src.model import user as user_model, splitwise as splitwise_model


def generate_sample_users():
    generated_users = []
    for user in test_users:
        test_user = user_model.User(user['name'], user['email'], user['phone_number'])
        generated_users.append(test_user)
    return generated_users


def initialise_app():
    sample_users = generate_sample_users()
    splitwise_instance = splitwise_model.Splitwise(sample_users)
    return splitwise_instance
