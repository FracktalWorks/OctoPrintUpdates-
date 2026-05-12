from pypdf import PdfReader
reader = PdfReader(r'C:\Users\Asus\Desktop\fracktalworks\ControlCenter\Beginner_Machine_Setup_with_Katapult.pdf')
print(f'Total pages: {len(reader.pages)}')
for i, page in enumerate(reader.pages):
    print(f'--- PAGE {i+1} ---')
    print(page.extract_text())
    print()
