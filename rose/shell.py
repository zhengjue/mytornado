from auth.models import *
from admin.models import *
from canteen.models import *
from common.utils import connect_db
from common.utils import connect_redis
connect_db()
connect_redis()

