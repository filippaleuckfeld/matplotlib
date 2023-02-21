def main():
    with open("coverage_bar.txt", "r") as f:
        contents = f.readlines()
        lists = [eval(i) for i in contents]
        out2 = [any(i) for i in zip(*lists)]
        out = [any(lists[:][i]) for i in range(len(lists[0]))]
        num = out2.count(True)
        print(f"coverage -- {num}/{len(out2)}: {num * 100/len(out2)}%: {out2}")


if __name__ == "__main__":
    main()