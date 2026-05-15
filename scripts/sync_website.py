import os
import re

WEB_PATH = os.path.expanduser(
    "~/zenith-web"
)

OUTPUT_FILE = os.path.expanduser(
    "~/zenith-ai-content/brand/website_raw.txt"
)

allowed_extensions = [
    ".html",
    ".md",
    ".svelte"
]

all_content = []

for root, dirs, files in os.walk(WEB_PATH):

    dirs[:] = [

        d for d in dirs

        if d not in [
            "node_modules",
            ".git",
            "dist",
            ".svelte-kit",
            "build"
        ]
    ]

    for file in files:

        if any(
            file.endswith(ext)
            for ext in allowed_extensions
        ):

            path = os.path.join(root, file)

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                    text_blocks = re.findall(
                        r'>\s*([^<>{}]{4,200})\s*<',
                        content
                    )

                    clean_text = "\n".join(text_blocks)

                    if len(clean_text) > 50:

                        all_content.append(
                            f"\n\nFILE: {path}\n\n{clean_text}"
                        )

            except:
                pass

final_content = "\n".join(all_content)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(final_content)

print("\n")
print("Website cleaned and synced.")
print("\n")
print(f"Saved to: {OUTPUT_FILE}")
print("\n")
