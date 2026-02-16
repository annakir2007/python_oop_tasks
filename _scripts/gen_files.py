import os

labs_count = 7
for _ in range(1, labs_count+1):
    folder_name = f"lab{_:02d}"
    full_path = os.path.join("src/", folder_name)
    readme_path = os.path.join(full_path, "README.md")

    os.makedirs(full_path, exist_ok = True)

    with open(readme_path, "w", encoding="UTF-8") as f:
        f.write(f"# Лабораторная работа {_}\n\n")

""" 

    что угодно лишь бы не делать лабу? :)

"""

