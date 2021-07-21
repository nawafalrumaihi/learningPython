while True:
    N = input("Please input factorial you would like to calculate: ")
    try: # try to ...
        N = int(N) # convert it to an integer.
    except ValueError: # If that didn't succeed...
        print("Invalid input: not an integer.")
        continue # retry by restarting the while loop.
    if N > 0: # valid input
        break # then leave the while loop.
    # If we are here, we are about to re-enter the while loop.
    print("Invalid input: not positive.")


N = input("Please input factorial you would like to calculate: ")
ans = 1
for i in range(1,N+1,1):
    ans = ans*i
print(ans)