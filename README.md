# Proyecto: Sistema de Gestión de Préstamos y Pagos

Este proyecto implementa un sistema de gestión de préstamos y pagos utilizando Django y Django REST Framework. El sistema permite gestionar clientes, préstamos y pagos, así como realizar validaciones complejas sobre los datos. A continuación se describe la estructura del proyecto y sus funcionalidades.

## Estructura del Proyecto

### Modelos

1. **Customer**: Representa a los clientes del sistema.
2. **Loan**: Representa los préstamos otorgados a los clientes.
3. **Payment**: Representa los pagos realizados por los clientes.
4. **PaymentDetail**: Detalles de los pagos, incluyendo el monto y el préstamo al que corresponde cada pago.

### Vistas

1. **CustomerViewSet**: Proporciona operaciones CRUD para los clientes.
2. **LoanViewSet**: Proporciona operaciones CRUD para los préstamos.
3. **PaymentViewSet**: Proporciona operaciones CRUD para los pagos.
4. **PaymentDetailViewSet**: Proporciona operaciones CRUD para los detalles de pagos.

### Serializadores

1. **CustomerSerializer**: Serializador para el modelo Customer.
2. **CustomerBalanceSerializer**: Serializador para obtener el balance del cliente.
3. **LoanSerializer**: Serializador para el modelo Loan.
4. **PaymentSerializer**: Serializador para el modelo Payment.
5. **PaymentDetailSerializer**: Serializador para el modelo PaymentDetail.

### URLs

Define las rutas para acceder a los diferentes endpoints del sistema.

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/jorgeluis2000/loan-monitoring.git
```

2. Crear un entorno virtual y activar:
```bash
python3 -m venv env
source env/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Realizar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Correr el servidor de desarrollo:

```bash
python manage.py runserver
```

### Alternativa

Correr el proyecto desde docker compose.

```bash
docker compose up -d --build
```

## Endpoints

### Panel admin

 - GET /admin

### documentation

 - GET /doc

### Access functionalities

 - GET /api/v1

La siguiente lista se complementa con **`/api/v1`** para poder acceder a ellas.

### Login

 - GET /credentials/: Lista todos los usuarios.
 - POST /credentials/: Crea un nuevo usuario.
 - GET /credentials/{id}/: Obtiene la información de un usuario específico.
 - PUT /credentials/{id}/: Actualiza la información de un usuario específico.
 - PUT /credentials/login/: Te entrega el token de autenticación de dicho usuario para poder utilizar el resto de la API.

#### Customers
 - GET /customers/: Lista todos los clientes.
 - POST /customers/: Crea un nuevo cliente.
 - GET /customers/{id}/: Obtiene la información de un cliente específico.
 - PUT /customers/{id}/: Actualiza la información de un cliente específico.
 - DELETE /customers/{id}/: Elimina un cliente específico.
 - GET /customers/{id}/balance/: Obtiene el balance del cliente.
 - GET /customers/{id}/loans/: Obtiene los préstamos del cliente.
 - GET /customers/{id}/payments/: Obtiene los pagos del cliente.
 - POST /create-customer-from-txt/: Crea clientes a partir de un archivo de texto.
#### Loans
 - GET /loans/: Lista todos los préstamos.
 - POST /loans/: Crea un nuevo préstamo.
 - GET /loans/{id}/: Obtiene la información de un préstamo específico.
 - PUT /loans/{id}/: Actualiza la información de un préstamo específico.
 - DELETE /loans/{id}/: Elimina un préstamo específico.
 - GET /get-loans-by-customer/{id}/: Obtiene los préstamos por cliente.
#### Payments
 - GET /payments/: Lista todos los pagos.
 - POST /payments/: Crea un nuevo pago.
 - GET /payments/{id}/: Obtiene la información de un pago específico.
 - PUT /payments/{id}/: Actualiza la información de un pago específico.
 - DELETE /payments/{id}/: Elimina un pago específico.
#### Payment Details
 - GET /paymentdetails/: Lista todos los detalles de pagos.
 - POST /paymentdetails/: Crea un nuevo detalle de pago.
 - GET /paymentdetails/{id}/: Obtiene la información de un detalle de pago específico.
 - PUT /paymentdetails/{id}/: Actualiza la información de un detalle de pago específico.
 - DELETE /paymentdetails/{id}/: Elimina un detalle de pago específico.

## Constantes

### Status del Cliente

```python
 STATUS_CUSTOMER = [
    (1, 'Activo'),    # Active customer
    (2, 'Inactivo')   # Inactive customer
]
```

### Status del Préstamo

```python
STATUS_LOAN = [
    (1, 'Pendiente'),  # Pending loan
    (2, 'Activo'),     # Active loan
    (3, 'Rechazado'),  # Rejected loan
    (4, 'Pagado')      # Paid loan
]
```

### Status del Pago

```python
STATUS_LOAN = [
    (1, 'Pendiente'),  # Pending loan
    (2, 'Activo'),     # Active loan
    (3, 'Rechazado'),  # Rejected loan
    (4, 'Pagado')      # Paid loan
]
```

## Ejemplo de Uso

1. Crear un cliente:

```bash
curl -X POST http://localhost:8000/customers/ -d '{"external_id": "12345", "score": 750}'
```

2. Crear un préstamo:

```bash
curl -X POST http://localhost:8000/customers/ -d '{"external_id": "12345", "customer_id": "<customer_id>", "maximum_payment_date": "datetime","amount": 100}'
```