"""Manage a dairy cooperative's milk collection ledger."""

import hashlib
import sqlite3


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk delivery."""
    connection.execute(
        "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)",
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token(farmer):
    """Generate a SHA-256 token for a farmer."""
    return hashlib.sha256(farmer.encode()).hexdigest()


def daily_total(connection, day):
    """Calculate the total milk collected on a given day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?", (day,)
    ).fetchall()
    total = sum(row[0] for row in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(connection):
    """Find the farmer with the highest total delivery."""
    rows = connection.execute(
        "SELECT farmer, SUM(litres) FROM milk GROUP BY farmer"
    ).fetchall()
    if not rows:
        return None
    largest_farmer = max(rows, key=lambda row: row[1])
    return largest_farmer[0]


def print_slip(farmer):
    """Print a milk collection slip message."""
    print(f"printing slip for {farmer}")


def low_fat(connection):
    """Find farmers whose milk fat content is below 3.5 or missing."""
    rows = connection.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run the dairy milk collection ledger."""
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE milk ("
            "id INTEGER PRIMARY KEY, "
            "farmer TEXT, "
            "litres REAL, "
            "fat REAL, "
            "day TEXT)"
        )
    record_milk(connection, "Gopal", 12.5, 4.1, "Mon")
    record_milk(connection, "Lata", 20.0, 3.2, "Mon")

    print(
        daily_total(connection, "Mon"),
        top_farmer(connection),
        low_fat(connection)
    )
    print_slip("Gopal")
    print(farmer_token("Lata"))


if __name__ == "__main__":
    main()
