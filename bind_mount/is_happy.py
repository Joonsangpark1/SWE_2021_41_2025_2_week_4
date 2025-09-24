def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        next_val = 0
        while n > 0:
            k = n % 10
            next_val += k * k
            n //= 10
        n = next_val

    return n == 1

if __name__=="__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    
    with open("/app/bind_mount/output.txt","w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        
        print("Results saved to /app/bind_mount/output.txt")
        
    