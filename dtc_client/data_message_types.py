from dtc.enums.message_types import MessageTypes

MARKET_DATA_MESSAGE_TYPES = [
    MessageTypes.MARKET_DATA_UPDATE_TRADE,
    MessageTypes.MARKET_DATA_UPDATE_TRADE_COMPACT,
    MessageTypes.MARKET_DATA_UPDATE_TRADE_INT,
    MessageTypes.MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT,
    MessageTypes.MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR,
    MessageTypes.MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP,
    MessageTypes.MARKET_DATA_UPDATE_BID_ASK,
    MessageTypes.MARKET_DATA_UPDATE_BID_ASK_COMPACT,
    MessageTypes.MARKET_DATA_UPDATE_BID_ASK_INT,
    MessageTypes.MARKET_DATA_UPDATE_BID_ASK_NO_TIMESTAMP,
    MessageTypes.MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MILLISECONDS,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_OPEN,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_OPEN_INT,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_HIGH,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_HIGH_INT,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_LOW,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_LOW_INT,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_VOLUME,
    MessageTypes.MARKET_DATA_UPDATE_OPEN_INTEREST,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_SETTLEMENT,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_SETTLEMENT_INT,
    MessageTypes.MARKET_DATA_UPDATE_SESSION_NUM_TRADES,
    MessageTypes.MARKET_DATA_UPDATE_TRADING_SESSION_DATE
]

MARKET_DEPTH_MESSAGE_TYPES = [
    MessageTypes.MARKET_DEPTH_UPDATE_LEVEL,
    MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS,
    MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP,
    MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_INT
]

HISTORICAL_DATA_MESSAGE_TYPES = [
    MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_HEADER,
    MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE,
    MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE,
    MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE_INT,
    MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE_INT,
    MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_TRAILER
]