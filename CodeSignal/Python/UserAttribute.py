# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# At CodeSignal information about the users is stored in the database. Anny is working on the class representation of this information, and needs to come up with a class that creates objects with the following attributes: username, _id, xp and name. She has already come up with a test object:

# username: "annymaster"
# _id: "1234567"
# xp: "1500"
# name: "anny"
# The problem is, she doesn't know if this will be enough. It is possible that the server will require information about additional attributes that are not yet present in Anny's representation.

# Given the attribute the server requested, return its value if it is defined, and the <attribute> attribute is not defined string otherwise.

# Example

# For attribute = "_id", the output should be
# solution(attribute) = "1234567";

# For attribute = "age", the output should be
# solution(attribute) = "age attribute is not defined".


class User:
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, attr):
        return "{} attribute is not defined".format(attr)
    

def solution(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)
