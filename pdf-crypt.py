import PyPDF2

def encrypt_pdf(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        
        for page_num in range(reader.numPages):
            writer.addPage(reader.getPage(page_num))
        
        writer.encrypt(password)
        
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

input_pdf = input("Introduce el nombre del archivo PDF que quieres encriptar: ")
output_pdf = "encrypted_" + input_pdf

password = input("Introduce la contraseña para encriptar el PDF: ")

encrypt_pdf(input_pdf, output_pdf, password)
print(f"¡Archivo PDF encriptado como {output_pdf}!")
