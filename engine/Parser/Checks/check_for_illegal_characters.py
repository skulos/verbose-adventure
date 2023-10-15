""" Insert """
from Components.regular_expression import validate_input
from Components.constants import *
from Logging.logging_config import logger


class IllegalCharactersException(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """
    pass


def check_for_illegal_characters(statement):
    """
    Checks for illegal characters in the given statement
    :param statement: (string)
    :return: returns true in case statement is clear of illegal characters and
    raises an exception if not.
    """
    logger.debug("Calling check_for_illegal_characters(%s)", statement)
    logger.debug("******************** starting input validation *******************")
    for _, char in enumerate(statement):
        if char in LEFT_BRACKETS or char in RIGHT_BRACKETS or char in WHITE_SPACES:
            continue
        if validate_input(char):
            continue
        else:
            logger.exception("FAIL: String contains illegal characters, please inspect: char=%s", char)
            raise IllegalCharactersException("Exception: String contains illegal characters.")
    logger.debug("******************** finished input validation *******************")

    logger.info("PASS: There were no illegal characters found.")
    return True  # returns True in case no fowl characters are found
