from selenium import webdriver


def before_all(context):
    context.browser = context.config.userdata['browser']
    context.driver = webdriver.Chrome()


def before_feature(context, feature):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    # context.driver.quit()
    pass
