from datetime import datetime
import pytz

bogota_tz = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_tz)
print ('Bogota: ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

mexico_tz = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_tz)
print ('Mexico: ', mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))
