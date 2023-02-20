def main():
    with open("to_rgba_no_colorcycle_helper.txt", "r") as f:
        contents = f.readlines()
        lists = [eval(i) for i in contents]
        out = [any(i) for i in zip(*lists)]
        num = out.count(True)
        print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")
        for i in range(0, len(out)):
            if not out[i]:
                print(i)


if __name__ == "__main__":
    main()
