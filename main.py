import argparse
from pypdf import PdfWriter, PdfReader
import sys

sys.setrecursionlimit(sys.getrecursionlimit() * 5)
def main():
    parser = argparse.ArgumentParser(description="pdf ops")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-m",
        "--merge",
        nargs="+",  # This allows space-separated arguments
        help="list of pdfs to merge (in order)",
    )

    group.add_argument(
        "-s",
        "--split",
        help="a single pdf to split",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Optional output file name"
    )
    args = parser.parse_args()


    if args.merge:
        merger = PdfWriter()
        for _, file in enumerate(args.merge, start=1):
            merger.append(file)

        if args.output:
            merger.write(args.output)
        else:
            print("No output file name specified, using: merged.pdf")
            merger.write("merged.pdf")

    elif args.split:
        reader = PdfReader(args.split)

        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page=page)
            writer.write(f"{args.split.strip(".pdf")}-{i+1}.pdf")


if __name__ == "__main__":
    main()
