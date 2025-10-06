n,c,k = map(int,input().split())
print(k//(n*c)+1,'страница', k%(n*c)//n+1, "столбец", k%(n*c)%n, "строка")