import streamlit as st
import io

def remove_pdf_password(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        if reader.isEncrypted:
            reader.decrypt(password)
            writer = PyPDF2.PdfFileWriter()
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)
            return True
        else:
            return False

st.title("PDF Password Remover")

uploaded_file = st.file_uploader("Carga el PDF con contraseña", type="pdf")

if uploaded_file is not None:
    password = st.text_input("Introduce la contraseña del PDF")
    if st.button("Eliminar contraseña"):
        output_pdf = f"unlocked_{uploaded_file.name}"
        if remove_pdf_password(uploaded_file, output_pdf, password):
            st.success(f"¡Contraseña eliminada! Puedes descargar el PDF sin contraseña desde [este enlace]({output_pdf}).")
        else:
            st.error("El PDF no tiene contraseña o la contraseña proporcionada es incorrecta.")
