from fastapi import APIRouter

from .product.views import router as products_router
from .user.views import router as user_router
from .profile.views import router as profile_router
from .post.views import router as post_router

router = APIRouter()

router.include_router(router=user_router, prefix="/user")
router.include_router(router=products_router, prefix="/product")
router.include_router(router=profile_router, prefix="/profile")
router.include_router(router=post_router, prefix="/post")
