#encoding:utf-8
# #用来初始化Flask对象、配置、注册蓝图、以及初始化各种第三方库
# from flask import Flask
# from app.house_views import house_blueprint
# from app.order_views import order_blueprint
# from app.user_views import user_blueprint
# from utils.config import Config
# from utils.functions import init_ext
# from utils.settings import TEMPLATE_DIR, STATIC_DIR

# def create_app():

#     # 初始化Flask对象
#     app = Flask(__name__,
#                 static_folder=STATIC_DIR,
#                 template_folder=TEMPLATE_DIR)

#     # 配置
#     app.config.from_object(Config)
    
#     # 初始化各种第三方库
#     init_ext(app)

#     # 注册蓝图
#     app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
#     app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
#     app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

   

#     return app