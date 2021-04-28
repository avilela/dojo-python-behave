from selenium import webdriver
from capabilities.android import generate_capabilities_android
from helpers.browser_stack import upload_app
import ipdb

def before_all(context):
    context.browser = context.config.userdata['browser']
    context.app_path = context.config.userdata['app_path']
    context.app_name = context.config.userdata['app_name']


def before_feature(context, feature):
    if 'web' in feature.tags:
        context.driver = webdriver.Chrome()
        context.drive.maximize_window()
    if 'app' in feature.tags:
        app_id = upload_app(
            app_path=context.app_path, 
            app_name=context.app_name
        )
        desired_capabilities = generate_capabilities_android('batata')
        context.app_driver = webdriver.Remote (
            desired_capabilities=desired_capabilities,
            command_executor="http://hub-cloud.browserstack.com/wd/hub"
        )


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_feature(context, feature):
    if 'web' in feature.tags:
        context.driver.quit()


def after_all(context):
    pass
