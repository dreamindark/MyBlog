from api.resources import Api
from api.common import Login,Get_code,Register,Logout
from article.views import Mian,Show
# from comment.views import Comments
api = Api()
api.add_resource(Login())
api.add_resource(Logout())
api.add_resource(Get_code())
api.add_resource(Register())
api.add_resource(Mian(name='main'))
api.add_resource(Show())
# api.add_resource(Comments())



