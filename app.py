# """Module providing a function printing python version."""
from flask import Flask
from flask import render_template
from flask import request
import mysql
import mysql.connector


app = Flask(__name__)


conexion = mysql.connector.connect(
    user='root',
    password='7884',
    host='localhost',
    database='handmade',
    port='3306')
print(conexion)
c = conexion.cursor()


@app.route('/')
def index():
    #    """Function printing python version."""
    return render_template('index.html')


@app.route('/servicios')
def servicios():
 #   """Function printing python version."""
    return render_template('servicio.html')


@app.route('/contacto')
def contacto():
  #  """Function printing python version."""
    return render_template('contacto.html')


@app.route('/cotiza')
def cotiza():
  #  """Function printing python version."""
    return render_template('cotiza.html')


@app.route('/cuento')
def cuento():
   # """Function printing python version."""
    return render_template('cuento.html')


@app.route('/datos', methods=['POST', 'GET'])
def datos():
  #  """Function printing python version."""
    if request.method == 'POST':
        nombre = request.form['nombre']
        ciudad = request.form['ciudad']
        direccion = request.form['direccion']
        celular = request.form['celular']
        idprod = request.form['idprod']
        cantidad = request.form['cantidad']
        print(nombre, ciudad, direccion, celular, idprod, cantidad)

    sql = "INSERT INTO pedido(nombre, ciudad, direccion, celular, idprod, cantidad) VALUES (%s,%s,%s,%s,%s,%s)"
    datos = (nombre, ciudad, direccion, celular, idprod, cantidad)
    c.execute(sql, datos)
    conexion.commit()
   # c.close()
   # conexion.close()
    return render_template('cotiza.html')


# @app.route('/consulta', methods=['POST', 'GET'])
# def consulta():
#    """Function printing python version."""

#   consul = "select * from producto"
#    c.execute(consul)
# pedido = c.fetchall()
#    c.close()
#   conexion.close()
    # return pedido
#    pedido
#   return render_template('revisar.html', pedido=pedido)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
