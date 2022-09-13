# Payment forms

**Payment forms** is a little application that can generate a page for paying for goods.
You can create a product or a set of products and generate a page to pay for them.\
*Made for familiarization with the library service Stripe.com


## 0. Set environment variables
In a root folder, create .env file wih the following contents:

```bash
    SECRET_KEY=django_secret_key
    STRIPE_API_KEY=stripe_secret_api_key
    STRIPE_PUBLIC_API_KEY=stripe_public_api_key
    DOMAIN=your_full_domain
    HOST=your_host_like(153.523.524.12)
    DEBUG=False
    DB_PASS=db_pass
    DB_NAME=db_name
    DB_USER=db_user
    DB_HOST=db_host
    DB_PORT=db_port
```

Or just

```bash
    export variables above
```

## 1. Run commands
    
**First run**

```bash
    docker-compose up -d --build
    docker-compose exec back python3 manage.py createsuperuser --username admin
```

## 2. Set up the app using Django admin panel

In order to access admin settings, follow the `<your-domain>/admin` URL and sign in
using the superuser credentials.
Create a product or set of products for testing endpoints.

## 3. Available endpoints

```
api/v1/item/{id}
api/v1/order/{id}
api/v1/buy/id - for manual generation session.id
```


# Stack:
  - Python
  - Django
  - DRF
  - Psql
  - Nginx
  - Gunicorn
  - Docker-compose
  - Django-money
  - Stripe
  - HTML + JS
