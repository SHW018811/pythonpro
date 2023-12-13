arr = {}

def frequency_analytic(s):
    for i in s:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1
    print(arr)

if __name__ == "__main__":
    msg = input("input your message: ")
    frequency_analytic(msg)
