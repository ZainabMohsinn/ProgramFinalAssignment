class Event:
    def __init__(self, eventId, eventType, theme, date, time, duration, venueAddress, clientId, guestList, cateringCompany, cleaningCompany,decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__eventId = eventId
        self.__eventType = eventType
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientId = clientId
        self.__guestList = guestList
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice

    def setEventId(self, eventId):
        self.__eventId = eventId

    def setEventType(self, eventType):
        self.__eventType = eventType

    def setTheme(self, theme):
        self.__theme = theme

    def setDate(self, date):
        self.__date = date

    def setTime(self, time):
        self.__time = time

    def setDuration(self, duration):
        self.__duration = duration

    def setVenueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

    def setClientId(self, clientId):
        self.__clientId = clientId

    def setGuestList(self, guestList):
        self.__guestList = guestList

    def setCateringCompany(self, cateringCompany):
        self.__cateringCompany = cateringCompany

    def setCleaningCompany(self, cleaningCompany):
        self.__cleaningCompany = cleaningCompany

    def setDecorationsCompany(self, decorationsCompany):
        self.__decorationsCompany = decorationsCompany

    def setEntertainmentCompany(self, entertainmentCompany):
        self.__entertainmentCompany = entertainmentCompany

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        self.__furnitureSupplyCompany = furnitureSupplyCompany

    def setInvoice(self, invoice):
        self.__invoice = invoice

    def getEventId(self):
        return self.__eventId

    def getEventType(self):
        return self.__eventType

    def getTheme(self):
        return self.__theme

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getDuration(self):
        return self.__duration

    def getVenueAddress(self):
        return self.__venueAddress

    def getClientId(self):
        return self.__clientId

    def getGuestList(self):
        return self.__guestList

    def getCateringCompany(self):
        return self.__cateringCompany

    def getCleaningCompany(self):
        return self.__cleaningCompany

    def getDecorationsCompany(self):
        return self.__decorationsCompany

    def getEntertainmentCompany(self):
        return self.__entertainmentCompany

    def getFurnitureSupplyCompany(self):
        return self.__furnitureSupplyCompany

    def getInvoice(self):
        return self.__invoice
