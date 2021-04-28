def generate_capabilities_android(app_id: str) -> dict:

    return {
        'capabilities': {
            'browserstack.user': 'augustoteixeira_XcHa4y',
            'browserstack.key': 'wLD4zP4qHh79MpRrYh54',
            'project': 'First Behave Android Project',
            'build': 'Behave Android',
            'name': 'first_test',
            'browserstack.debug': True,
            'app': f'bs://{app_id}',
            'device': 'Google Pixel 3',
            'os_version': '9.0'
        }
    }
