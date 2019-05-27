# from classes.test_import.receiver_message import receive as t

# 导入包
from classes.test_import.receiver_message import receive

# t()

receive()

def getFuncationByName(module_name, funcation_name):
    module = __import__(module_name)
    return getattr(module, funcation_name)

print(repr(getFuncationByName("classes.test_import.receiver_message", "receive")))
