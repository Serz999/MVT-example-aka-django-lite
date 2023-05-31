from my_django.router import Router
from .views import hello_veiw, home_veiw

router = Router()
router.register('/', home_veiw)
router.register('/hello', hello_veiw)