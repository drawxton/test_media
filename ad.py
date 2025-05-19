import requests
import os

# List of .webp image URLs
image_urls = [
"https://content.dashtoon.ai/user-uploaded-files/UPLno5wseqyRBVV3j3dXdachcbMfU6BaDt4.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLJorzBxoTSjiPeZXIIY1kwDyBqLeaIX9T.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLAK0KBodofGZVM0wlzr84rO1bkCHIIJea.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLtFsN2HPv8KlIFupt7YPXqRWoDUHMVF3f.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLwM5bo2WpmRYgXc4JnjAVd71oGeNghJle.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLkz9tpaSbaJfPyr2DlOBvx3YAcfmaWZcY.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLQsN9iKAdjpVkhkSIPQfJYI4TRlpCQ7jT.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPL4AK0Yr6QV5Wj461sdEioEzfHIjIp8agm.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLQRPY5J1nb6nbWRcr646dR2yMB5KSOVMX.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLvFQIkfDPRYwwt8MLsqW9IRWhgyeYxgrw.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPL9JBkYrkRDXUW6gmFiNGSzBveHxSqh8US.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLz0aXzOopV34CtHsk7FmkdK01nyGMSZ6s.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLvYLNqndPEOfFEJzHmpAYxcQfrKNthw6r.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLci9ZksmNAMBrAaz5ohr33WEcs8uSIJTH.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLSzk9wm42jqjqnrK2qOkGq2rg62lr6ACS.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPL2JMozRjs1d0gJ4DOw1bZEnmsKwVMUbsB.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPL14Kf2qvlmbIGGtNKYPATMVcLbJV8BGcJ.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLVo5tsma1mxsNMzx8yhPRNPGZmUVq226M.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLMM4vigf9XoeqEiWD8RzWW9Yc7HMSuCpl.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLVKBh2n29K9eXG9Jq9VLaUThtyRtTEoVF.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLSX1VX4fFi4auvXv2RW1ky0Xqz8lZhhRt.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLK1yOTxAJnLrktwn3ArjOungmmNig1OTH.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLKdJ6ChOQX2Y4UpeC8K2ySBmhcuOIuGl7.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPL62snjUveARhdHm9ERCMgsgLYOVfnnB6e.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLM4RfuA1zag0J8IqwZdfuP4f9JHXvOnVL.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLXlxZL9YmKSKCOpGjQiM6ZGJUFAs71c6i.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLTUBlKyKivuV17Ucc5uUIfj7fZ0n7pTsv.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLhFW6JUXLcftSFev69HypvGzf0RAz1jIX.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLRylMN37O2HmB6f5LvKi9ZWbPjwX15Kfh.webp",
"https://content.dashtoon.ai/user-uploaded-files/UPLjLqqejeXtivsp7wpzDx36uPS9tl1AT60.webp",
]

# Output directory
output_dir = "downloaded_webp_images"
os.makedirs(output_dir, exist_ok=True)

# Download each image
for idx, url in enumerate(image_urls):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract file name or use index fallback
        filename = os.path.basename(url) or f"image_{idx}.webp"
        if not filename.endswith(".webp"):
            filename += ".webp"

        filepath = os.path.join(output_dir, filename)

        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
