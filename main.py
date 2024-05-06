import subprocess

def remove_pdf_password(input_pdf, output_pdf, password):
    command = f"qpdf --decrypt --password='{password}' {input_pdf} {output_pdf}"
    subprocess.run(command, shell=True)

input_pdf = "input.pdf"
output_pdf = "output.pdf"
password = "tu_contraseña"

remove_pdf_password(input_pdf, output_pdf, password)
print("Contraseña eliminada del PDF.")
