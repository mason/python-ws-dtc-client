import logging
import traceback
import hashlib

from codegen.dtc_client.dtc_client import DTCClient
from dtc.message_types.market_data_request import MarketDataRequest
from dtc.enums.request_action_enum import RequestActionEnum
from dtc.message_types.market_data_snapshot import MarketDataSnapshot
from lib.util import Util, CONSOLE_LOGGING

_NAME = 'name'
_ID = 'ID'


def get_symbol_id(symbol):
    return int(hashlib.sha1(symbol.encode('utf-8')).hexdigest(), 16) % 4294967295


if __name__ == '__main__':
    # Symbols to monitor
    SYMBOL_LIST = [
        {_NAME: "ESM20_FUT_CME"},
        {_NAME: "CLM20_FUT_NYMEX"}
    ]
    # Generate symbol IDs
    for ix, symbol in enumerate(SYMBOL_LIST):
        SYMBOL_LIST[ix][_ID] = get_symbol_id(symbol[_NAME])

    class MyDTCClient(DTCClient):
        def __init__(self):
            super().__init__(on_message_handler=self.on_message_thread, post_login_thread=self.post_login_thread)

        def post_login_thread(self):
            logger.debug("post_login_thread")
            for ix, symbol in enumerate(SYMBOL_LIST):
                self.send(
                    MarketDataRequest(
                        request_action=RequestActionEnum.SUBSCRIBE,
                        symbol_id=SYMBOL_LIST[ix][_ID],
                        symbol=symbol[_NAME]))

        def on_message_thread(self, message):
            logger.debug("on_message_thread")
            if isinstance(message, MarketDataSnapshot):
                marketDataSnapshot = MarketDataSnapshot()
                # do something with market data


    try:
        logger = Util.setup_logging("DTC_Client", console=CONSOLE_LOGGING)
        dtc_client = MyDTCClient()
        dtc_client.start()
    except BaseException as e:
        logging.error(e.__str__())
        logging.debug(traceback.format_exc())
