import lxml.etree as ET

def convert_svg_to_geometrydrawing(svg_file_path, output_file_path):
    """
    فایل SVG را به GeometryDrawing تبدیل می‌کند و نتیجه را در یک فایل متنی ذخیره می‌کند.
    """

    tree = ET.parse(svg_file_path)
    root = tree.getroot()

    with open(output_file_path, 'w') as f:
        for element in root.iter():
            if element.tag.endswith('path'):
                geometry = element.get('d')
                brush = element.get('fill')
                f.write(f'<GeometryDrawing Geometry="{geometry}" Brush="{brush}"/>\n')

if __name__ == "__main__":
    svg_file = "input.svg"  # مسیر فایل SVG ورودی
    output_file = "output.txt"  # مسیر فایل متنی خروجی
    convert_svg_to_geometrydrawing(svg_file, output_file)
    print(f"تبدیل با موفقیت انجام شد و نتیجه در فایل {output_file} ذخیره شد.")