from itertools import combinations
import matplotlib.colors as mcolors
from wcag_contrast_ratio import rgb as contrast_ratio

# Color palette
colors = {
    "Crimson": "#6f1212",
    "Tangerine": "#bd5a20",
    "Royal Blue": "#0e13ac",
    "Turquoise": "#1ebec9",
    "Off-White": "#f5f2f7"
}

# Convert HEX to 0–255 RGB tuple
def hex_to_rgb_255(hex_code):
    r, g, b = mcolors.to_rgb(hex_code)
    return (int(r * 255), int(g * 255), int(b * 255))

# Check all combinations
pairs = list(combinations(colors.items(), 2))

for (name1, hex1), (name2, hex2) in pairs:
    rgb1 = hex_to_rgb_255(hex1)
    rgb2 = hex_to_rgb_255(hex2)

    # Text 1 on Background 2
    ratio1 = contrast_ratio(rgb1, rgb2)
    print(f"{name1} text on {name2} background - Contrast Ratio: {ratio1:.2f}")
    print(f"  AA Normal: {'PASS' if ratio1 >= 4.5 else 'FAIL'}")
    print(f"  AAA Normal: {'PASS' if ratio1 >= 7 else 'FAIL'}")
    print(f"  AA Large: {'PASS' if ratio1 >= 3 else 'FAIL'}")
    print(f"  AAA Large: {'PASS' if ratio1 >= 4.5 else 'FAIL'}\n")

    # Text 2 on Background 1
    ratio2 = contrast_ratio(rgb2, rgb1)
    print(f"{name2} text on {name1} background - Contrast Ratio: {ratio2:.2f}")
    print(f"  AA Normal: {'PASS' if ratio2 >= 4.5 else 'FAIL'}")
    print(f"  AAA Normal: {'PASS' if ratio2 >= 7 else 'FAIL'}")
    print(f"  AA Large: {'PASS' if ratio2 >= 3 else 'FAIL'}")
    print(f"  AAA Large: {'PASS' if ratio2 >= 4.5 else 'FAIL'}\n")
