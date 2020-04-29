from rest_framework.exceptions import APIException


class ResultadosObtenidos(APIException):
    status_code = 200
    default_detail = "resultados obtenidos"
    default_code = "resultados_obtenidos"

class HamburguesaCreada(APIException):
    status_code = 201
    default_detail = "hamburguesa creada"
    default_code = "hamburguesa_creada"

class InputInvalido(APIException):
    status_code = 400
    default_detail = "input invalido"
    default_code = "input_invalido"

class OperacionExitosa(APIException):
    status_code = 200
    default_detail = "operacion exitosa"
    default_code = "operacion_exitosa"

class IdInvalido(APIException):
    status_code = 400
    default_detail = "id invalido"
    default_code = "id_invalido"

class HamburguesaInexistente(APIException):
    status_code = 404
    default_detail = "hamburguesa inexistente"
    default_code = "hamburguesa_inexistente"

class HamburguesaEliminada(APIException):
    status_code = 200
    default_detail = "hamburguesa eliminada"
    default_code = "hamburguesa_eliminada"

class ParametrosInvalidos(APIException):
    status_code = 400
    default_detail = "parametros invalidos"
    default_code = "parametros_invalidos"

class IngredienteCreado(APIException):
    status_code = 201
    default_detail = "ingrediente creado"
    default_code = "ingrediente_creado"

class IngredienteInexistente(APIException):
    status_code = 404
    default_detail = "ingrediente inexistente"
    default_code = "ingrediente_inexistente"

class IngredienteNoSePuedeBorrar(APIException):
    status_code = 409
    default_detail = "ingrediente no se puede borrar, se encuentra presente en una hamburguesa"
    default_code = "ingrediente_no_se_puede borrar,_se_encuentra_presente_en_una_hamburguesa"