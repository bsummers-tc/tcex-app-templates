"""App Module"""
# standard library
from typing import TYPE_CHECKING

# third-party
from app_inputs import AppInputs
from pydantic import ValidationError

if TYPE_CHECKING:
    # standard library

    # third-party
    from tcex import TcEx
    from tcex.input.input import Input
    from tcex.logger.trace_logger import TraceLogger


class ApiServiceApp:
    """Service App Class"""

    def __init__(self, _tcex: 'TcEx'):
        """Initialize class properties."""
        self.tcex: 'TcEx' = _tcex

        # properties
        self.exit_message = 'Success'
        self.inputs: 'Input' = self.tcex.inputs
        self.log: 'TraceLogger' = self.tcex.log

        # automatically parse args on init
        self._update_inputs()

    def _update_inputs(self) -> None:
        """Add an custom App models and run validation."""
        try:
            AppInputs(inputs=self.tcex.inputs)
        except ValidationError as ex:
            self.tcex.exit(code=1, msg=ex)

    def setup(self) -> None:
        """Perform setup actions."""
        self.log.trace('feature=app, event=setup')

    def shutdown_callback(self) -> None:
        """Handle the shutdown message."""
        self.log.trace('feature=app, event=shutdown-callback')

    def teardown(self) -> None:
        """Perform teardown actions."""
        self.log.trace('feature=app, event=teardown')
