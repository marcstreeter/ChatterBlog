

class Errors(Exception):
    __status_code = 400
    __error_cat = "General Error"
    __default_message = "System Error Occurred"

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.category = self.__error_cat
        self.message = message or self.__default_message
        self.status_code = status_code or self.__status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['category'] = self.__error_cat
        return rv

# System Errors
class SystemError(Errors):
    __error_cat = "System Error"
    __default_message = "Oops, Pardon us! An engineer has been notified and woken from slumber."
    __status_code = 500


# User Errors
class UserErrors(Errors):
    __error_cat = "User Error"
    __default_message = "Error Caused By User"

class InvalidUsageError(UserErrors):
    __default_message = "Invalid Usage"

class UnauthenticatedError(UserErrors):
    __default_message = "Unauthenicated Usage"
    __status_code = 401

class UnauthorizedError(UserErrors):
    __default_message = "Unauthorized Usage"
    __status_code = 403


