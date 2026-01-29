from typing import List, Dict, Any
from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor(dictionary=True)


def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    query = """
        SELECT customerName, creditLimit
        FROM customers
        WHERE creditLimit < 10 OR creditLimit > 100000
        """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_orders_with_null_comments():
    """Return orders that have null comments."""
    query = """
        SELECT orderNumber, comments
        FROM orders
        WHERE comments IS null
        ORDER BY orderDate DESC
        """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_first_5_customers():
    """Return the first 5 customers."""
    query = """
        SELECT 
            customerName, 
            contactLastName, 
            contactFirstName
        FROM customers 
        ORDER BY contactLastName
        """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_payments_total_and_average():
    """Return total and average payment amounts."""
    query = """
        SELECT 
            SUM(amount),
            AVG(amount),
            MIN(amount),
            MAX(amount)
        FROM payments
            """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    query = """
                """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    query = """
                """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    query = """
                """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    query = """
                """

    cursor.execute(query)
    results = cursor.fetchall()
    return results
