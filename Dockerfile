# Use a imagem base do Python
FROM python:3.8

# Configuração do diretório de trabalho
WORKDIR /mnt/code

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código-fonte do Django RestFramework para o contêiner
COPY api ./api

# Copie o código-fonte do Django para o contêiner
COPY /processing ./processing

# Comando para executar o aplicativo após 5s da inicialização do container (para que espere o db estar pronto)
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]