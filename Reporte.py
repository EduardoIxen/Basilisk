import webbrowser
from tabulate import *
import os.path

class Reporte:
    def crearHtml(self, lista, titulo):
        if lista != []:
            contador = 0
            listaFormateada = []
            dictTemp = {}
            #print(lista)
            keys = lista[0].keys()
            for item in lista:
                contador = contador + 1
                for key in keys:
                    dictTemp["No"] = contador
                    dictTemp[key] = item.get(key)
                listaFormateada.append(dictTemp)
                dictTemp = {}

            content = tabulate(listaFormateada, headers="keys", tablefmt='html')
            contenidoTabla = str(content)
            contenidoTabla = contenidoTabla.replace('<table>','<table class="table table-striped table-bordered" style="margin: 2%  auto; width:80%" >',1)
            contenidoTabla = contenidoTabla.replace('<thead>','<thead class="thead-dark">',1)
            contenidoTabla = contenidoTabla.replace('right','center')
            contenidoTabla = contenidoTabla.replace('<td>', '<td style="text-align: center;">')

            file =open(f"Reportes/{titulo}.html", "w")

            file.write('<!DOCTYPE html>')
            file.write('<html>')
            file.write('<head>')
            file.write('<title>Reporte</title>')
            file.write('<meta charset="utf-8">')
            file.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
            file.write(
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
            file.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
            file.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
            file.write('<link rel="stylesheet" href="css/estilo.css">')
            file.write(
                "<style>body{background: rgba(242,246,248,1);background: -moz-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -webkit-gradient(left bottom, right top, color-stop(0%, rgba(242,246,248,1)), color-stop(28%, rgba(216,225,231,1)), color-stop(100%, rgba(104,149,179,1)));background: -webkit-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -o-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -ms-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f2f6f8', endColorstr='#6895b3', GradientType=1 );}"
                "table{-webkit-box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);-moz-box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);}</style>")
            file.write('</head>')
            file.write('<body>')
            file.write('<center>')
            file.write(f'<h1>{titulo}</h1>')
            file.write(contenidoTabla)
            file.write('</center>')
            file.write('</body>')
            file.write('</html>')
            file.close()

            #obtiene la ruta absoluta del archivo
            opcion = input(f"Desea abrir el reporte {titulo}? S/N\n")
            if opcion == "S" or opcion == "s" or opcion == "SI" or opcion == "si" or opcion == "Si":
                my_path = os.path.abspath(os.path.dirname(__file__))
                path = os.path.join(my_path, f"../Reportes/{titulo}.html")
                path = path.replace("\\","/")
                path = path.replace("../","")
                webbrowser.open_new_tab(path)
            else:
                print("Archivo guardado en la carpeta 'Reportes'")