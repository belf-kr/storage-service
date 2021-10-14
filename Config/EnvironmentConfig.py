import os

"""
Search parameter in environment variables and return the value when it is existed.
"""


def get_environment_variable(variable_name: str):
    env_value = os.getenv(variable_name)
    return env_value
