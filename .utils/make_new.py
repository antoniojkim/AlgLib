# -*- coding: utf-8 -*-
import argparse
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

test_template = """# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from {name} import {name}
"""

implementation_template = """# -*- coding: utf-8 -*-


def {name}():
    pass
"""

link = "https://github.com/antoniojkim/AlgLib/blob/master/Algorithms"

readme_template = """# [{name}]()

## Problem



### Examples



## Solution



## [Implementation]({link}/{category}/{name_path}/{filename}.py#L)

```python

```

### Runtime

`O()`
"""


def main(args):
    categories = os.listdir(os.path.join(file_dir, "..", "Algorithms"))
    categories.sort()

    print("\nCategories")
    for i, category in enumerate(categories):
        print(f"{i}) {category}")

    while True:
        category = int(input("Choose a Category: "))
        if category >= 0 and category < len(categories):
            break

    category = categories[category]

    print(f"Creating an {category} algorithm called {args.name}")
    confirm = input("Enter y/Y to continue: ")

    if confirm.lower() == "y":
        os.mkdir(os.path.join(file_dir, "..", "Algorithms", category, args.name))
        os.mkdir(
            os.path.join(file_dir, "..", "Algorithms", category, args.name, "tests")
        )

        file_name = "_".join(args.name.lower().replace("'", "").split())

        with open(
            os.path.join(
                file_dir, "..", "Algorithms", category, args.name, "README.md"
            ),
            "w",
        ) as file:
            file.write(
                readme_template.format(
                    name=args.name,
                    link=link,
                    category=category.replace(" ", "%20"),
                    name_path=args.name.replace(" ", "%20"),
                    filename=file_name,
                )
            )

        with open(
            os.path.join(
                file_dir, "..", "Algorithms", category, args.name, f"{file_name}.py"
            ),
            "w",
        ) as file:
            file.write(implementation_template.format(name=file_name))

        with open(
            os.path.join(
                file_dir,
                "..",
                "Algorithms",
                category,
                args.name,
                "tests",
                f"test_{file_name}.py",
            ),
            "w",
        ) as file:
            file.write(test_template.format(name=file_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="Name of the new Algorithm")
    main(parser.parse_args())
