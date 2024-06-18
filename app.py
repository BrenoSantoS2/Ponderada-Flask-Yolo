from flask import Flask, request, render_template, redirect, url_for
import os
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

# Carregar os modelos
model1 = load_model('models/conv_model.h5')
model2 = load_model('models/linear_model.h5')

# Definir o caminho para upload de arquivos
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verificar se o post request tem o arquivo
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Processar a imagem com os modelos
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # Ler a imagem em escala de cinza
            img = cv2.resize(img, (28, 28))  # Ajuste o tamanho conforme necessário
            img = np.expand_dims(img, axis=-1)  # Adicionar a dimensão do canal
            img = np.expand_dims(img, axis=0) / 255.0  # Adicionar a dimensão do batch e normalizar
            
            pred1 = model1.predict(img)
            pred2 = model2.predict(img)
            
            # Supondo que o modelo retorne uma array, pegando o índice da classe com maior valor
            classification1 = np.argmax(pred1, axis=1)[0]
            classification2 = np.argmax(pred2, axis=1)[0]
            
            return render_template('index.html', filename=filename, pred1=classification1, pred2=classification2)
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)
