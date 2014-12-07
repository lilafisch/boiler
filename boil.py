import requests

s = requests.Session()
s.post('https://my.tado.com/j_spring_security_check', params={'j_username': someEmailAddress, 
          'j_password': somePassword})
s.post('https://my.tado.com/mobile/1.5/updateThermostatSettings', cookies=r.cookies, 
                    params={'setMode':'AUTO'})

