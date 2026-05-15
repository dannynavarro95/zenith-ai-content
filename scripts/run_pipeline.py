import os

print("\n")
print("SYNCING WEBSITE...")
print("\n")

os.system(
    "python3 sync_website.py"
)

print("\n")
print("BUILDING KNOWLEDGE...")
print("\n")

os.system(
    "python3 build_knowledge.py"
)

print("\n")
print("GENERATING CAMPAIGN...")
print("\n")

os.system(
    "python3 auto_instagram.py"
)

print("\n")
print("COMPOSING FINAL POST...")
print("\n")

os.system(
    "python3 compose_post.py"
)

print("\n")
print("PIPELINE COMPLETE.")
print("\n")
