""" config for  esp """

dev_name = 'esplana'
broker_host = '172.17.3.6'

room="workroom"

""" topics will be subscribed with pins name !"""
lights = (
        (4,"table_a"), 
        (5,"table_b")
        )

button = (13, 'table')
button_debounce = 0.2

led_pin = 15
