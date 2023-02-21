def main():
    with open("coverage_spectral_helper.txt", "r") as f:
        contents = f.readlines()
        lists = [eval(i) for i in contents]
        out = [any(i) for i in zip(*lists)]
        num = out.count(True)
        print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")
        for i, elem in enumerate(out):
            if not elem:
                print(i)


if __name__ == "__main__":
    main()
