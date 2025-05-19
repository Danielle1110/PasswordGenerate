from random import *

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
count = int(input('������� ���������� ������� ��� ���������: '))
length = int(input('������� ����� ������: '))
dig = input('�������� �� ����� 0123456789? (y/n): ')
low = input('�������� �� ��������� ����� ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
up = input('�������� �� �������� ����� abcdefghijklmnopqrstuvwxyz? (y/n): ')
punc = input('�������� �� ������� !#$%&*+-=?@^_? (y/n): ')
ne = input('��������� �� ������������� ������� il1Lo0O? (y/n): ')

if dig == 'y':
    chars += digits
if low == 'y':
    chars += lowercase_letters
if up == 'y':
    chars += uppercase_letters
if punc == 'y':
    chars += punctuation
if ne == 'y':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')

for i in range(count):
    print(generate_password(length, chars))
