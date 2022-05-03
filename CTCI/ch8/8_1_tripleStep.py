# hop n steps
# can hop 1,2,3 steps
# how many possible ways to run up stairs?

def triple_step(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    arr = [1, 2, 4]
    for i in range(3, n):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    return arr[n-1]

def triple_step_optimized(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    one = 1
    two = 2
    three = 4

    for i in range(4, n):
        next_value = one + two + three
        if i % 3 == 1: # update 1
            one = next_value
        elif i % 3 == 2: # update 2
            two = next_value
        elif i % 3 == 0: # update 3
            three = next_value
    return one + two + three



if __name__ == "__main__":
    print(triple_step(5))
    print(triple_step_optimized(5))