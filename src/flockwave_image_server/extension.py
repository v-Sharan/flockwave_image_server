from __future__ import annotations

from logging import Logger
from trio import sleep
from typing import TYPE_CHECKING

from flockwave.server.ext.base import Extension

if TYPE_CHECKING:
    from flockwave.ext.base import Configuration
    from flockwave.server.app import SkybrushServer


__all__ = ("ExtensionTemplate", )

class ExtensionTemplate(Extension):
    """Template for Skybrush Server extensions."""

    async def run(
        self, app: SkybrushServer, configuration: Configuration, logger: Logger
    ):
        """This function is called when the extension was loaded.

        The signature of this function is flexible; you may use zero, one, two
        or three positional arguments after ``self``. The extension manager
        will detect the number of positional arguments and pass only the ones
        that you expect.

        Parameters:
            app: the Skybrush server application that the extension belongs to.
                Also available as ``self.app``.
            configuration: the configuration object. Also available in the
                ``configure()`` method.
            logger: Python logger object that the extension may use. Also
                available as ``self.log``.
        """
        logger.info("Extension is now running.")
        await sleep(2)
        logger.warn(configuration.get("bacon"))
        await sleep(3)
        logger.info("Five seconds have passed, exiting.")
        
