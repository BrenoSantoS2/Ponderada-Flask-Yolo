## Como rodar o projeto:
_Obs: O tutorial de como rodar o projeto foi feito para Windows utilizando um terminal Bash_

Primeiramente crie um ambiente virtual e entre nele:

``` 
python -m venv venv
source venv/Scripts/activate
```

Após isso baixe as dependências do arquivo requirements.txt:

```
pip install -r requirements.txt
```

E por último rode o App.py para inicializar a interface com os modelos:

```
python app.py
```
Agora forcença as imagens do mnist e veja ele advinhando (Tem algumas já dentro do diretório uploads caso queira testar)
