from connectionDB import DatabaseConnection


class CatEmpleadoModel:
    def __init__(self):
        self.db = DatabaseConnection()

    def fetch_all(self):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute("select "
                               "ce.noemp,"
                               "(ce.nombre||' '||ce.app||' '||ce.apm) as nombre, "
                               "ce.area, "
                               "ce.status "
                               "from cat_empleado ce "
                               "left join datos_biometricos dbs "
                               "on ce.noemp = dbs.noemp "
                               "where ce.status = 'Activo' and dbs.noemp is null")
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(f"Error al consultar datos: {str(e)}")

    def search_emp(self, noemp):
        try:
            consultar = ("SELECT ce.noemp, (ce.nombre||' '||ce.app||' '||ce.apm) as nombre, ce.status "
                         "FROM cat_empleado ce "
                         "INNER JOIN datos_biometricos dbs ON dbs.noemp = ce.noemp "
                         "LEFT JOIN lista_asist la "
                         "ON la.noemp = ce.noemp "
                         "WHERE ce.noemp = %s AND dbs.rostro IS NOT NULL AND ce.status = 'Activo'")
            with self.db.connection.cursor() as cursor:
                cursor.execute(consultar, (noemp,))
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(f"Error al consultar datos: {str(e)}")
