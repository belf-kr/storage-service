from typing import (
    Optional,
    Callable,
    Any,
    Union,
    Type,
    Dict
)

import aerich
import uvloop
from sanic import (
    Sanic,
    Request
)
from sanic.config import (
    Config,
    SANIC_PREFIX
)
from sanic.handlers import ErrorHandler
from sanic.router import Router
from sanic.signals import SignalRouter
from sanic_cors import CORS
from tortoise import Model
from tortoise.contrib.sanic import register_tortoise

from API import api
from Config.ApplicationConfig import ApplicationConfig
from Config.DatabaseConfig import DatabaseConfig
from Models import File


class TortoiseRouter:
    def db_for_read(self, model: Type[Model]):
        return "slave"

    def db_for_write(self, model: Type[Model]):
        return "master"


class Application(Sanic):
    def __init__(
            self,
            config: Optional[Config] = None,
            ctx: Optional[Any] = None,
            router: Optional[Router] = None,
            signal_router: Optional[SignalRouter] = None,
            error_handler: Optional[ErrorHandler] = None,
            load_env: Union[bool, str] = True,
            env_prefix: Optional[str] = SANIC_PREFIX,
            request_class: Optional[Type[Request]] = None,
            strict_slashes: bool = False,
            log_config: Optional[Dict[str, Any]] = None,
            configure_logging: bool = True,
            register: Optional[bool] = None,
            dumps: Optional[Callable[..., str]] = None,
    ) -> None:
        self.application_config = ApplicationConfig.get_instance()

        super().__init__(
            name=self.application_config.APP_NAME,
            config=config,
            ctx=ctx,
            router=router,
            signal_router=signal_router,
            error_handler=error_handler,
            load_env=load_env,
            env_prefix=env_prefix,
            request_class=request_class,
            strict_slashes=strict_slashes,
            log_config=log_config,
            configure_logging=configure_logging,
            register=register,
            dumps=dumps
        )

    def start(self):
        self.app_init()
        self.set_events()
        self.run(
            host=self.application_config.HOST,
            port=self.application_config.PORT,
            auto_reload=True
        )

    def set_events(self):
        @self.listener('before_server_start')
        async def before_server_start(app: Sanic, loop: uvloop.Loop):
            ...

        @self.listener('after_server_start')
        async def after_server_start(app: Sanic, loop: uvloop.Loop):
            ...

        @self.listener('before_server_stop')
        async def before_server_start(app: Sanic, loop: uvloop.Loop):
            ...

        @self.listener('after_server_stop')
        async def after_server_start(app: Sanic, loop: uvloop.Loop):
            ...

    def app_init(self):
        # CORS
        CORS(self)

        # Master Slave Config of MySQL Connection Info
        config = {
            "connections": {
                "master": DatabaseConfig.get_instance().get_connection_url(),
                "slave": DatabaseConfig.get_instance().get_connection_url()
            },
            "apps": {
                "models": {
                    "models": [File, aerich.models],
                    "default_connection": "master",
                }
            },
            "routers": [TortoiseRouter],
            "use_tz": False,
            "timezone": "asia/seoul",
        }

        register_tortoise(
            app=self,
            config=config,
            generate_schemas=True
        )

        # Blue Print
        self.blueprint(api)
