from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result

from api_v1.product import crud
from core.models import db_helper, Order, OrderProductAssociation

http_bearer = HTTPBearer()
# router = APIRouter(tags=["Order"], dependencies=[Depends(http_bearer)])
router = APIRouter(tags=["Order"])

# Сделать end point для получения заказов одного пользователя
# Сделать end point для получения активного заказа
# Сделать end point для получения заказа по id


@router.post("/")
async def create_order(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    # Создание заказа
    order = Order()
    session.add(order)
    await session.commit()

    return order


@router.post("/add-product")
async def add_product_in_order(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    first_order = await session.scalar(
        select(Order)
        .where(Order.id == 3)
        .options(
            selectinload(Order.products_details).joinedload(
                OrderProductAssociation.product
            )
        )
        .order_by(Order.id)
    )
    first_product = await crud.get_item_products(session=session, product_id=2)

    first_order.products_details.append(
        OrderProductAssociation(product=first_product, count=1)
    )
    await session.commit()


@router.get("/")
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    stmt = (
        select(Order)
        .options(
            selectinload(Order.products_details).joinedload(
                OrderProductAssociation.product
            )
        )
        .order_by(Order.id)
    )
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)
