import logging
import traceback
from dtc.message_types.submit_new_single_order import SubmitNewSingleOrder

from dtc_client.dtc_client import DTCClient
from dtc.message_types.market_data_request import MarketDataRequest
from dtc.enums.request_action_enum import RequestActionEnum
from dtc.message_types.market_data_snapshot import MarketDataSnapshot
from lib.symbol_util import get_symbol_id
from lib.util import Util, CONSOLE_LOGGING

_NAME = 'name'
_ID = 'ID'


if __name__ == '__main__':
    # Symbols to monitor
    SYMBOL_LIST = [
        {_NAME: "ESU3.CME"},
        # {_NAME: "CLM20_FUT_NYMEX"}
    ]
    # Generate symbol IDs
    for ix, symbol in enumerate(SYMBOL_LIST):
        SYMBOL_LIST[ix][_ID] = get_symbol_id(symbol[_NAME])

    class ExampleDTCClient(DTCClient):
        def __init__(self):
            super().__init__(on_message_handler=self.on_message_thread, post_login_thread=self.post_login_thread)

        def post_login_thread(self):
            for ix, symbol in enumerate(SYMBOL_LIST):
                self.send(
                    MarketDataRequest(
                        request_action=RequestActionEnum.SUBSCRIBE,
                        symbol_id=SYMBOL_LIST[ix][_ID],
                        symbol=symbol[_NAME]))

                
            self.send(
                    SubmitNewSingleOrder(
                        # symbol=symbol[_NAME],
                        symbol="ESU3.CME",
                        exchange="CME",
                        trade_account="Sim1",
                        client_order_id = "15",
                        order_type=1,
                        buy_sell=1,
                        quantity=1,
                        time_in_force=1,
                        is_automated_order=1,
                        open_or_close=1,
                        is_parent_order=0,
                        )
            )
        def on_message_thread(self, message):
            if isinstance(message, MarketDataSnapshot):
                marketDataSnapshot = MarketDataSnapshot()
                # do something with market data


    try:
        logger = Util.setup_logging("DTC_Client", console=CONSOLE_LOGGING)
        dtc_client = ExampleDTCClient()
        dtc_client.start()
    except BaseException as e:
        logging.error(e.__str__())
        logging.debug(traceback.format_exc())
