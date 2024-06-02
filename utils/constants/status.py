# Define the statuses for the Customer model
STATUS_CUSTOMER = [
    (1, 'Activo'),    # Active customer
    (2, 'Inactivo')   # Inactive customer
]

# Define the statuses for the Loan model
STATUS_LOAN = [
    (1, 'Pendiente'),  # Pending loan
    (2, 'Activo'),     # Active loan
    (3, 'Rechazado'),  # Rejected loan
    (4, 'Pagado')      # Paid loan
]

# Define the statuses for the Payment model
STATUS_PAYMENT = [
    (1, 'Completado'), # Completed payment
    (2, 'Rechazado')   # Rejected payment
]
