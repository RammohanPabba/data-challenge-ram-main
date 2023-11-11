import csv
import random
import re
from faker import Faker
from datetime import datetime, time, timedelta


def csv_header():
    header = [
        "transaction_id",
        "transaction_status",
        "merchant_id",
        "merchant_name",
        "order_total_amount",
        "order_tax_amount",
        "shipping_address",
        "shipping_city",
        "shipping_state",
        "shipping_zip",
        "payment_datetime",
        "payment_method",
        "payment_bank_account_number",
        "payment_digital_wallet_account_number",
        "payment_attempt",
        "payment_status",
        "customer_name",
        "customer_email",
        "customer_phone",
        "customer_id",
    ]
    return header


def generate_merchants(num_merchants):
    fake = Faker("en_AU")
    merchants = []
    for _ in range(num_merchants):
        merchant_id = fake.uuid4()
        merchant_name = re.sub(r"[^a-zA-Z\s]", "", fake.company())
        merchants.append({"merchant_id": merchant_id, "merchant_name": merchant_name})

    return merchants


def generate_row(day, merchants):
    start_of_day = datetime.combine(day, time.min)
    end_of_day = datetime.combine(day, time.max) - timedelta(seconds=1)
    merchant = random.choice(merchants)

    fake = Faker("en_AU")
    payment_methods = ["bank", "digital_wallet"]
    payment_statuses = ["Success", "Pending", "Failed", "Fraud"]
    status = random.choices(payment_statuses, weights=[0.7, 0.1, 0.1, 0.1])[0]

    transaction_id = fake.uuid4()
    transaction_status = status
    merchant_id = merchant["merchant_id"]
    merchant_name = merchant["merchant_name"]
    order_total_amount = round(random.uniform(10.0, 500.0), 2)
    order_tax_amount = round(order_total_amount * 0.1, 2)
    shipping_address = fake.street_address()
    shipping_city = fake.city()
    shipping_state = fake.state_abbr()
    shipping_zip = fake.postcode()
    payment_datetime = fake.date_time_between(
        start_date=start_of_day, end_date=end_of_day + timedelta(days=1)
    )
    payment_method = random.choices(payment_methods, weights=[0.7, 0.3])[0]
    payment_bank_account_number = None
    payment_digital_wallet_account_number = None
    if payment_method == "bank":
        payment_bank_account_number = fake.random_int(100000, 999999)
        payment_digital_wallet_account_number = None
    else:
        payment_bank_account_number = None
        payment_digital_wallet_account_number = (
            "wallet_"
            + merchant_name.lower().replace(" ", "_")
            + "_"
            + fake.hexify(text="^^^^^^^")
        )

    payment_attempt = fake.random_int(1, 5)
    payment_status = status
    customer_name = fake.name()
    customer_email = fake.email()
    customer_phone = fake.phone_number()
    customer_id = fake.uuid4()

    row = [
        transaction_id,
        transaction_status,
        merchant_id,
        merchant_name,
        order_total_amount,
        order_tax_amount,
        shipping_address,
        shipping_city,
        shipping_state,
        shipping_zip,
        payment_datetime,
        payment_method,
        payment_bank_account_number,
        payment_digital_wallet_account_number,
        payment_attempt,
        payment_status,
        customer_name,
        customer_email,
        customer_phone,
        customer_id,
    ]
    return row


def main():
    num_rows = 200
    num_days = 7
    start_date = datetime(2023, 10, 20)
    num_merchants = 100
    merchants = generate_merchants(num_merchants)

    for _ in range(num_days):
        file_name = "./data/" + start_date.strftime("%Y-%m-%d") + ".csv"

        with open(file_name, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_header())

            for _ in range(num_rows):
                writer.writerow(generate_row(start_date, merchants))

        print(f"Sample data generated and saved to {file_name}")

        start_date += timedelta(days=1)


if __name__ == "__main__":
    main()
