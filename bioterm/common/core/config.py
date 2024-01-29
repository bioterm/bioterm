import os


def getenv_boolean(var_name, default_value=True) -> bool:
    """
    Returns the boolean representation of an environment variable's value.

    This function retrieves the value of the specified environment variable,
    converts it to upper case and checks if it is either "TRUE" or "1".
    If so, it returns True, otherwise False. If the environment variable does
    not exist, it returns the provided default value.

    Parameters
    ----------
    var_name : str
        The name of the environment variable to retrieve.
    default_value : bool, optional
        The default boolean value to return if the environment variable does not exist
         (default is True).

    Returns
    -------
    bool
        The boolean representation of the environment variable's value.

    Example
    -------
    >>> getenv_boolean('SOME_VAR', False)
    True  # if 'SOME_VAR' is set to 'True' or '1' in the environment variables,
    else False
    """
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result
