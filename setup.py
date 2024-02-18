from setuptools import setup


setup(
    name='UserDataAPI',
    author='hardCodeMatter',
    install_requires=[
        'fastapi',
        'pydantic',
        'pydantic-settings',
        'SQLAlchemy',
        'uvicorn',
        'alembic',
        'psycopg2-binary',
    ],
)
