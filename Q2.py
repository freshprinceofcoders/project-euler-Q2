sequance = [1,2]
even_list = []
def my_game(n):
    num = 4000000
    for n in range(num):
        ans = sequance[-1] + sequance[-2]
        sequance.append(ans)
        #print(sequance)
        if ans % 2 == 0 :
            even_list.append(ans)
            even_list.append(n)
        answer = sum(even_list)
        print(answer) 
my_game('n')