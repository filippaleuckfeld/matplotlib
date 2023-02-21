def main():
    with open("coverage_hexbin_file.txt", "r") as f:
        contents = f.readlines()
        lists = [eval(i) for i in contents]
        # out = [any(lists[i][:]) for i in range(len(lists[0]))]
        out = [any(i) for i in zip(*lists)]
        num = out.count(True)
        res = [((i), (out[i])) for i in range(len(out))]
        #print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {res}")
        print(f"coverage -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")


if __name__ == "__main__":
    main()