# Imports
from utils_binance import download_1week
from utils_generic import make_candlestick_plot
from utils_telegram import telegram_bot_send_text, telegram_bot_send_photo


# Download data
df_BTCEUR = download_1week('BTCEUR')
df_ADAEUR = download_1week('ADAEUR')
df_DOTEUR = download_1week('DOTEUR')

# Make message
message = 'Buenos días!'

# Make plots
make_candlestick_plot(df_BTCEUR, 'BTCEUR')
make_candlestick_plot(df_ADAEUR, 'ADAEUR')
make_candlestick_plot(df_DOTEUR, 'DOTEUR')

# Send to telegram
telegram_bot_send_text(message)
telegram_bot_send_photo('./fig/fig_BTCEUR.png')
telegram_bot_send_photo('./fig/fig_ADAEUR.png')
telegram_bot_send_photo('./fig/fig_DOTEUR.png')
