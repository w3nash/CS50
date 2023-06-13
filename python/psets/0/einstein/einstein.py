def main():
    inp = input().strip()
    print(einstein(inp))


def einstein(m):
    m = int(m)
    E = m * 300000000**2
    return E


if __name__ == "__main__":
    main()
