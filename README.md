# -loan-monitoring
Rest Loan Monitoring API


## Commands

Comando para migrar

```bash
python manage.py makemigrations
```

Comando para realizar la migración

```bash
python manage.py migrate
```

Comando para crear super usuario.

```bash
python manage.py createsuperuser
```

Comando para iniciar servidor.

```bash
python manage.py runserver
```

## Routes

- /api/v1/crud/**:
    - /customers
    - /loans
    - /payments