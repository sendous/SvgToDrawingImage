import tkinter as tk
from tkinter import filedialog, messagebox
import lxml.etree as ET

def convert_svg_to_geometrydrawing(svg_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()

        drawings = []
        for element in root.iter():
            if element.tag.endswith('path'):
                geometry = element.get('d')
                brush = element.get('fill')
                if geometry and brush:
                    drawings.append(f'<GeometryDrawing Geometry="{geometry}" Brush="{brush}" />')

        drawing_group = "\n".join(drawings)
        final_output = f"""<DrawingImage>
<DrawingImage.Drawing>
<DrawingGroup>
{drawing_group}
</DrawingGroup>
</DrawingImage.Drawing>
</DrawingImage>"""

        return final_output
    except Exception as e:
        return f"خطا در پردازش فایل: {e}"


def open_svg_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("SVG files", "*.svg")],
        title="انتخاب فایل SVG"
    )
    if file_path:
        output = convert_svg_to_geometrydrawing(file_path)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)

def save_output_to_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="ذخیره خروجی به فایل"
    )
    if file_path:
        content = output_text.get(1.0, tk.END)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        messagebox.showinfo("ذخیره شد", f"فایل خروجی در {file_path} ذخیره شد.")

# ایجاد رابط گرافیکی
app = tk.Tk()
app.title("SVG به GeometryDrawing")

# آیکن دلخواه (فرمت .ico)
try:
    app.iconbitmap("icon.ico")  # آیکن رو در مسیر پروژه قرار بده
except:
    pass  # اگر نبود مشکلی نیست

# دکمه انتخاب فایل
select_button = tk.Button(app, text="انتخاب فایل SVG", command=open_svg_file)
select_button.pack(pady=10)

# TextArea برای نمایش خروجی
output_text = tk.Text(app, wrap="word", height=20, width=80)
output_text.pack(padx=10, pady=10)

# دکمه ذخیره
save_button = tk.Button(app, text="ذخیره خروجی به فایل", command=save_output_to_file)
save_button.pack(pady=10)

app.mainloop()
