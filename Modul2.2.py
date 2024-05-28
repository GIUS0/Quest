first= int(input('Введите число:'))
second=int(input('Введите 2-е число:'))
third=int(input('Введите 3-е число:'))
if first==second==third:
    print('3')
elif first==second!=third:
    print('2')
elif first!=second==third:
    print('2')
elif first==third!=second:
    print('2')
elif first!=second!=third:
    print('0')