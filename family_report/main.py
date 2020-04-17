# **************************** Challenge: Family Report with Decorators ****************************
 
'''
Author: Trinity Terry
pyrun: python main.py
'''

def kids(sentence_func):
    def add_person(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"{original_sentence} by kids"
    return add_person

def dad(sentence_func):
    def add_person(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"{original_sentence} by Dad"
    return add_person






def mom(sentence_function):
    def add_person(*args, **kwargs):
        original_sentence = sentence_function(*args, **kwargs)
        return f"{original_sentence} by Mom"
    return add_person

@mom
def laundry():
    return "The dirty laundry was cleaned"

@kids
def garbage():
    return "The garbage was taken out"

@dad
def dust():
    return "The house was dusted"

def cook():
    return "The dog was brushed"

@kids
def eat():
    return "The food was eaten"

print(laundry())
print(garbage())
print(dust())
print(cook())
print(eat())