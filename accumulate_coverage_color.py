def main():
    filenames = ["to_rgba_no_colorcycle_helper.txt"]
    for name in filenames:
        with open(name, "r") as f:
            contents = f.readlines()
            lists = [eval(i) for i in contents]
            out = [any(i) for i in zip(*lists)]
            num = out.count(True)
            print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")
            print("Branches with no test coverage: ", end="")
            for i, elem in enumerate(out):
                if not elem:
                    print(i, end=" ")
            print("\n")


if __name__ == "__main__":
    main()