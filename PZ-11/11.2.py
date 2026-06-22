'''2.Составить генератор (yield), который преобразует все буквенные символы в
заглавные.
'''



def super(text):
    for i in text:
        yield i.upper()
t = 'jOWKMxjaKENDNWBk21883hkjxiou'
result = ''.join(super(t))
print(result)