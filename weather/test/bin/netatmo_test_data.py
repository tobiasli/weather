"""Test data for netatmo_tests"""

MOCK_STATION_CONFIG = {'station:mock:id:1': {'_id': 'bogus:station:id:1',
                                             'cipher_id': 'bogus:cipher:information',
                                             'date_setup': 1550321641,
                                             'last_setup': 1550321641,
                                             'type': 'NAMain',
                                             'last_status_store': 1551959592,
                                             'module_name': 'Livingroom',
                                             'firmware': 137,
                                             'last_upgrade': 1550321642,
                                             'wifi_status': 51,
                                             'reachable': True,
                                             'co2_calibrating': False,
                                             'station_name': 'Superstation',
                                             'data_type': ['Temperature', 'CO2', 'Humidity', 'Noise', 'Pressure'],
                                             'place': {'altitude': 227.5,
                                                       'city': 'Madrid',
                                                       'country': 'ES',
                                                       'timezone': 'Europe/Madrid',
                                                       'location': [-3.716667, 40.383333]},
                                             'dashboard_data': {'time_utc': 1551959583,
                                                                'Temperature': 22.2,
                                                                'CO2': 810,
                                                                'Humidity': 35,
                                                                'Noise': 35,
                                                                'Pressure': 988.1,
                                                                'AbsolutePressure': 961.8,
                                                                'min_temp': 21.7,
                                                                'max_temp': 22.3,
                                                                'date_min_temp': 1551936324,
                                                                'date_max_temp': 1551956262,
                                                                'temp_trend': 'stable',
                                                                'pressure_trend': 'down'},
                                             'modules': [{'_id': 'bogus:module:id:1',
                                                          'type': 'NAModule4',
                                                          'module_name': 'Basement',
                                                          'data_type': ['Temperature', 'CO2', 'Humidity'],
                                                          'last_setup': 1551722412,
                                                          'reachable': True,
                                                          'dashboard_data': {'time_utc': 1551959569,
                                                                             'Temperature': 20.5,
                                                                             'CO2': 642,
                                                                             'Humidity': 32,
                                                                             'min_temp': 20.3,
                                                                             'max_temp': 20.5,
                                                                             'date_min_temp': 1551914554,
                                                                             'date_max_temp': 1551958647,
                                                                             'temp_trend': 'stable'},
                                                          'firmware': 44,
                                                          'last_message': 1551959589,
                                                          'last_seen': 1551959569,
                                                          'rf_status': 63,
                                                          'battery_vp': 6254,
                                                          'battery_percent': 100}]}}