from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result

from api_v1.order.schemas import OrderCreate, OrderGet, OrderBase
from core.models import Order, OrderProductAssociation


async def create_order(session: AsyncSession, user_id: int) -> OrderCreate:
    is_item_active_order = await check_exist_active_order(
        session=session, user_id=user_id
    )

    if is_item_active_order:
        return await get_item_orders(session=session, order_id=is_item_active_order.id)

    order = Order(user_id=user_id)
    session.add(order)
    await session.commit()
    return await get_item_orders(session=session, order_id=order.id)


async def get_item_orders(
    session: AsyncSession, order_id: int
) -> Optional[OrderCreate]:
    return await session.scalar(
        select(Order)
        .where(Order.id == order_id)
        .options(selectinload(Order.user))
        .options(
            selectinload(Order.products_details).joinedload(
                OrderProductAssociation.product
            )
        )
        .order_by(Order.id)
    )


async def check_exist_active_order(
    session: AsyncSession, user_id: int
) -> Optional[OrderBase]:
    return await session.scalar(
        select(Order)
        .where(Order.user_id == user_id)
        .where(Order.order_status == "ACTIVE")
    )


async def get_active_item_orders(
    session: AsyncSession, user_id: int
) -> Optional[OrderCreate]:
    return await session.scalar(
        select(Order)
        .where(Order.user_id == user_id)
        .where(Order.order_status == "ACTIVE")
        .options(selectinload(Order.user))
        .options(
            selectinload(Order.products_details).joinedload(
                OrderProductAssociation.product
            )
        )
        .order_by(Order.id)
    )


async def get_orders(session: AsyncSession, user_id: int) -> list[OrderGet]:
    stmt = (
        select(Order)
        .where(Order.user_id == user_id)
        .options(selectinload(Order.user))
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
