# botslack
Exemplo de um bot para Slack utilizando Python, Django e Celery

- **Django Admin**
   - *user: admin*
   - *password: admin123*

- **Comando para executar o beat do chatbot**
  - *python bot/beat.py*

- **Para uso do alarm no celery, executar o beat e o work do celery**
  - *python manage.py celery beat --loglevel=info*
  - *python manage.py celery worker --queue=alarm --concurrency=1 --app=botslack --loglevel=info*
  
- **Alterações**
  - *Em core/constants.py inserir o Token do Bot na constante TOKEN_SLACK_API*
  - *Em core/constants.py inserir o canal de comunicação a ser utilizado na constante TEAM_CHANNEL*
