from selenium import webdriver


def before_all(context):
    context.browser = context.config.userdata['browser']


def before_feature(context, feature):
    if 'web' in feature.tags:
        context.driver = webdriver.Chrome()
        context.drive.maximize_window()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_feature(context, feature):
    if 'web' in feature.tags:
        context.driver.quit()


def after_all(context):
    pass
