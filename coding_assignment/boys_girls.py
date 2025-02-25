def arrange_students(n, boys, girls):
    boys.sort()
    girls.sort()
    
    for i in range(n):
        if i % 2 == 0:
            if boys[i // 2] > girls[i // 2]:
                return "NO"
        else:
            if girls[i // 2] > boys[i // 2]:
                return "NO"
    
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        boys = list(map(int, input().split()))
        girls = list(map(int, input().split()))
        
        result = arrange_students(n, boys, girls)
        print(result)

if __name__ == "__main__":
    main()
