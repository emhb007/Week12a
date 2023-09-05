import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='sakila',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a number of records
        sql = "SELECT first_name, last_name, email from Customer"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(len(result))
        print(result)

    with connection.cursor() as cursor:
        # Count records
        print("Query 2!\n")
        sql = "SELECT COUNT(customer_id) from Customer"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        print(result['COUNT(customer_id)'])

    with connection.cursor() as cursor:
        # Read a single record
        print("Query 3")
        sql = "SELECT first_name, last_name, email from Customer WHERE last_name=%s"
        cursor.execute(sql,'Lee')
        result = cursor.fetchone()
        print(result)

    with connection.cursor() as cursor:
        # Create a new record using INSERT
        print("Query 4 - inserting a record")
        sql = "INSERT INTO `actor` (first_name, last_name) VALUES (%s, %s)"
        print(sql)
        cursor.execute(sql, ('Eoghan', 'Barr'))

    # Commit to save changes to db.
    connection.commit()

    with connection.cursor() as cursor:
        # Search for record
        print('Query 5')
        sql = "SELECT first_name, last_name FROM actor WHERE last_name=%s "
        cursor.execute(sql, 'Barr')
        result = cursor.fetchall()
        print(len(result))
        print(result)
        for record in result:
            print(f"First name from the db is: {record['first_name']}")
            print(f"Surname from db is {record['last_name']}")

    with connection.cursor() as cursor:
        # Deletes all Barrs
        print("Query 6 - Delete!")
        sql = "DELETE FROM `actor` WHERE last_name = %s"
        cursor.execute(sql, 'Barr')
        # Commit to save changes to db.
        connection.commit()

    with connection.cursor() as cursor:
        # Search for record
        print('Query 7 - checking no Barrs')
        sql = "SELECT first_name, last_name FROM actor WHERE last_name=%s "
        cursor.execute(sql, 'Barr')
        result = cursor.fetchall()
        print(len(result))
        print(result)
        for record in result:
            print(f"First name from the db is: {record['first_name']}")
            print(f"Surname from db is {record['last_name']}")