# python3
def parallel_processing(n, m, data):
    output = []
    threads = [0]*n
    job_count = 0
    time = 0

    while job_count < m:
        for i in range(n):
            if threads[i] == 0 and job_count< m:
                threads[i] = data[job_count]
                job_count = job_count+ 1
                output.append([i, time])
            if threads[i]> 0:
                threads[i] = threads[i]- 1
        time = time+ 1

    return output

def main():
    full_input = input()
    n, m = map(int, full_input.split())

    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()