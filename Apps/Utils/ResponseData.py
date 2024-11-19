class ResponseData:
    pass
    def  __init__(self, Success, Status, Message, Record = None):
        self.Message = Message
        self.success = Success
        self.Status = Status
        self.Record = Record

    def toResponse(self):
        #Convertir los atributos de la instancia en un diccionario
        return self.__dict__