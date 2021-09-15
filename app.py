import flask 
from flask import request, redirect
from flask_mysqldb import MySQL
from flask import jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dMvprYm.90'
app.config['MYSQL_DB'] = 'showroom'

mysql = MySQL(app)

@app.route('/products', methods=['GET'])
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    record = ['product_id','product_name','product_type','product_price','product_color']
    data = cur.fetchall()
    respdata = []
    for mainItem in data:
        indx = 0
        innerResp = {}
        for item in mainItem:
            innerResp[record[indx]] = item
            indx += 1
        respdata.append(innerResp)
    resp =jsonify(respdata)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    resp.headers['Access-Control-Expose-Headers'] = '*'
    resp.status_code = 200
    mysql.connection.commit()
    cur.close()
    return resp 


# @app.route('/products/<int:product_id>', methods =['GET'])
# def getProduct(product_id):
#     resp = []
#     cur = mysql.connection.cursor()
#     if product_id and request.method == 'GET':
#         cur.execute("SELECT * FROM product WHERE product_id = %s", str(product_id))
#         record = ['product_id','product_name','product_type','product_price','product_color']
#         data = cur.fetchall()      
#         for mainItem in data:
#             indx = 0
#             innerResp = {}
#             for item in mainItem:
#                 innerResp[record[indx]] = item
#                 indx += 1
#             resp.append(innerResp)
#     return jsonify(resp)

# @app.route('/products', methods =['POST'])
# def postProduct():
#     resp = []
#     cur = mysql.connection.cursor()
#     for prod in request.json:
#         product_id = prod['product_id']
#         product_name = prod['product_name']
#         product_type = prod['product_type']
#         product_price = prod['product_price']
#         product_color = prod['product_color']

#         if request.method == 'POST':
#             cur.execute("INSERT INTO product (product_id,product_name,product_type,product_price,product_color)VALUES(%s, %s, %s, %s, %s)",(product_id, product_name,product_type,product_price,product_color))
#     mysql.connection.commit()
#     cur.close()
#     return jsonify(resp)

# @app.route("/product/<int:product_id>", methods=['DELETE'])
# def update_product(product_id):
#     cur = mysql.connection.cursor()
#     if product_id and  request.method == 'DELETE':
#         cur.execute("DELETE FROM product WHERE product_id = %s", str(product_id))
#         resp = jsonify('Product deleted successfully')
#         resp.status_code =200
#     else:
#         resp = jsonify('Please give proper data')
#         resp.status_code = 400
#     mysql.connnection.commit()
#     cur.close()
#     return redirect('/products')


if __name__ == "__main__":
    app.run(debug = True)
