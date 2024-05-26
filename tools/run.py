
def calculate_binoninal_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return calculate_binoninal_coefficient(n - 1, k - 1) + calculate_binoninal_coefficient(n - 1, k)


def main():
    print("Hello, World!")
    print(f"(3 over 4) = {calculate_binoninal_coefficient(4, 3)}")


if __name__ == '__main__':
    main()
