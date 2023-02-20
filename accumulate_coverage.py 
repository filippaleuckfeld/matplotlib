def main():
    with open("coverage_spectral_helper.txt", "r") as f:
        contents = f.readlines()
        lists = [eval(i) for i in contents]
        out = [any(lists[:][i]) for i in range(len(lists[0]))]
        num = out.count(True)
        print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")


if __name__ == "__main__":
    main()
