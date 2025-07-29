def square_root(square_target,tolerance=1e-7,max_iteration=100):
    if square_target < 0:
        raise ValueError('error')
    elif square_target == 1 :
        print(f'suare root of {square_target} is 1')
    elif square_target == 0:
        print(f'suare root of {square_target} is 0')
    else:
        low=0
        high=max(1,square_target)
        root=None

        for _ in range(max_iteration):
            mid=(low+high)/2
            square_mid=mid**2
            if abs(square_mid-square_target)< tolerance:
                root=mid
                break
            elif square_mid < square_target:
                low=mid 
            else:
                high=mid

        if root is None:
            print("no root found ")
        else:
            print(f"aprrox square root is {root}")

        return root
    

N=16
square_root(N)