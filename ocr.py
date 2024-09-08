import pytesseract
import cv2

# Caminho para o executável do Tesseract (ajuste conforme a sua instalação)
caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract

# Carrega a imagem
imagem = cv2.imread("./inputs/sample.JPG")

# Extrai o texto da imagem
texto = pytesseract.image_to_string(imagem, lang="eng")

# Imprime o texto extraído
print(texto)
