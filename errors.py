class ACPYError(Exception):
    pass

class FileNotValidError(ACPYError):
    pass

class ACPYSyntaxError(ACPYError):
    pass

class FileNotPassedError(ACPYError):
    pass