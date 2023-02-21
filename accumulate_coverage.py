def main():
    filenames = [
        "coverage_boxplot.txt", "coverage_spectral_helper.txt",
        "to_rgba_no_colorcycle_helper.txt", "coverage_hexbin_file.txt",
        "coverage_bar.txt"
        ]
    for name in filenames:
        with open(name, "r") as f:
            contents = f.readlines()
            lists = [eval(i) for i in contents]
            out = [any(i) for i in zip(*lists)]
            num = out.count(True)
            print(f"coverage({name}) -- {num}/{len(out)}: {num * 100/len(out)}%: {out}")
            for i, elem in enumerate(out):
                if not elem:
                    print(i, end=", ")
            print()


if __name__ == "__main__":
    main()
