#using a memoized recursive solution
def fib(nth,fib_list):
    if fib_list[nth]!="null":
        return fib_list[nth]
    if nth==1 or nth==2:
        result=1    
    else:
        result=fib(nth-1, fib_list)+fib(nth-2, fib_list)
    fib_list[nth]=result
    return result    
repeat_prompt="yes"
while (repeat_prompt=="yes" or repeat_prompt=="y"):

    #prompt for getting n
    nth=int(input("Which fibonacci number do you want? (Enter a positive integer) "))
    #list containing fib series
    fib_list=["null"] * (nth+1)
    answer=fib(nth, fib_list)
    print(answer)
    repeat_prompt=input("Do you want to get another fibonacci number? (yes/no) ")
else:
    print("okay bye!")