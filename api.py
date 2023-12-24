from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root1"
app.config["MYSQL_DB"] = "customersdata"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

# ========================================================Accounts=====================================================================
# @app.route("/customersdata", methods=["GET"])
# def get_actors():
#     data = data_fetch("""select * from accounts""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_actor_by_id(id):
#     data = data_fetch("""SELECT * FROM accounts where customer_id = {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_actor():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     customer_type_code = info["customer_type_code"]
#     customer_name= info["customer_name"]
#     customer_phone = info['customer_phone']
#     customer_email = info['customer_email']
#     date_became_customer = info['date_became_customer']
    
    
#     cur.execute(
#         """ INSERT INTO accounts (customer_type_code, customer_name) VALUE (%s, %s, %s, %s, %s, %s)""",
#         (customer_type_code, customer_name, customer_phone, customer_email, date_became_customer ),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_actor(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     first_name = info["first_name"]
#     last_name = info["last_name"]
#     cur.execute(
#         """ UPDATE accounts SET customers_id= %s, customers_type_code = %s WHERE actor_id = %s """,
#         (first_name, last_name, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_actor(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM accounts where customer_id = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# ==============================================================customers=================================================================================

# @app.route("/customersdata", methods=["GET"])
# def get_actors():
#     data = data_fetch("""select * from customers""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_actor_by_id(id):
#     data = data_fetch("""SELECT * FROM customers where customer_id = {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_actor():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     customer_id = info["customer_id"]
#     customer_type_code= info["customer_type_code"]
#     customer_name = info['customer_name']
#     customer_phone = info['customer_phone']
#     customer_email = info['customer_email']
#     date_became_customer = info["date_became_customer"]
    
    
#     cur.execute(
#         """ INSERT INTO customers (customer_id, customer_type_code) VALUE (%s, %s, %s, %s, %s, %s)""",
#         (customer_id, customer_type_code, customer_name, customer_phone, customer_email, date_became_customer ),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_actor(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     customers_id = info["customers_id"]
#     customer_type_code= info["customer_type_code"]
#     cur.execute(
#         """ UPDATE accounts SET customers_id= %s, customer_type_code = %s WHERE customer_id = %s """,
#         (customers_id, customer_type_code),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_actor(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM customers where customer_id = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# =======================================================parties=========================================
# @app.route("/customersdata", methods=["GET"])
# def get_party_id():
#     data = data_fetch("""select * from parties""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_party_by_id(id):
#     data = data_fetch("""SELECT * FROM parties where party_id = {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_party_id():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     party_id = info["party_id"]
#     name= info["name"]
#     phone = info["phone"]
#     email = info['email']

    
#     cur.execute(
#         """ INSERT INTO parties (party_id, name) VALUE (%s, %s, %s, %s)""",
#         (party_id, name, phone, email ),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_party_id(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     party_id = info["party_id"]
#     name = info["name"]
#     cur.execute(
#         """ UPDATE parties SET party_id= %s, name = %s WHERE phone = %s """,
#         (party_id, name, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_party_id(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM parties where party_id = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# =========================================================ref_account_types========================================================

# @app.route("/customersdata", methods=["GET"])
# def get_party_id():
#     data = data_fetch("""select * from ref_account_types""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_party_by_id(id):
#     data = data_fetch("""SELECT * FROM ref_account_types where account_code= {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_party_id():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     account_type_code = info["account_type_code"]
#     account_type_description = info["account_type_description"]


    
#     cur.execute(
#         """ INSERT INTO ref_account_types (account_type_code, customer_name) VALUE (%s, %s,)""",
#         (account_type_code, account_type_description),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_party_id(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     party_id = info["party_id"]
#     name = info["name"]
#     cur.execute(
#         """ UPDATE ref_account_typess SET account_type_code = %s, account_type_code = %s WHERE account_type_description = %s """,
#         (party_id, name, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_party_id(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM ref_account_types where account_type_code = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# =======================================================ref_customer_types==================================================================
# @app.route("/customersdata", methods=["GET"])
# def get_party_id():
#     data = data_fetch("""select * from ref_customer_types""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_party_by_id(id):
#     data = data_fetch("""SELECT * FROM ref_customer_types where account_code= {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_party_id():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     customer_type_code = info["customer_type_code"]
#     customer_type_description = info["customer_type_description"]


    
#     cur.execute(
#         """ INSERT INTO ref_customer_types (customer_type_code, customer_type_description) VALUE (%s, %s,)""",
#         (customer_type_code, customer_type_description),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_party_id(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     party_id = info["party_id"]
#     name = info["name"]
#     cur.execute(
#         """ UPDATE  SET ref_customer_types = %s, customer_type_code = %s WHERE customer_type_description = %s """,
#         (party_id, name, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_party_id(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM ref_customer_types  where customer_type_description = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# =========================================================ref_transaction_types==========================
# @app.route("/customersdata", methods=["GET"])
# def get_party_id():
#     data = data_fetch("""select * from ref_transaction_types""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_party_by_id(id):
#     data = data_fetch("""SELECT * FROM ref_transaction_types where transaction_type_code= {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_party_id():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     transaction_type_code = info["transaction_type_code"]
#     transaction_type_description = info["transaction_type_description"]


    
#     cur.execute(
#         """ INSERT INTO ref_transaction_types ( transaction_type_code, transaction_type_description) VALUE (%s, %s,)""",
#         ( transaction_type_code, transaction_type_description),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_party_id(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     transaction_type_code = info["transaction_type_code"]
#     transaction_type_description = info["transaction_type_description"]
#     cur.execute(
#         """ UPDATE  SET ref_transaction_types = %s, transaction_type_code = %s WHERE transaction_type_description = %s """,
#         (transaction_type_code, transaction_type_description, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_party_id(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM ref_transaction_types  where customer_type_description = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )
# ================================================================transaction_messages==================================================
# @app.route("/customersdata", methods=["GET"])
# def get_party_id():
#     data = data_fetch("""select * from transaction_messages""")
#     return make_response(jsonify(data), 200)


# @app.route("/customersdata/<int:id>", methods=["GET"])
# def get_party_by_id(id):
#     data = data_fetch("""SELECT * FROM transaction_messages where tmessage_number= {}""".format(id))
#     return make_response(jsonify(data), 200)





# @app.route("/customersdata", methods=["POST"])
# def add_party_id():
#     cur = mysql.connection.cursor()
#     info = request.get_json()
    
#     message_number = info[" message_number"]
#     account_id = info[" account_id"]
#     counterparty_id= info["counterparty_id"]
#     party_id = info["party_id"]
#     transaction_type_code= info["transaction_type_code"]
#     counterparty_role = info["counterparty_role"]
#     currency_code= info["currency_code"]
#     BAN_Number = info["BAN_Number"]
#     transaction_date = info["transaction_date"]
#     amount = info["amount"]
#     balance= info["balance"]
#     location= info["location"]
#     party_role= info["party_role"]

#     cur.execute(
#         """ INSERT INTO transaction_messages (  message_number,  account_id) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)""",
#         ( message_number, account_id, counterparty_id, party_id, transaction_type_code, 
#          counterparty_role, currency_code, BAN_Number, transaction_date, amount, balance, location, party_role),
#     )
#     mysql.connection.commit()
#     print("row(s) affected :{}".format(cur.rowcount))
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor added successfully", "rows_affected": rows_affected}
#         ),
#         201,
#     )


# @app.route("/customersdata/<int:id>", methods=["PUT"])
# def update_party_id(id):
#     cur = mysql.connection.cursor()
#     info = request.get_json()
#     message_number = info[" message_number"]
#     account_id = info[" account_id"]
#     counterparty_id= info["counterparty_id"]
#     party_id = info["party_id"]
#     transaction_type_code= info["transaction_type_code"]
#     counterparty_role = info["counterparty_role"]
#     currency_code= info["currency_code"]
#     BAN_Number = info["BAN_Number"]
#     transaction_date = info["transaction_date"]
#     amount = info["amount"]
#     balance= info["balance"]
#     location= info["location"]
#     party_role= info["party_role"]
#     cur.execute(
#         """ UPDATE  SET transaction_messages = %s, message_number = %s WHERE account_id = %s """,
#         (message_number, account_id, counterparty_id, party_id, transaction_type_code, counterparty_role, currency_code, BAN_Number, transaction_date, amount, balance, location, party_role, id),
#     )
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor updated successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )


# @app.route("/customersdata/<int:id>", methods=["DELETE"])
# def delete_party_id(id):
#     cur = mysql.connection.cursor()
#     cur.execute(""" DELETE FROM transaction_messages  where message_number = %s """, (id,))
#     mysql.connection.commit()
#     rows_affected = cur.rowcount
#     cur.close()
#     return make_response(
#         jsonify(
#             {"message": "actor deleted successfully", "rows_affected": rows_affected}
#         ),
#         200,
#     )

if __name__ == "__main__":
    app.run(debug=True)
    
    

