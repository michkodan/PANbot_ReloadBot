import requests

from config import MainConfig


class Duty(MainConfig):

    def get_duty(self):
        assignments = ''
        legal = ''
        develop = ''
        booking = ''
        mortgage = ''
        moscow = ''
        url = MainConfig.URL + 'contacts.ajax&mode=class&action=getContacts'
        try:
            request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            response = request.json()
            if response['data']['managersOnDuty']:
                data = response['data']['managersOnDuty']
                if data[0]['assignments']:
                    assignments = f'''
<b>Отдел переуступок:</b>  
{data[0]['assignments']['name']}
{data[0]['assignments']['position']}
E-mail: {data[0]['assignments']['email']}
Тел: {data[0]['assignments']['phone']}
WhatsApp: <a href="https://api.whatsapp.com/send?phone={data[0]['assignments']['watsApp']}">{data[0]['assignments']['watsApp']}</a>
'''
                if data[0]['legal']:
                    legal = f'''
<b>Юридический одел:</b>  
{data[0]['legal']['name']}
{data[0]['legal']['position']}
E-mail: {data[0]['legal']['email']}
'''
                if data[0]['develop']:
                    develop = f'''
<b>Отдел развития:</b> 
{data[0]['develop']['name']}
{data[0]['develop']['position']}
E-mail: {data[0]['develop']['email']}
Тел: {data[0]['develop']['phone']}
Telegram: @{data[0]['develop']['telegram']}
WhatsApp: <a href="https://api.whatsapp.com/send?phone={data[0]['develop']['watsApp']}">{data[0]['develop']['watsApp']}</a>
'''

                if data[0]['booking']:
                    booking = f'''
<b>Отдел бронирования:</b> 
{data[0]['booking']['name']}
{data[0]['booking']['position']}
E-mail: {data[0]['booking']['email']}
Тел: {data[0]['booking']['phone']}
Telegram: @{data[0]['booking']['telegram']}
WhatsApp: <a href="https://api.whatsapp.com/send?phone={data[0]['booking']['watsApp']}">{data[0]['booking']['watsApp']}</a>
'''
                if data[0]['mortgage']:
                    mortgage = f'''
<b>Ипотека:</b>  
{data[0]['mortgage']['name']}
{data[0]['mortgage']['position']}
E-mail: {data[0]['mortgage']['email']}
Тел: {data[0]['mortgage']['phone']}
Telegram: @{data[0]['mortgage']['telegram']}
WhatsApp: <a href="https://api.whatsapp.com/send?phone={data[0]['mortgage']['watsApp']}">{data[0]['mortgage']['watsApp']}</a>
'''
                if data[0]['moscow']:
                    moscow = f'''
<b>Москва:</b>  
{data[0]['moscow']['name']}
{data[0]['moscow']['position']}
E-mail: {data[0]['moscow']['email']}
Тел: {data[0]['moscow']['phone']}
Telegram: @{data[0]['moscow']['telegram']}
WhatsApp: <a href="https://api.whatsapp.com/send?phone={data[0]['moscow']['watsApp']}">{data[0]['moscow']['watsApp']}</a>
'''
                duty_list = f'{develop}{booking}{mortgage}{assignments}{moscow}{legal}'
            else:
                duty_list = '''
Сегодня мы работаем в обычном режиме.
Все менеджеры доступны по своим рабочим контактам 😉               
                '''
            return duty_list
        except Exception as e:
            return e
