#!/usr/bin/env python3
"""
Simple color ramp generator for construction contractor website.
Creates perceptual ramps using direct calculations.
"""

import colorsys

def rgb_to_hex(r, g, b):
    """Convert RGB values (0-1) to hex string"""
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}".upper()

def hex_to_rgb(hex):
    """Convert hex string to RGB values (0-1)"""
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hsl(r, g, b):
    """Convert RGB to HSL"""
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360, s * 100, l * 100

def hsl_to_rgb(hue, saturation, lightness):
    """Convert HSL to RGB"""
    h = hue / 360.0
    s = saturation / 100.0
    l = lightness / 100.0
    
    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t += 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        
        q = l * (1 + s) if l < 0.5 else l - s + l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    
    return r, g, b

def generate_warm_gray_ramp():
    """Generate warm gray neutral ramp"""
    ramp = {}
    
    # Warm gray parameters
    base_hue = 35  # Warm yellow-bronze hue
    
    # Lightness values with perceptual spacing
    lightness_values = [
        96,   # 50 - very light
        90,   # 100 - light
        85,   # 200 - light
        80,   # 300 - medium light
        72,   # 400 - medium
        65,   # 500 - neutral base
        58,   # 600 - medium dark
        50,   # 700 - dark
        40,   # 800 - very dark
        30,   # 900 - almost black
        20    # 950 - near black
    ]
    
    # Saturation increases with darkness for warm grays
    for i, (step, lightness) in enumerate(zip(['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950'], lightness_values)):
        if lightness < 40:
            saturation = 20
        elif lightness < 60:
            saturation = 25
        elif lightness < 80:
            saturation = 15
        else:
            saturation = 10
        
        r, g, b = hsl_to_rgb(base_hue, saturation, lightness)
        ramp[step] = rgb_to_hex(r, g, b)
    
    return ramp

def generate_simple_ramp(base_hsl, base_color, is_status=False):
    """Generate a simple color ramp with proper perceptual spacing"""
    hue, saturation, lightness = base_hsl
    ramp = {}
    base_r, base_g, base_b = hex_to_rgb(base_color)
    
    # Lightness values with perceptual spacing (denser at light end)
    lightness_values = [
        96,   # 50 - very light
        90,   # 100 - light
        85,   # 200 - light
        78,   # 300 - medium light
        70,   # 400 - medium
        66,   # 500 - base color
        58,   # 600 - medium dark
        50,   # 700 - dark
        38,   # 800 - very dark
        25,   # 900 - almost black
        15    # 950 - near black
    ]
    
    # Adjust saturation for different ramp types
    if is_status:
        # Status colors have higher saturation
        status_saturation = saturation * 1.2
        sat_factor = 1.0
    else:
        # Brand colors have reduced saturation at ends
        sat_factor = 0.8
    
    for i, (step, target_lightness) in enumerate(zip(['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950'], lightness_values)):
        sat = 0  # Initialize sat variable
        
        if step == '500':
            # Base step is the exact brand color
            r, g, b = base_r, base_g, base_b
            sat = saturation
        elif target_lightness > 66:
            # Light end: interpolate between base and near-white
            t = (target_lightness - 66) / (96 - 66)
            r = base_r + (1 - base_r) * t
            g = base_g + (1 - base_g) * t
            b = base_b + (1 - base_b) * t
            
            # Adjust saturation for light end
            sat = saturation * sat_factor * (0.8 + 0.2 * t)
        elif target_lightness > 38:
            # Middle: keep base saturation
            r, g, b = hsl_to_rgb(hue, saturation, target_lightness)
            sat = saturation * sat_factor
        else:
            # Dark end: interpolate between base and near-black
            t = (15 - target_lightness) / (38 - 15)
            r = base_r * (1 - t) + 0.05 * t
            g = base_g * (1 - t) + 0.05 * t
            b = base_b * (1 - t) + 0.05 * t
            
            # Adjust saturation for dark end
            sat = saturation * sat_factor * (0.6 + 0.4 * t)
        
        # Convert to RGB for intermediate steps
        if step != '500':
            # Use HSL conversion for intermediate steps to maintain hue
            r, g, b = hsl_to_rgb(hue, sat, target_lightness)
        
        ramp[step] = rgb_to_hex(r, g, b)
    
    return ramp

def main():
    print("Generating simple color ramps for construction contractor website...")
    
    # Brand colors
    dark_navy = '#2B4C5E'  # Primary for "CASUAL" brand
    terracotta = '#E2583E'  # Secondary for "PAINTING AND CARPENTRY"
    
    # Status colors
    danger = '#E74C3C'      # Red
    warning = '#F39C12'      # Orange/Yellow
    success = '#27AE60'      # Green
    info = '#3498DB'         # Blue
    
    # Convert to HSL for reference
    dark_navy_hsl = rgb_to_hsl(*hex_to_rgb(dark_navy))
    terracotta_hsl = rgb_to_hsl(*hex_to_rgb(terracotta))
    danger_hsl = rgb_to_hsl(*hex_to_rgb(danger))
    warning_hsl = rgb_to_hsl(*hex_to_rgb(warning))
    success_hsl = rgb_to_hsl(*hex_to_rgb(success))
    info_hsl = rgb_to_hsl(*hex_to_rgb(info))
    
    print(f"Dark Navy: {dark_navy} -> HSL {dark_navy_hsl}")
    print(f"Terracotta: {terracotta} -> HSL {terracotta_hsl}")
    
    # Generate ramps
    neutral_ramp = generate_warm_gray_ramp()
    accent_ramp = generate_simple_ramp(dark_navy_hsl, dark_navy)
    secondary_accent_ramp = generate_simple_ramp(terracotta_hsl, terracotta)
    
    # Generate status ramps
    status_ramps = {
        'danger': generate_simple_ramp(danger_hsl, danger, is_status=True),
        'warning': generate_simple_ramp(warning_hsl, warning, is_status=True),
        'success': generate_simple_ramp(success_hsl, success, is_status=True),
        'info': generate_simple_ramp(info_hsl, info, is_status=True)
    }
    
    # Generate CSS output
    css = ":root {\n"
    
    # Neutral ramp
    css += "  /* Neutral ramp */\n"
    for step in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']:
        css += f"  --color-neutral-{step}: {neutral_ramp[step]};\n"
    css += "\n"
    
    # Accent ramp (Dark Navy)
    css += "  /* Accent ramp (Dark Navy) */\n"
    for step in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']:
        css += f"  --color-accent-{step}: {accent_ramp[step]};\n"
    css += "\n"
    
    # Secondary accent (Terracotta)
    css += "  /* Secondary accent (Terracotta) */\n"
    for step in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']:
        css += f"  --color-accent-secondary-{step}: {secondary_accent_ramp[step]};\n"
    css += "\n"
    
    # Status ramps
    css += "  /* Status ramps */\n"
    for status in ['danger', 'warning', 'success', 'info']:
        for step in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']:
            css += f"  --color-{status}-{step}: {status_ramps[status][step]};\n"
    css += "}\n"
    
    # Write to file
    output_path = "/home/jnobles/nny_dev/frontend/contractor/src/styles/color-ramps.css"
    with open(output_path, 'w') as f:
        f.write(css)
    
    print(f"Color ramps written to {output_path}")
    
    # Print some sample colors for verification
    print("\nSample colors:")
    print(f"Neutral 500: {neutral_ramp['500']}")
    print(f"Accent 500 (Dark Navy): {accent_ramp['500']}")
    print(f"Secondary Accent 500 (Terracotta): {secondary_accent_ramp['500']}")
    print(f"Danger 500: {status_ramps['danger']['500']}")
    print(f"Warning 500: {status_ramps['warning']['500']}")
    print(f"Success 500: {status_ramps['success']['500']}")
    print(f"Info 500: {status_ramps['info']['500']}")

if __name__ == "__main__":
    main()