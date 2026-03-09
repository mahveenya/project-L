from sqlalchemy import select, func

from app.db.models.pokemon_model import PokemonModel


async def get_pokemon_db_models(session, offset, limit):
    stmt = select(PokemonModel).offset(offset).limit(limit)
    return await session.execute(stmt).scalars().all()


async def count_pokemon_db_models(session):
    stmt = select(func.count()).select_from(PokemonModel)
    return await session.scalar(stmt)


async def get_pokemon_db_model_by_id(session, pokemon_id):
    stmt = select(PokemonModel).where(PokemonModel.id == pokemon_id)
    return await session.execute(stmt).scalar_one_or_none()
