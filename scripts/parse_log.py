from _typeshed import FileDescriptorLike
import os

with open("recursive-png-to-jpg.log", "r") as file:
    files = file.read().splitlines()

actual_posts = []
for f in files:
    if f.endswith(".th.png") or f.endswith(".md.png"):
        pass
    else:
        actual_posts.append(f)

with open("actual_posts.log", "w") as file:
    file.write("\n".join(actual_posts).replace(".png", ".jpg"))