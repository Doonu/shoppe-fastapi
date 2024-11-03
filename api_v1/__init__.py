from fastapi import APIRouter

from .product.views import router as products_router
from .user.views import router as user_router
from .profile.views import router as profile_router

router = APIRouter()

router.include_router(router=user_router, prefix="/users")
router.include_router(router=products_router, prefix="/products")
router.include_router(router=profile_router, prefix="/profile")
